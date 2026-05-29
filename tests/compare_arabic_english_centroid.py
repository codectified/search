"""
Side-by-side comparison of arabic-openai (Arabic centroid search) vs
english-openai (English centroid search) for a set of queries.

Run inside container:
    docker exec search-web-1 python3 /code/tests/compare_arabic_english_centroid.py
"""
import urllib.request, urllib.parse, json, re, time

BASE = "http://localhost:5000"

QUERIES = [
    "comparing yourself to others",
    "forgiveness of sins",
    "visiting the sick",
    "honoring one's parents",
    "fasting in Ramadan",
    "prayer before sleeping",
    "giving charity",
]

MODELS = ["arabic-openai", "english-openai"]


def strip_html(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t or '')).strip()


def search(model, query, size=10):
    url = BASE + "/en/search?q=" + urllib.parse.quote(query) + "&model=" + model + "&mode=semantic&size=" + str(size)
    t0 = time.perf_counter()
    with urllib.request.urlopen(url, timeout=30) as r:
        body = json.loads(r.read())
    wall_ms = round((time.perf_counter() - t0) * 1000)
    return body, wall_ms


for q in QUERIES:
    print("\n" + "=" * 72)
    print("QUERY: " + q)
    print("=" * 72)
    results = {}
    for model in MODELS:
        try:
            body, wall_ms = search(model, q)
            hits = body.get("hits", {}).get("hits", [])
            meta = body.get("_meta", {})
            results[model] = [h["_source"].get("collection","") + " " + str(h["_source"].get("hadithNumber","")) for h in hits]
            print("\n  [" + model + "] wall=" + str(wall_ms) + "ms"
                  + " embed=" + str(meta.get("embed_ms","?")) + "ms"
                  + " clusters=" + str(meta.get("clusters", "?")))
            for i, h in enumerate(hits[:8], 1):
                s = h["_source"]
                text = strip_html(s.get("hadithText") or s.get("englishText", ""))[:100]
                print("    " + str(i) + ". [" + str(round(h["_score"], 3)) + "] "
                      + s.get("collection", "") + " " + str(s.get("hadithNumber", "")) + " — " + text)
        except Exception as e:
            print("  ERROR [" + model + "]: " + str(e))
            results[model] = []

    # Overlap analysis
    set_ar = set(results.get("arabic-openai", []))
    set_en = set(results.get("english-openai", []))
    overlap = set_ar & set_en
    only_ar = set_ar - set_en
    only_en = set_en - set_ar
    print("\n  Overlap: " + str(len(overlap)) + "/10 | only-arabic: " + str(sorted(only_ar)) + " | only-english: " + str(sorted(only_en)))
