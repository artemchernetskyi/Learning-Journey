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