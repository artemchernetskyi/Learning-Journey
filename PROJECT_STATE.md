# Project State — Learning Journey

Last updated: 2026-09-16

## Purpose

This file is the short, current source of truth for the Learning Journey.
Detailed context: `DevOps/Linux.md`, `DevOps/Docker.md`, `DevOps/Python.md`, `PROGRESS.md`, and `ROADMAP.md`.

---

## Current stage

- **Main track:** DevOps
- **Current technology:** Python for DevOps
- **Completed setup:** Python Setup / Lesson 00 on 2026-09-13
- **Latest completed lesson:** Python Lesson 03 on 2026-09-16
- **Next learning step:** Python Lesson 04 (not started)

---

## Completed foundation

- Linux Lessons 01–19 and both Linux checkpoints completed; Linux foundation complete.
- Bash fundamentals and the health-check script completed; continue practising Bash.
- Docker Lessons 01–12 completed.
- Comprehensive Docker checkpoint passed with approximately **9/10**.
- [Docker Visitor Counter mini-project](Projects/docker-visitor-counter/README.md) completed on **2026-09-12**.
- The entire Docker block, including the checkpoint and mini-project, is complete.
- [Python Setup / Lesson 00](DevOps/Python.md) completed on **2026-09-13**: uv `0.12.13`, repository `.venv` based on system Python `3.12.3`, REPL practice, and the first program verified in the terminal and VS Code. No third-party Python packages were installed; the system package environment was unchanged.

- [Python Lesson 01](DevOps/Python.md#python-lesson-01--variables-data-types-input-conversion-and-arithmetic-operators) completed on **2026-09-14**: variables, basic data types, dynamic typing, input, conversion, f-strings, comparisons, and arithmetic operators. Both programs were verified, including the `80%` disk-warning boundary and `10 % 4 = 2`. Final knowledge check: **4/5 before correction**; conversion direction corrected to **str → int**. Existing Python `3.12.3` environment used; no packages installed or network requests made.

- Python Lesson 02 — Conditional Statements and Boolean Logic completed on **2026-09-14**: first-match priority, comparisons, `and`/`or`/`not`, disk/resource and service-health exercises. Knowledge check: **4/5 before clarification**; Boolean composition and `=` versus `==` clarified. All six final documentation runs exited `0` and matched expected disk and service results. Maintenance mode was temporarily `True` to test priority, then restored to `False`, confirmed in the final source. Both source hashes were unchanged during correction verification. See [lesson notes](DevOps/Python.md#python-lesson-02--conditional-statements-and-boolean-logic).

- Python Lesson 03 — Collections and DevOps Data Structures completed on **2026-09-16**: lists, tuples, sets, dictionaries, nested collections, and a practical deployment validator across seven source files. The final validator reports BLOCKED because `git` is missing; the temporary READY path was also observed. Knowledge check: approximately **4.5/6 before clarification**, then passed after corrections. All seven final scripts exited `0`, and their source hashes were preserved. See [lesson notes](DevOps/Python.md#python-lesson-03--collections-and-devops-data-structures).

---

## Review focus

- Continue practising Boolean-expression composition and assignment versus comparison.
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

The next lesson is **Python Lesson 04** (not started), using the existing repository `.venv` and selected VS Code interpreter `./.venv/bin/python`. Setup / Lesson 00 and Python Lessons 01–03 are complete; `uv init` and `pyproject.toml` were intentionally deferred.

After each completed lesson, update the relevant lesson notes, `PROGRESS.md`, and `PROJECT_STATE.md`; follow the Git workflow above and push to GitHub unless instructed otherwise.

---

## AI continuation rule

When continuing the Learning Journey after a break or in a new session:

1. Read `PROJECT_STATE.md` first.
2. Check detailed notes only when more context is needed.
3. Keep this file current and concise.
