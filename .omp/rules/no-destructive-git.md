---
condition: ["git reset --hard", "git clean -f", "git checkout -- \\.", "git rebase", "git commit --amend"]
interruptMode: always
---
No destructive git in a lane worktree: no hard resets, mass discards,
rebases, or amends. The harness owns git state. If the tree is wedged,
stop and report it instead of force-cleaning.
