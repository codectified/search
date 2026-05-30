import json, time, os
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from collections import Counter
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

es = Elasticsearch("http://172.31.250.10:9200", basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]))
urns, vraw = [], []
for hit in es_scan(es, index="english-mxbai",
                   query={"query":{"match_all":{}},"_source":["urn","semantic_text"]}, size=200):
    s = hit["_source"]
    chunks = s.get("semantic_text",{}).get("inference",{}).get("chunks",[])
    if chunks and chunks[0].get("embeddings"):
        urns.append(str(s.get("urn", hit["_id"])))
        vraw.append(chunks[0]["embeddings"])
vectors = normalize(np.array(vraw, dtype=np.float32), norm="l2")
print(f"Loaded {len(urns):,} vectors dim={vectors.shape[1]}")
for k in [5, 10, 15, 20, 25, 30]:
    km = MiniBatchKMeans(n_clusters=k, batch_size=4096, max_iter=200, n_init=5, random_state=42)
    labels = km.fit_predict(vectors)
    cents = normalize(km.cluster_centers_, norm="l2")
    sim = cents @ cents.T
    p93 = sum(1 for i in range(k) for j in range(i+1,k) if sim[i,j]>0.93)
    p85 = sum(1 for i in range(k) for j in range(i+1,k) if sim[i,j]>0.85)
    counts = Counter(labels.tolist())
    sizes = sorted(counts.values(), reverse=True)
    top2 = sum(sizes[:2])
    coh = float(np.mean([float((vectors[labels==ki] @ cents[ki]).mean()) for ki in range(k) if (labels==ki).sum()>0]))
    print(f"k={k:2d}: coh={coh:.3f} p93={p93:3d} p85={p85:3d} median={sizes[len(sizes)//2]:4d} top2={top2:,}({100*top2/len(urns):.1f}%)")
