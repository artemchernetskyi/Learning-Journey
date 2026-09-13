# Project State — Learning Journey

Last updated: 2026-09-13

## Purpose

This file is the short, current source of truth for the Learning Journey.
Detailed context: `DevOps/Linux.md`, `DevOps/Docker.md`, `DevOps/Python.md`, `PROGRESS.md`, and `ROADMAP.md`.

---

## Current stage

- **Main track:** DevOps
- **Current technology:** Python for DevOps
- **Completed setup:** Python Setup / Lesson 00 on 2026-09-13
- **Next learning step:** Python Lesson 01 (not started)

---

## Completed foundation

- Linux Lessons 01–19 and both Linux checkpoints completed; Linux foundation complete.
- Bash fundamentals and the health-check script completed; continue practising Bash.
- Docker Lessons 01–12 completed.
- Comprehensive Docker checkpoint passed with approximately **9/10**.
- [Docker Visitor Counter mini-project](Projects/docker-visitor-counter/README.md) completed on **2026-09-12**.
- The entire Docker block, including the checkpoint and mini-project, is complete.
- [Python Setup / Lesson 00](DevOps/Python.md) completed on **2026-09-13**: uv `0.12.13`, repository `.venv` based on system Python `3.12.3`, REPL practice, and the first program verified in the terminal and VS Code. No third-party Python packages were installed; the system package environment was unchanged.

---

## Review focus

- Practise combining Bash variables, conditions, arrays, loops, functions, return codes, and counters into complete scripts without examples.
- After **Python Lesson 05**, plan a short optional Linux refresher: `chmod`, `chown`, permissions, processes, services, logs, and SSH.
- Continue brief reviews of Docker checkpoint gaps: Dockerfile → image → container; `docker start` preserving container identity; `-v` versus `--mount` with missing bind-mount paths; environment-variable security; `ENTRYPOINT`, `CMD`, PID 1, and `--rm`; container `localhost`.

---

## Default lesson workflow

1. Short theory
2. Prediction question when useful
3. Small command batch
4. Wait for Artem's real output and analyse it
5. Troubleshooting task
6. Independent challenge
7. Cleanup
8. Update notes
9. Run relevant checks and review Git diff
10. Commit intended changes
11. Confirm a clean working tree

---

## Teaching rules

- English is the main technical language.
- Use Ukrainian for difficult explanations.
- Prefer practical scenarios over repetitive theory.
- Practical understanding is more important than memorization.
- Give commands in small batches.
- Explain why commands are used.
- Explain how to read their output.
- Mark reused Linux concepts as **Linux review**.
- Give hints before full answers when possible.
- Revisit weak topics in later lessons.
- Do not treat a successful command as proof that the concept is understood.

---

## Next action

Start **Python Lesson 01** using the existing repository `.venv` and selected VS Code interpreter `./.venv/bin/python`. Setup / Lesson 00 is complete; `uv init` and `pyproject.toml` were intentionally deferred.

After each completed lesson, update the relevant lesson notes, `PROGRESS.md`, and `PROJECT_STATE.md`; follow the Git workflow above and push to GitHub unless instructed otherwise.

---

## AI continuation rule

When continuing the Learning Journey after a break or in a new session:

1. Read `PROJECT_STATE.md` first.
2. Check detailed notes only when more context is needed.
3. Keep this file current and concise.
