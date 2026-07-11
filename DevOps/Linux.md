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
---

## Lesson 01 — Basic Linux navigation

Today I practiced basic Linux commands.

### Commands

pwd

It shows the current directory.

ls

It shows files and folders in the current directory.

ls -la

It shows all files, including hidden files.

git status

It shows the current state of the Git repository.

### New vocabulary

- current directory — поточна папка
- hidden files — приховані файли
- repository — репозиторій
- working tree clean — робоча папка чиста
- command — команда

### My sentence

I practiced basic Linux commands and updated my Linux notes.
---

## Lesson 02 — Git log and git diff

Today I learned two Git commands.

### git log --oneline

It shows the commit history in a short format.

### git diff

It shows changes that are not committed yet.

### New vocabulary

- commit history — історія комітів
- short format — короткий формат
- difference — різниця
- uncommitted changes — незакомічені зміни

### My sentence

I learned how to check commit history and see file changes.
---

## Lesson 03 — Git show and git log stat

Today I learned how to check commit details.

### git show --stat

It shows details of the latest commit.

It shows:

- commit message
- changed files
- insertions
- deletions

### git show

It shows the full changes from the latest commit.

### git log --stat

It shows commit history with changed files.

### New vocabulary

- latest commit — останній коміт
- commit hash — унікальний код коміта
- details — деталі
- insertions — додані рядки
- deletions — видалені рядки
- changed files — змінені файли

### My sentence

I learned how to check commit details and file statistics.
---

## Lesson 04 — Linux file operations

Today I practiced basic Linux file operations.

### mkdir

It creates a directory.

### touch

It creates an empty file.

### cp

It copies a file.

### mv

It moves or renames a file.

### rm

It removes a file.

### rm -r

It removes a directory with files inside.

Important: I should be careful with rm and rm -r.

### New vocabulary

- create — створити
- copy — копіювати
- move — перемістити
- rename — перейменувати
- remove — видалити
- empty file — порожній файл
- directory — папка / директорія

### My sentence

I practiced creating, copying, renaming, and removing files in Linux.
---

## Lesson 05 — Linux paths and hidden files

Today I learned about Linux paths and hidden files.

### Absolute path

An absolute path starts from the root directory.

Example:

/home/artem/Projects/Learning-Journey

### Relative path

A relative path starts from the current directory.

Example:

DevOps/Linux.md

### Special symbols

. means current directory.

.. means parent directory.

~ means home directory.

### Hidden files

Hidden files and folders start with a dot.

Example:

.git

### ls -la

It shows all files, including hidden files.

### New vocabulary

- absolute path — абсолютний шлях
- relative path — відносний шлях
- root directory — головна директорія
- current directory — поточна папка
- parent directory — папка вище
- hidden file — прихований файл
- hidden folder — прихована папка

### My sentence

I learned how to use absolute paths, relative paths, and hidden files in Linux.
---

## Lesson 06 — Linux system information

Today I learned how to check basic Linux system information.

### uname

`uname -a` shows information about the Linux kernel and system.

`uname -r` shows only the kernel version.

### hostnamectl

`hostnamectl` shows basic information about the operating system.

It can show:

- hostname
- operating system
- kernel
- architecture

### lscpu

`lscpu` shows information about the CPU.

### free -h

`free -h` shows RAM usage in a human-readable format.

### df -h

`df -h` shows disk space usage in a human-readable format.

### uptime

`uptime` shows how long the system has been running.

### New vocabulary

- kernel — ядро системи
- operating system — операційна система
- CPU — процесор
- memory / RAM — оперативна памʼять
- disk space — місце на диску
- used — використано
- available — доступно
- human-readable — зручно для людини
- uptime — час роботи системи
- load average — середнє навантаження

### My sentence

I learned how to check Linux system information from the terminal.
