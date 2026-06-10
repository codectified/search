"""
Copies isChainRef=True from english-mxbai to arabic-openai for matching
hadiths (matched by collection + hadithNumber). After this, the chain-ref
filter in _arabic_openai_search works properly at query time.

Run inside container:
    docker exec search-web-1 python3 /code/tests/backfill_arabic_chain_refs.py
"""
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk as es_bulk

es = Elasticsearch("http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=60)

# Step 1: Collect all (collection, hadithNumber) pairs where isChainRef=True
print("Scanning english-mxbai for isChainRef=True docs...")
chain_refs = set()
for hit in es_scan(es, index="english-mxbai",
        query={"query": {"term": {"isChainRef": True}}},
        _source=["collection", "hadithNumber"],
        size=500):
    s = hit["_source"]
    coll = s.get("collection", "")
    num  = str(s.get("hadithNumber", ""))
    if coll and num:
        chain_refs.add((coll, num))
print(f"  {len(chain_refs):,} chain-ref hadiths in english-mxbai")

# Step 2: Scan arabic-openai, find matching docs, bulk update
print("Scanning arabic-openai for matching hadiths to update...")
actions = []
for hit in es_scan(es, index="arabic-openai",
        query={"query": {"match_all": {}}},
        _source=["collection", "hadithNumber"],
        size=500):
    s    = hit["_source"]
    coll = s.get("collection", "")
    num  = str(s.get("hadithNumber", ""))
    if (coll, num) in chain_refs:
        actions.append({
            "_op_type": "update",
            "_index":   "arabic-openai",
            "_id":      hit["_id"],
            "doc":      {"isChainRef": True},
        })

print(f"  {len(actions):,} docs to update")

if actions:
    ok, errs = es_bulk(es, actions, raise_on_error=False, raise_on_exception=False)
    print(f"  Updated: {ok:,} | errors: {len(errs) if errs else 0}")
    es.indices.refresh(index="arabic-openai")

print("Done")
