# Linux Notes — Artem

## Purpose

This file contains my Linux notes.

The goal is to learn Linux step by step and explain basic Linux concepts in simple English.

Linux is one of the most important foundations for DevOps.

---

## Current Linux status

Current progress:

- Ubuntu is installed.
- Internet connection is working.
- Git is installed.
- Visual Studio Code is installed.
- The Learning Journey project folder is created.
- The project was opened in VS Code.
- Git repository was initialized.

Project path:

/home/artem/Projects/Learning-Journey

---

## Why Linux is important for DevOps

Linux is important because many servers run on Linux.

DevOps engineers often work with:

- servers
- files
- logs
- permissions
- services
- networking
- scripts
- containers
- deployments

To understand DevOps, I need to understand Linux basics first.

---

## Basic terminal idea

The terminal is a tool where I can control the system using commands.

In DevOps, the terminal is very important because many tasks are done from the command line.

English explanation:

The terminal allows me to work with the operating system using text commands.

---

## Commands I already used

### pwd

Command:

pwd

Meaning:

Print working directory.

Simple English explanation:

It shows the current directory.

Example:

/home/artem/Projects/Learning-Journey

---

### cd

Command:

cd ~/Projects/Learning-Journey

Meaning:

Change directory.

Simple English explanation:

It moves me into another folder.

Example:

cd ~/Projects/Learning-Journey

This command moves me to my Learning Journey project folder.

---

### ls

Command:

ls

Meaning:

List files and folders.

Simple English explanation:

It shows files and folders in the current directory.

---

### mkdir

Command:

mkdir

Meaning:

Make directory.

Simple English explanation:

It creates a new folder.

Example:

mkdir Projects

This command creates a folder called Projects.

---

### mkdir -p

Command:

mkdir -p ~/Projects/Learning-Journey

Meaning:

Create folders, including parent folders if they do not exist.

Simple English explanation:

It creates the full folder path if it does not already exist.

---

### touch

Command:

touch README.md

Meaning:

Create an empty file.

Simple English explanation:

It creates a new empty file.

Example:

touch README.md

This command creates an empty README.md file.

---

### cat

Command:

cat README.md

Meaning:

Show file content.

Simple English explanation:

It prints the content of a file in the terminal.

---

### find

Command:

find . -maxdepth 3 -type f

Meaning:

Find files.

Simple English explanation:

It shows files inside the current directory and subdirectories.

---

## Git commands used on Linux

### git --version

Command:

git --version

Simple English explanation:

It shows the installed Git version.

---

### git init

Command:

git init

Simple English explanation:

It initializes a new Git repository.

This means Git starts tracking the project.

---

### git status

Command:

git status

Simple English explanation:

It shows the current state of the Git repository.

It tells me which files are changed, staged, or untracked.

---

### git add

Command:

git add .

Simple English explanation:

It adds changed files to the staging area.

The staging area is a preparation area before a commit.

---

### git commit

Command:

git commit -m "Commit message"

Simple English explanation:

It saves a snapshot of my project in Git history.

Example:

git commit -m "Initial learning journey setup"

---

## Important words

- directory — папка / директорія
- file — файл
- command — команда
- terminal — термінал
- repository — репозиторій
- current directory — поточна папка
- hidden files — приховані файли
- install — встановити
- update — оновити
- configure — налаштувати
- set up — налаштувати
- troubleshoot — шукати і вирішувати проблему

---

## My first technical English sentences

I installed Git on Ubuntu.

I installed Visual Studio Code on Ubuntu.

I created my Learning Journey project folder.

I opened the project folder in VS Code.

I initialized a Git repository.

I created my first Markdown files.

I made my first Git commit.

I am learning Linux step by step.

---

## Next Linux topics

Next topics to learn:

- file system basics
- absolute and relative paths
- hidden files
- ls -la
- permissions
- users
- sudo
- apt
- system updates
- processes
- logs
- services
- networking basics
- SSH basics

---

## Personal rule

Do not rush.

Linux is a foundation.

I need to understand the basics before Docker, Kubernetes, Terraform, and cloud.
