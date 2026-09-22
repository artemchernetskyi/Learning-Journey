# Learning Journey Roadmap — Artem

## Main goal

My main goal is to become ready for a junior IT / DevOps-related position in 12–18 months.

This roadmap is flexible. If I need more time, I will extend the project. The most important thing is to build strong foundations and real practical skills.

The goal is not to learn everything at once. The goal is to move step by step and build a real portfolio.

---

## Core idea

This project combines:

- English
- Linux
- Git
- Markdown documentation
- Bash scripting
- Networking basics
- Docker
- Docker Compose
- Python for DevOps
- CI/CD
- Cloud
- Terraform
- Kubernetes
- Monitoring
- Interview preparation

English and DevOps should grow together.

Example:

Command:

ls -la

English explanation:

It shows all files, including hidden files.

---

## Current stage

Updated: 2026-09-22

Current level:

- English: A2+ / B1- communication
- Grammar: A2 / A2+
- IT / DevOps: beginner with practical Linux and Docker experience
- Linux: foundation phase completed
- Git: basic practical workflow
- Docker: Lessons 01–12, comprehensive checkpoint (approximately 9/10), and Docker Visitor Counter mini-project completed
- Docker Compose: basics, logs, and `exec` completed in Lesson 09; multiple services completed in Lesson 10; networking and service discovery completed in Lesson 11
- Python for DevOps: Python Setup / Lesson 00 completed on 2026-09-13; Python Lessons 01–02 completed on 2026-09-14; Python Lesson 03 completed on 2026-09-16; Python Lessons 04–05 completed on 2026-09-17; Python Lesson 06 completed on 2026-09-22; reading JSON and YAML configuration is next.
- CI/CD: not started yet
- Cloud: not started yet
- Terraform: not started yet
- Kubernetes: not started yet

Current progress:

- Ubuntu is the main Linux learning environment.
- Git and VS Code are used regularly.
- The Learning Journey repository is maintained on GitHub.
- Linux Lessons 01-19 are completed.
- Linux Checkpoint 01 and Checkpoint 02 are completed.
- Bash fundamentals are completed but need continued practice.
- Docker Lessons 01–12 are completed; the Docker lesson block is complete.
- Bind mounts, named volumes, and environment variables are completed.
- Docker Lesson 09 — Docker Compose basics, logs, and `exec` are completed.
- Docker Lesson 10 — Multiple Services is completed.
- Docker Lesson 11 — Docker Networking and Service Discovery is completed.
- Docker Lesson 12 — Image Optimization and Multi-Stage Builds is completed.
- The comprehensive Docker checkpoint was passed with approximately 9/10 on 2026-09-12.
- The [Docker Visitor Counter mini-project](Projects/docker-visitor-counter/README.md) was completed successfully on 2026-09-12.
- The Docker and Docker Compose phase, including the checkpoint and practical project, is complete.
- Python for DevOps: Python Setup / Lesson 00 completed on 2026-09-13; Python Lessons 01–02 completed on 2026-09-14; Python Lesson 03 completed on 2026-09-16; Python Lessons 04–05 completed on 2026-09-17; Python Lesson 06 completed on 2026-09-22; reading JSON and YAML configuration is next.

---

## Learning path after the Linux foundation

Docker (including Docker Compose)
→ final comprehensive Docker checkpoint + practical Docker project
→ Python for DevOps
→ CI/CD + GitHub Actions
→ Cloud fundamentals and provider decision
→ Terraform
→ Kubernetes
→ Monitoring and troubleshooting
→ Integrated DevOps projects

Complete each phase through practical exercises and a small working result before moving on. Time estimates are flexible; later phases can take longer than the original 12–18 month goal.

Optional: Ansible/configuration management can be revisited later only if relevant job vacancies or a real project require it. It is not a current priority.

---

## Phase 1 — Foundations

Estimated time: first 1–3 months

Main focus:

- English 60%
- Linux 40%

Topics:

- English grammar automation
- Past Simple
- Present Simple vs Present Continuous
- writing 8–10 sentence texts
- basic technical English
- Linux terminal basics
- files and directories
- permissions
- users
- package management
- basic system commands
- Git basics
- Markdown notes

Expected result:

I can use Ubuntu comfortably for learning.  
I can write simple English texts about my day, work, Linux, and learning progress.  
I can use Git for my notes and commits.

---

## Phase 2 — Git, Bash, and Linux practice

Estimated time: months 3–5

Topics:

- Git branches
- GitHub
- README files
- Markdown documentation
- Bash basics
- variables
- simple scripts
- file operations
- permissions
- services
- logs
- SSH basics
- networking basics

Expected result:

I can create simple Bash scripts and document them in English.  
I can explain basic Linux commands and Git workflow.  
I can start using GitHub as a learning portfolio.

---

## Phase 3 — Docker and Docker Compose

Estimated time: months 5–8

Topics:

- containers
- images
- Dockerfile
- docker run
- docker ps
- ports
- bind mounts and named volumes
- environment variables
- Docker Compose
- simple web application
- basic troubleshooting

Expected result:

I can containerize a simple application.  
I can run a small project with Docker Compose.  
I can explain what a container is in simple English.

Docker Lesson 11 — Docker Networking and Service Discovery is completed: default and custom networks, service-name DNS, container ports, protocol troubleshooting, and network isolation.

Docker Lesson 12 — Image Optimization and Multi-Stage Builds is completed: single-stage versus multi-stage images, image history, build-cache behaviour, build context, and `.dockerignore`.

Docker Lessons 01–12 are complete. On 2026-09-12, I passed the comprehensive Docker checkpoint with approximately **9/10** and successfully completed the Docker Visitor Counter mini-project. This completes the Docker block.

Checkpoint strengths:

- ports, Compose lifecycle, service-name DNS, and network isolation;
- multi-stage builds, build context/cache, and `.dockerignore`;
- logs, persistence, and troubleshooting.

Areas for continued review:

- Dockerfile → image → container build sequence;
- `docker start` preserving container identity;
- `-v` versus `--mount` missing-path behaviour;
- environment-variable security;
- `ENTRYPOINT`, `CMD`, PID 1, and `--rm`;
- `localhost` inside containers.

Portfolio result:

The [Docker Visitor Counter](Projects/docker-visitor-counter/README.md) connects Nginx, Go, and Redis using two networks, health checks, runtime configuration, and a persistent named volume. HTTP responses, persistence, network isolation, the read-only mount, and final cleanup were verified. Detailed results are recorded in [Docker notes](DevOps/Docker.md) and [progress](PROGRESS.md).

Next: begin Python for DevOps and continue short reviews of the checkpoint gaps.

---

## Phase 4 — Python for DevOps

Estimated time: after the full Docker block and final checkpoint/project

Completed: **Python Setup / Lesson 00 on 2026-09-13**, **Python Lesson 01 on 2026-09-14** (variables, data types, input, conversion, and arithmetic operators), **Python Lesson 02 on 2026-09-14** (conditional statements and Boolean logic), **Python Lesson 03 on 2026-09-16** (collections and DevOps data structures), **Python Lesson 04 on 2026-09-17** (loops and iteration), **Python Lesson 05 on 2026-09-17** (functions), and **Python Lesson 06 on 2026-09-22** (files and paths). Next Python milestone: **reading JSON and YAML configuration**.

Lesson 02 final documentation verification reproduced the expected disk and service results; all six runs exited `0`. The final service source has `maintenance_mode = False` after the temporary branch-priority test. Both source files were preserved during correction verification. Detailed results are recorded in [Python notes](DevOps/Python.md#python-lesson-02--conditional-statements-and-boolean-logic).

Lesson 03 covered lists, tuples, sets, dictionaries, nested collections, and an independent deployment validator across seven source files. The final BLOCKED scenario and temporary READY path were observed, the knowledge check was passed after clarification, and all final source hashes were preserved. Detailed results are recorded in [Python notes](DevOps/Python.md#python-lesson-03--collections-and-devops-data-structures).

Lesson 04 covered `for` and `while` loops, `range()`, `enumerate()`, dictionary iteration, counters and accumulators, `break`, `continue`, nested data, and status classification across eight source files. The final deployment monitor reported one READY, WARNING, CRITICAL, and SKIPPED service. The knowledge check was passed after clarification, all eight scripts exited successfully, and all final source hashes were preserved. Detailed results are recorded in [Python notes](DevOps/Python.md#python-lesson-04--loops-and-iteration).

Lesson 05 covered function definitions and calls, parameters and arguments, returned strings and Booleans, `print()` versus `return`, argument styles and defaults, local scope, multiple return paths, condition priority, dictionaries passed into functions, and a final deployment summary across seven source files. The final task was completed independently, the knowledge check was passed, all seven scripts exited successfully, and all final source hashes were preserved. Detailed results are recorded in [Python notes](DevOps/Python.md#python-lesson-05--functions).

Lesson 06 covered `pathlib` paths, reading, overwriting and appending text, idempotent updates, directory creation and scanning, portable script-relative paths, and a service summary. All seven scripts ran successfully in the required order, both repeated runs preserved the expected results, and the two portable scripts worked from another directory. All seven Python and both TXT file hashes were preserved. Detailed results are recorded in [Python notes](DevOps/Python.md#python-lesson-06--files-and-paths).

Local Python project management will use `uv`, while basic `pip` and `venv` concepts should still be understood. The current Ubuntu system has Python **3.12.3**.

Setup verified uv **0.12.13**, the repository `.venv` based on `/usr/bin/python3`, REPL practice, and the first program in the terminal and VS Code using `./.venv/bin/python`. No third-party Python packages were installed or system packages changed. `uv init` and `pyproject.toml` were intentionally deferred. Detailed results: [Python notes](DevOps/Python.md).

Topics:

- Python basics: variables, conditions, loops, and functions
- lists and dictionaries
- files and paths
- reading JSON and YAML configuration
- command-line arguments and environment variables
- HTTP requests and simple API use
- error handling, logging, and exit codes
- virtual environments and dependencies
- small automation scripts and basic tests

Completed checkpoint: early on **2026-09-17**, before finishing Python Lesson 05, I completed the short optional Linux refresher covering `chmod`, `chown`, permissions, processes with `pgrep` and `kill`, systemd services and `journalctl` logs, and SSH client/server troubleshooting with `systemctl` and `ss`. No persistent practice files were created.

Expected result:

I can write a Python script to check service health or summarize logs.

I can handle errors, test the result, and document how to run the script.

I can explain when I would use Bash or Python for a small DevOps task.

---

## Phase 5 — CI/CD and GitHub Actions

Estimated time: months 8–11

Topics:

- basic CI/CD idea
- GitHub Actions
- build pipeline
- test step
- Docker image build
- basic deployment workflow
- secrets basics
- pipeline documentation

Expected result:

I can create a simple CI/CD pipeline for my project.  
I can explain what happens when I push code to GitHub.  
I can document the pipeline in English.

---

## Phase 6 — Cloud fundamentals and provider decision

Estimated time: months 10–14

After Python and CI/CD, choose one primary cloud provider based on relevant entry-level vacancies in Poland. Candidate providers are Azure and AWS; GCP may be considered if job-market evidence supports it. No provider is chosen yet.

Topics:

- cloud basics
- selected primary provider basics
- resource organization in the selected provider
- virtual machines
- networking basics in cloud
- storage basics
- basic deployment
- cost awareness
- cloud security basics

Expected result:

I understand the basic idea of cloud infrastructure.  
I can deploy a simple service or VM in the selected primary cloud provider.
I can describe basic cloud resources in English.

---

## Phase 7 — Terraform basics

Estimated time: months 12–15

Topics:

- Infrastructure as Code
- Terraform basics
- providers
- resources
- variables
- outputs
- state
- simple infrastructure in the selected primary cloud provider
- documentation

Expected result:

I can create simple infrastructure using Terraform.  
I understand why Infrastructure as Code is useful.  
I can explain a basic Terraform project in an interview.

---

## Phase 8 — Kubernetes basics

Estimated time: months 14–18

Topics:

- why Kubernetes exists
- pods
- deployments
- services
- config maps
- secrets
- namespaces
- basic kubectl commands
- simple app deployment

Expected result:

I understand the basics of Kubernetes.  
I can deploy a simple app to a local or test Kubernetes environment.  
I can explain the difference between Docker and Kubernetes at a junior level.

Important note:

Kubernetes is not the first priority. It comes after Linux, Git, networking, Docker, Docker Compose, Python, CI/CD, cloud, and Terraform practice.

---

## Phase 9 — Monitoring and troubleshooting

Estimated time: later stage

Topics:

- logs
- metrics
- basic monitoring idea
- uptime
- alerts
- troubleshooting steps
- documenting incidents

Expected result:

I can explain simple technical problems and how I investigated them.  
I can write basic troubleshooting notes in English.

---

## Phase 10 — Integrated DevOps projects

Estimated time: after monitoring and troubleshooting basics

Extend the practical project built during earlier phases into a small complete deployment:

- use Python for health checks or operational automation
- build and test Docker images with GitHub Actions
- create infrastructure in the selected primary cloud provider with Terraform
- deploy the application and practise a small Kubernetes deployment where useful
- add logs, basic metrics, and alerts
- practise troubleshooting and recovery
- document setup, architecture, costs, cleanup, and lessons learned

Expected result:

I can demonstrate a working service from source code to deployment.

I can explain each tool's role and investigate a simple failure at a junior DevOps level.

---

## Portfolio projects

By the end of this journey, I want to have two portfolio projects.

### Project 1 — Learning Journey Knowledge Base

This repository is my first project.

It shows:

- my learning process
- English progress
- Linux notes
- Git history
- DevOps roadmap
- mistakes and corrections
- technical explanations in English

Interview value:

I can show that I learn systematically, document my work, and improve over time.

### Project 2 — Practical DevOps Project

The Docker foundation is complete: [Docker Visitor Counter](Projects/docker-visitor-counter/README.md), completed on 2026-09-12. It can grow through later phases into an integrated DevOps project.

Possible technologies:

- Linux
- GitHub
- Docker
- Docker Compose
- Python for DevOps
- CI/CD
- selected primary cloud provider
- Terraform
- basic monitoring
- maybe Kubernetes

Interview value:

I can show that I can build, containerize, deploy, and document a simple service.

---

## Job preparation stage

Estimated time: around months 12–18

Topics:

- CV
- LinkedIn
- GitHub profile
- interview English
- common junior IT questions
- Linux interview questions
- Git questions
- Docker questions
- basic cloud questions
- explaining my projects

Possible first job directions:

- Junior IT Support
- Technical Support
- Linux Support
- Junior System Administrator
- Cloud Support
- DevOps Intern
- DevOps Trainee
- Junior DevOps-related role

The first job does not have to be a perfect DevOps Engineer position.  
The first goal is to enter the IT / infrastructure path and continue growing.

---

## Personal rules

1. Do not learn everything at once.
2. Build strong foundations first.
3. Practice English every lesson.
4. Write short texts regularly.
5. Document everything in Markdown.
6. Use Git from the beginning.
7. Build two real portfolio projects.
8. Prefer consistency over intensity.
9. Do not rush into Kubernetes, Terraform, or cloud too early.
10. Learn by doing, not only by watching courses.

---

## Key sentence

Consistency is more important than intensity.
