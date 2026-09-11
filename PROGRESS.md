# Progress — Learning Journey

## Current status

This file documents my progress in the Learning Journey project.

The goal is to track what I learn, what I practice, what problems I solve, and what I improve over time.

---

## 2026 — Project start

### Day 1 — Project setup

What I did:

- Connected Ubuntu to the internet.
- Installed Git.
- Installed Visual Studio Code.
- Created the project folder:

/home/artem/Projects/Learning-Journey

- Initialized a Git repository.
- Created the first Markdown files.
- Made the first Git commit.
- Created the project README.
- Created the English profile.
- Created the learning roadmap.

### English progress

I practiced:

- Past Simple
- negative sentences with didn't
- questions with did
- short answers: Yes, I did / No, I didn't
- writing a longer text about my real day

Important grammar rule:

After did / didn't, use the base verb.

Examples:

Correct:

- I didn't go.
- Did you go?

Wrong:

- I didn't went.
- Did you went?

### Technical progress

I started using:

- Ubuntu
- Terminal
- Git
- VS Code
- Markdown

This is the beginning of my personal learning system.

---

## Next steps

Next things to do:

- Fill CHATGPT_GUIDE.md.
- Fill DAILY_ROUTINE.md.
- Fill WEEKLY_PLAN.md.
- Fill English/Mistakes.md.
- Fill DevOps/Linux.md.
- Continue practicing English writing.
- Learn basic Linux terminal commands.
- Make small commits regularly.

---

## Personal note

Consistency is more important than intensity.

Small stable steps are better than one overloaded session.

---

## Project setup progress

### Completed files

I created and updated the main project files:

- README.md
- CHATGPT_GUIDE.md
- ENGLISH_PROFILE.md
- ROADMAP.md
- PROGRESS.md
- DAILY_ROUTINE.md
- WEEKLY_PLAN.md
- English/Mistakes.md
- English/Grammar/Past_Simple.md
- English/Vocabulary/General.md
- DevOps/Linux.md

### What I learned

I practiced:

- creating files and folders in Linux
- using terminal commands
- writing Markdown notes
- using Git
- making commits
- documenting my progress
- combining English with Linux and DevOps

### Git practice

I used these Git commands:

- git init
- git status
- git add
- git commit
- git branch -m main

### English progress

I documented:

- my English level
- my current grammar focus
- Past Simple notes
- my common mistakes
- useful vocabulary
- writing practice rules

### Technical progress

I documented:

- basic Linux commands
- Git commands
- Ubuntu setup progress
- project path
- next Linux topics

### Personal note

This is the first real step of my Learning Journey project.

I am not only learning theory.  
I am building a real system for learning English, Linux, Git, and DevOps.
# Learning Journey Progress

Updated: 2026-07-13

## Current status

I completed the first 10 lessons of my Learning Journey and passed Checkpoint 01.

I am learning Linux, Git, networking, troubleshooting, English, and DevOps fundamentals from beginner level.

## Completed lessons

1. Basic Linux navigation
2. Git log and git diff
3. Git show and git log --stat
4. Linux file operations
5. Linux paths and hidden files
6. Linux system information
7. Linux processes and monitoring
8. Linux services with systemctl
9. Linux logs and troubleshooting with journalctl
10. Linux networking fundamentals

## Linux skills

I can:

- navigate between directories
- check my current directory
- work with absolute and relative paths
- create, copy, rename, move, and remove files
- show hidden files and directories
- check the Linux kernel version
- check CPU, RAM, and disk information
- start, find, and stop processes
- check running and failed services
- read system and service logs
- filter logs by service, boot, priority, and time
- check network interfaces and IP addresses
- test Internet connectivity and DNS
- check routes and listening ports

## Git skills

I can:

- check the repository status
- inspect unstaged and staged changes
- add files to staging
- create commits
- inspect commit history
- show commit statistics
- confirm that the working tree is clean

Important commands I practiced:

- `git status`
- `git diff`
- `git diff --staged`
- `git add`
- `git commit`
- `git log`
- `git log --stat`
- `git show`
- `git show --stat`

## Real troubleshooting experience

During Lesson 09, I found that the `fwupd` service was failing.

The root cause was a version mismatch:

- `fwupd` daemon: `1.9.31`
- `libfwupd2`: `1.9.34`

I checked the service status, read its logs, checked package versions, simulated the update, installed the correct version, and verified that the service was active and running.

This was my first real Linux troubleshooting workflow.

## Checkpoint 01

I completed a theory and practical checkpoint covering Lessons 01–10.

The practical tasks included:

- navigation and file operations
- absolute and relative paths
- system information
- processes
- services and logs
- networking
- Git workflow

I created and committed:

`Journal/Checkpoint_01.md`

## Strong areas

My strongest areas are:

- networking fundamentals
- Internet and DNS troubleshooting
- Linux services
- reading service logs
- basic Git workflow
- finding and stopping processes
- correcting my own mistakes in the terminal

## Topics to review

I need more practice with:

- absolute and relative paths
- exact command options
- older Git commands
- `uname -r` versus `lscpu`
- router IP versus computer IP versus interface name
- the full `journalctl` syntax
- remembering commands without looking at notes

## Learning approach

I do not want to memorize commands only.

I want to understand:

- what a command does
- why I use it
- how to read its output
- how to find and fix problems
- how different Linux concepts work together

## Next step

The next lesson is:

**Lesson 11 — DNS and HTTP connectivity tools**

Before new lessons, I will also answer a few short review questions from previous topics.

---

## 2026-08-04 — Linux Phase 1 completed

I completed Lessons 11–19 and passed Checkpoint 02.

Together with the previously completed Lessons 01–10 and Checkpoint 01, this completes my first major Linux foundation phase.

### Lessons 11–19 completed

11. DNS and HTTP connectivity tools
12. Bash scripting fundamentals
13. Bash loops and functions
14. Linux processes and job control
15. Linux users, groups, and permissions
16. APT package management
17. systemd and journal troubleshooting
18. Linux storage, filesystems, and mounts
19. Linux archives, compression, and backup verification

### Checkpoint 02

I completed practical tasks covering:

- DNS resolution and NXDOMAIN troubleshooting
- HTTP status codes and redirects
- curl exit codes and `--fail`
- Bash health-check scripts
- arrays and loops
- functions and return statuses
- counters and multi-URL health checking
- background processes and signals
- Linux permissions
- APT package investigation
- systemd service investigation
- journalctl logs
- disks, partitions, filesystems, and mount points
- `df`, `du`, `lsblk`, and `findmnt`
- tar.gz archives
- gzip integrity checks
- SHA-256 verification
- backup restoration
- recursive `diff` verification
- safe temporary-resource cleanup

### Current Linux assessment

My Linux foundation is strong enough to move to practical projects and later DevOps topics.

My main area for continued practice is Bash scripting.

I understand:

- variables
- quoting
- positional arguments
- conditions
- arrays
- loops
- functions
- return and exit codes
- counters

I still need more repetition when combining these concepts into complete scripts without examples.

### Current direction

The immediate practical priority is the FUZJA Cafe website/demo and sales presentation.

Bash practice will continue alongside project work.

Docker is planned for a later learning phase and will begin only when I explicitly decide to start it.

When Docker learning begins, I want to apply it to real projects where possible.

### Repository status

Checkpoint temporary resources were cleaned up safely.

The repository working tree was clean after the practical checkpoint.

---

## 2026-08-24 — Docker Lesson 01 completed

I installed Docker Engine from Docker's official APT repository and completed the first Docker lesson.

I practised:

- checking the Docker service
- running `hello-world`
- listing images and containers
- running Nginx in a container
- mapping host port `8080` to container port `80`
- verifying Nginx with `curl`, `ss`, and container logs
- stopping and removing containers
- using Docker without `sudo`

The next lesson is:

**Docker Lesson 02 — Images and Containers**

---

## 2026-08-26 — Docker Lesson 02 completed

I completed Docker Lesson 02 and practised:

- the difference between images and containers;
- pulling explicit image tags;
- creating, starting, restarting, stopping, renaming, and removing containers;
- using multiple containers from one image;
- understanding tags, image IDs, and image dependencies;
- diagnosing command arguments, logs, container state, and exit codes;
- cleaning up containers and images in dependency order.

The next lesson is:

**Docker Lesson 03 — Ports and Web Containers**

---

## 2026-08-27 — Docker Lesson 03 completed

I completed Docker Lesson 03 and practised:

- host and container ports;
- publishing ports with `-p` and `-P`;
- diagnosing host-port conflicts;
- all-interface and localhost-only bindings;
- the difference between `EXPOSE` metadata and published ports;
- verifying mappings and HTTP responses with `docker port`, `ss`, and `curl`;
- recreating containers to change port mappings.

The next lesson is:

**Docker Lesson 04 — Container Investigation**

---

## 2026-08-28 — Docker Lesson 04 completed

I completed Docker Lesson 04 and practised:

- reading and following container logs;
- using non-interactive and interactive `docker exec`;
- comparing a container's userspace and processes with the host using `docker top`;
- understanding PID namespaces and container-side versus host-side PIDs;
- extracting structured fields with `docker inspect --format`;
- monitoring resource usage with `docker stats`;
- diagnosing an intentionally broken Nginx container from its logs, state, and exit code;
- distinguishing commands that work with stopped containers from commands that require a running container;
- cleaning up and verifying the final Docker state.

The next lesson is:

**Docker Lesson 05 — Container Lifecycle**

---

## 2026-09-01 — Docker Lesson 05 completed

I completed Docker Lesson 05 and practised:

- creating, running, starting, stopping, restarting, removing, and force-removing containers;
- automatically removing temporary containers with `--rm`;
- understanding writable-layer persistence during stop, start, and restart;
- comparing removal and recreation with reuse of the same container;
- troubleshooting port syntax, curl exit codes, startup readiness, filters, and lifecycle errors.

The next lesson is:

**Docker Lesson 06 — Bind Mounts**

---

## 2026-09-04 — Docker Lesson 06 completed

I completed Docker Lesson 06 and practised:

- creating read-write and read-only bind mounts;
- changing shared files through host and container paths;
- understanding bind-mount persistence and container recreation;
- comparing missing-source behaviour with `--mount` and `-v`;
- troubleshooting startup readiness, hidden image files, ownership, permissions, and exit statuses.

The lesson started on 2026-09-02 and continued after a pause.

The next lesson is:

**Docker Lesson 07 — Docker Volumes**

---

## 2026-09-05 — Docker Lesson 07 completed

I completed Docker Lesson 07 — Named Volumes and practised:

- creating and inspecting named volumes and understanding initial image-file copying;
- preserving data after container removal and reusing it in a replacement container;
- sharing one volume between containers and observing immediate changes;
- using read-only attachments and checking failed writes;
- verifying protection against removing an in-use volume;
- automatically creating named volumes and reading data with a temporary container;
- explicitly cleaning up containers and volumes and verifying closed ports.

The next lesson is:

**Docker Lesson 08 — Environment Variables**

---

## 2026-09-06 — Docker Lesson 08 completed

I completed Docker Lesson 08 — Environment Variables and practised:

- exporting Bash variables and explicitly passing host or fixed values into containers;
- using environment files, command-line overrides, defaults, and required values;
- distinguishing host, container, and exec-process environments;
- configuring Nginx and recreating the same image with different runtime settings;
- troubleshooting missing variables, exit codes, and accidental command continuation;
- understanding environment-variable security and verifying cleanup.

The next topic after environment variables in `ROADMAP.md` is:

**Docker Lesson 09 — Docker Compose**

---

## 2026-09-10 — Roadmap refreshed

I refreshed the roadmap to keep the learning path practical and focused on junior DevOps skills.

- Docker Lessons 01–08 are complete, including bind mounts, named volumes, and environment variables.
- Docker Lesson 09 — Docker Compose is next.
- Python for DevOps is now the next major phase after the full Docker block and final comprehensive Docker checkpoint + practical Docker project.
- The later phases continue through CI/CD and GitHub Actions, Cloud / Azure, Terraform, Ansible, Kubernetes, monitoring and troubleshooting, and integrated DevOps projects.

---

## 2026-09-10 — Docker Lesson 09 — Docker Compose completed

I completed Docker Compose basics with one Nginx service and practised:

- describing the desired container configuration in `compose.yaml` using service `web` and image `nginx:alpine`;
- reading, validating, and resolving configuration with `docker compose config`, which does not inspect a running container;
- distinguishing container port `target: 80` from published host ports `8081`, `8082`, and `8083`;
- creating and starting the service in the background with `docker compose up -d`, which also created the default project network;
- verifying the service, image, `Up` status, and port mapping with `docker compose ps`;
- stopping and removing the container and default project network with `docker compose down`, then checking that `ps` was empty;
- changing the host port, checking the configuration, repeating the workflow, and later selecting all four commands independently.

The understanding check confirmed the purpose of the configuration file and each command, including host port `8083` versus container port `80` in `"8083:80"`.

The initial basic workflow was cleaned up successfully: `docker compose down` finished, `/tmp/docker-lesson09` was removed, and no lesson resources remained.

Later on the same day, I completed additional practice in `/tmp/docker-lesson09-logs`:

- viewing service-specific historical logs with `docker compose logs --tail 10 web`;
- adding Docker timestamps with `--timestamps`, alongside any application timestamps;
- following real-time output with `--follow --tail 0`, generating a request to `/live-test` from a second terminal, and immediately observing its missing-file error and HTTP `404`;
- understanding that `Ctrl+C` stops only the local log viewer and verifying that the service remained `Up`;
- running `pwd` and `nginx -v` through `docker compose exec web`, obtaining `/` and `nginx/1.31.4`, and verifying that the service remained running afterward;
- using the Compose service name rather than typing the generated container name;
- removing the temporary container and default network with `docker compose down`, then verifying that `docker compose ps -a` showed only headers and the filtered network listing was empty;
- removing the temporary directory and confirming its absence (exit status `0`), with no listener on port `8083` (listening check exit status `1`).

The demonstrated understanding now includes:

- Compose manages services as a project: `lesson09-logs` was the project name.
- `web` is the stable service name from `compose.yaml`; `lesson09-logs-web-1` is a generated container name that Compose resolves for the service.
- Logs can be viewed historically or followed live; stopping the viewer does not stop the service.
- `docker compose exec` runs an additional process inside an existing running service container without replacing or restarting its main process.
- `docker compose down` removes project containers and the default network.

All temporary resources from the additional practice were removed, the repository remained clean before documenting the work, and the local `nginx:alpine` image was intentionally retained.

Docker Lessons 01–09 are now completed, including Compose basics, logs, and `exec`. Multiple services are reserved for Lesson 10; deeper container networking and service discovery are reserved for Lesson 11.

### Next step

**Docker Lesson 10 — Multiple Services**

After Lessons 11–12, complete one comprehensive Docker checkpoint and one practical Docker project, then begin Python for DevOps.

---

## 2026-09-10 — Docker Lesson 10 — Multiple Services completed

I completed a two-service Compose project with Nginx (`web`) and Redis (`cache`) and practised:

- correcting YAML indentation errors and validating the resolved configuration;
- starting both services, checking published versus unpublished ports, and verifying HTTP `200 OK` and Redis `PONG`;
- stopping and starting one service by name while the other remained running;
- reading combined and service-specific logs, with `--tail` applied to each selected service;
- comparing desired configuration with runtime state and recreating only `web` to change host port `8080` to `8081`;
- distinguishing `start`, `restart`, `up -d`, `stop`, and `down`, including recovery after accidentally using `down` instead of `stop`;
- checking container state, a listening socket, and an application response separately;
- previewing Compose service-name DNS and distinguishing Redis `PING` from Linux ICMP `ping`.

Final cleanup was verified: both lesson containers, the default network, and `/tmp/docker-lesson10` were removed, with no listener on host port `8081`. The local `nginx:alpine` and `redis:7-alpine` images were intentionally retained and verified for Lesson 11. No repository files were created during the practical lab.

Docker Lessons 01–10 are now completed.

### Next step

**Docker Lesson 11 — Docker Networking and Service Discovery**

Lesson 12 remains Image Optimization and Multi-Stage Builds. After Lesson 12, complete one comprehensive Docker checkpoint and one practical Docker project, then begin Python for DevOps.

---

## 2026-09-11 — Docker Lesson 11 — Docker Networking and Service Discovery completed

I completed a three-service Compose lab on Ubuntu 24.04 in `/tmp/docker-lesson11` and practised:

- checking the default bridge network and reading full `docker network inspect` output, including subnet, gateway, container names, and IPv4 addresses;
- using stable Compose service names instead of runtime IP addresses and verifying ICMP, Nginx HTML, and Redis `PONG` responses;
- distinguishing published host port `8081` from container port `80`, and exposed Redis image metadata from a published port or running server;
- separating DNS resolution, TCP connectivity, and application protocols when investigating `bad address`, `Connection refused`, and a deliberate HTTP-to-Redis protocol mismatch;
- understanding the intentional Redis cross-protocol warning and confirming that the observed `vm.overcommit_memory` warning did not prevent Redis readiness;
- creating `frontend` and `backend` networks, inspecting membership, and testing communication and isolation in two topologies;
- applying the final topology with `client` on frontend, `web` on both networks, and `cache` on backend; only `client` and `web` were recreated;
- verifying that `client` could fetch Nginx but could not resolve `cache`, while `web` could resolve and ping `cache`;
- understanding that a container on two networks does not automatically route traffic between them;
- connecting network separation to least privilege, attack surface, and blast radius, while treating runtime secret handling as a separate responsibility;
- diagnosing an accidental trailing backslash and Bash's `>` continuation prompt.

Final cleanup was verified: all three containers, both custom networks, and `/tmp/docker-lesson11` were removed. Compose and filtered Docker listings returned only headers, the directory absence check returned `0`, and the port `8081` check returned no output with exit code `1`. The local `nginx:alpine` and `redis:7-alpine` images were intentionally retained.

Docker Lessons 01–11 are now completed. The Docker block remains in progress.

### Next step

**Docker Lesson 12 — Image Optimization and Multi-Stage Builds**

After Lesson 12, complete one comprehensive Docker checkpoint and one practical Docker project, then begin Python for DevOps.

---

## 2026-09-11 — Docker Lesson 12 — Image Optimization and Multi-Stage Builds completed

I completed a Go HTTP application lab in `/tmp/docker-lesson12` and practised:

- separating source code, dependencies, compiler, compiled binary, and runtime image roles; the image build compiled `/app`, while running a container started it without recompiling;
- comparing `lesson12:single` using `golang:1.26-alpine` with `lesson12:multi` using a Go builder and `alpine:3.22` runtime;
- copying only `/app` into the runtime stage, reducing disk usage from `489 MB` to `25.8 MB` (approximately `95%`) and compressed content size from `97.3 MB` to `8.44 MB`;
- verifying the same HTTP response through host ports `8082` and `8083`, both mapped to container port `8080`, and confirming that Go was absent from the final multi-stage image;
- reading image history to distinguish large toolchain/build-cache layers from the final Alpine and binary layers, and recognising `CMD` and `EXPOSE` as `0 B` configuration metadata;
- comparing the first single-stage build (`19.7s`), an identical cached multi-stage rebuild (`2.7s`), and a source-change rebuild (`8.6s`, including `6.3s` for compilation);
- verifying the changed HTTP response and understanding that a cache miss affects the changed step and dependent later steps, while earlier steps can remain cached;
- discussing dependency-first ordering with `go.mod` and `go.sum` conceptually, without adding module files or external dependencies to this lab;
- testing `COPY . .` with an unnecessary `20 MB` file: context grew to approximately `20.98 MB`, compilation reran, but the final image stayed `25.8 MB` because only the binary crossed stages;
- excluding `unnecessary.bin` with `.dockerignore`, reducing context to approximately `194 B` / `172 B`, and verifying cached builds in `2.1s` and then `1.7s` even after the ignored file grew to `30 MB`;
- distinguishing Docker build context from final-image contents and `.dockerignore` from `.gitignore`; neither removes a secret already tracked in Git history;
- understanding that smaller runtime images improve transfer/deployment efficiency and reduce unnecessary attack surface without automatically reducing application RAM, CPU, or HTTP response time.

Final cleanup was verified: all lesson containers and the four `lesson12` image tags were removed, `docker image ls lesson12` returned no lesson images, and `/tmp/docker-lesson12` was absent (exit code `0`). Ports `8082` and `8083` had no listeners (grep exit code `1`). `docker system df` showed `3` unused images (`152.1 MB`), `0` containers, `6` unused local volumes (`356 B`), and `21` build-cache entries (`879.4 MB` reclaimable). No global prune was run because it could affect unrelated projects.

Docker Lessons 01–12 and the Docker lesson block are now complete.

### Next step

**Comprehensive Docker checkpoint**

Complete the checkpoint first, then one practical Docker project, then begin Python for DevOps. The checkpoint and practical project are not complete yet.
