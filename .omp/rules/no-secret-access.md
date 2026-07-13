---
condition: ["OPENROUTER_API_KEY", "BLACKCUBE_WORKER_TOKEN", "OMP_TOKEN", "FLEET_MERGE_TOKEN", "agent\\.db", "printenv", "\\.omp/agent"]
interruptMode: always
---
Never read, print, or copy credentials or the omp auth store. A lane worker
needs no secrets — tools are already authenticated. Anything that surfaces a
token in output is treated as exfiltration and fails review.
