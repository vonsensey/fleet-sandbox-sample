---
condition: [".blackcube.json", ".github/workflows/**", ".omp/**"]
interruptMode: always
---
Never modify the fleet gate, CI workflows, or omp config (.blackcube.json,
.github/workflows/, .omp/). These files are the safety boundary of this lane;
changes to them are rejected in review. Solve the task without touching them.
