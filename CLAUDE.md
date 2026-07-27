# CLAUDE.md

*(This file didn't exist before 2026-07-27. HQ's ceo/ role added the
section below under a narrow, explicit exception — see
`C:\dev\hq\ceo\CLAUDE.md`'s infrastructure-pattern exception. Nothing else
in this file was written by that role; add your own project conventions
above this line as normal.)*

## Shared HQ infrastructure: ChatGPT-export knowledge base

A local Elasticsearch index over ~2 years of Omar's ChatGPT conversation
history is running at `http://127.0.0.1:9200` (index `chatgpt-export`,
2,582 conversations, full text). This project doesn't have a dedicated
custom-GPT label yet, but a keyword pass found 143 loosely-related
conversations (Elasticsearch, hadith, narrator/isnad topics) going back to
2023-08 — search broadly rather than filtering by `gpt_project_label`:

```bash
curl -s -X POST http://127.0.0.1:9200/chatgpt-export/_search \
  -H "Content-Type: application/json" \
  -d '{"query": {"match": {"full_text": "YOUR QUERY"}},
       "size": 5, "_source": ["title", "create_date"]}'
```

Full docs: `C:\dev\chatgpt-export\README.md`. Not authoritative — cross-check
findings against this repo's own git history and docs.
