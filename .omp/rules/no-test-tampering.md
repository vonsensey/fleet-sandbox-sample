---
condition: ["pytest.*--deselect", "pytest.*--ignore", "@pytest\\.mark\\.skip", "pytest\\.skip\\(", "unittest\\.skip"]
interruptMode: always
---
Never skip, deselect, or delete a failing test to make the suite green.
Fix the code until the real test suite passes. If a test is genuinely wrong,
say so in your summary instead of silencing it.
