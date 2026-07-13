---
condition: ["git push"]
interruptMode: always
---
Lane workers never push. The lane harness owns commits, branches, and the PR.
Finish your code changes and stop — the harness takes it from here.
