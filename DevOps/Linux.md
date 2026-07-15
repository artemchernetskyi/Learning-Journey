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
---

## Lesson 07 — Linux processes and system monitoring

Today I learned how to check running processes in Linux.

### Process

A process is a running program.

Examples:

- terminal
- browser
- VS Code
- system service

### ps

`ps` shows processes connected to the current terminal.

### ps aux

`ps aux` shows all running processes.

Important columns:

- USER — who started the process
- PID — process ID
- %CPU — CPU usage
- %MEM — memory usage
- COMMAND — command or program name

### top

`top` shows live system activity.

To exit `top`, press `q`.

### pgrep

`pgrep` finds a process by name.

Example:

`pgrep -a bash`

### kill

`kill` stops a process by PID.

Safe practice:

`sleep 300 &`

Then find it:

`pgrep -a sleep`

Then stop it:

`kill PID`

Important: I should not kill random system processes.

### New vocabulary

- process — процес
- running program — запущена програма
- PID / process ID — номер процесу
- CPU usage — використання процесора
- memory usage — використання памʼяті
- live system activity — активність системи в реальному часі
- background process — процес у фоні
- stop a process — зупинити процес

### My sentence

I learned how to find and stop a process safely in Linux.
---

## Lesson 08 — Linux services with systemctl

Today I learned how to check Linux services.

### Service

A service is a background program.

Examples:

- network service
- Bluetooth service
- printing service
- update service

### systemctl status

`systemctl status` shows general system and service status.

To exit, press `q`.

### Running services

`systemctl list-units --type=service --state=running`

This command shows running services.

### NetworkManager

`systemctl status NetworkManager`

This command shows the network service status.

### Failed services

`systemctl --failed`

This command shows failed services.

### Important vocabulary

- service — сервіс / фонова програма
- background program — програма у фоні
- running — працює
- active — активний
- inactive — неактивний
- failed — помилка
- enabled — запускається автоматично
- disabled — не запускається автоматично
- status — стан

### My sentence

I learned how to check Linux services with systemctl.
## Lesson 09 — Linux logs with journalctl

Today I learned how to check Linux logs and troubleshoot service problems.

### Linux logs

Linux logs contain information about system events.

Logs can show:

- service activity
- warnings
- errors
- system startup events
- hardware messages

### Recent logs

`journalctl -n 15 --no-pager`

This command shows the last 15 log entries.

`--no-pager` shows the result directly in the terminal.

### Current boot logs

`journalctl -b -n 20 --no-pager`

This command shows logs from the current system boot.

`-b` means current boot.

### Warnings and errors

`journalctl -b -p warning --no-pager`

This command shows warnings and more serious messages from the current boot.

`journalctl -b -p err --no-pager`

This command shows only errors and more serious messages.

### Service logs

`journalctl -b -u fwupd --no-pager`

This command shows logs for the `fwupd` service.

`-u` means systemd unit.

### Service status

`systemctl status fwupd --no-pager`

This command shows the current status of the `fwupd` service.

### Logs from a specific time

`journalctl -u fwupd --since "10 minutes ago" --no-pager`

This command shows `fwupd` logs from the last 10 minutes.

### Troubleshooting example

The `fwupd` service failed because two package versions did not match.

The installed versions were:

- `fwupd` — version `1.9.31`
- `libfwupd2` — version `1.9.34`

The log message showed:

`libfwupd version 1.9.34 does not match daemon 1.9.31`

I checked the installed package versions with:

`dpkg -l | grep -E 'fwupd|libfwupd'`

I checked available package versions with:

`apt policy fwupd libfwupd2`

I simulated the update before changing the system:

`apt install --simulate fwupd`

Then I updated the package:

`sudo apt install fwupd`

After the update, the `fwupd` service became active and started successfully.

### Important lesson

Old errors stay in the journal after a problem is fixed.

To confirm that a problem is resolved, I should check:

- the latest log entries
- the service status
- new logs after the fix

### Important vocabulary

- log — журнал подій
- log entry — запис у журналі
- warning — попередження
- error — помилка
- current boot — поточний запуск системи
- service logs — логи сервісу
- troubleshooting — пошук і усунення проблем
- root cause — першопричина
- version mismatch — невідповідність версій
- failed — завершився з помилкою
- active — активний
- running — працює
- successful — успішний
- package — пакет

### My sentence

I learned how to use journalctl to find and resolve a real Linux service problem.
## Lesson 10 — Linux networking fundamentals

Today I learned how to check Linux network interfaces, connectivity, DNS, routes, and listening ports.

### IP address

An IP address identifies a computer inside a network.

My local IP address was:

`192.168.0.193`

An IP address can change when the computer reconnects to the network.

### MAC address

A MAC address is a hardware identifier of a network adapter.

A MAC address normally stays the same.

### Check the IP address

`hostname -I`

This command shows the computer's IP addresses.

### Network interfaces

`ip addr`

This command shows network interfaces and their IP addresses.

`ip link`

This command shows network interfaces and their current state.

### Loopback interface

The `lo` interface is the loopback interface.

Its IPv4 address is:

`127.0.0.1`

It always points to the same computer.

Network traffic sent to `127.0.0.1` does not leave the computer.

### Ethernet interface

My Ethernet interface is:

`enp8s0`

It showed:

- `NO-CARRIER`
- `state DOWN`

This means Linux can see the Ethernet adapter, but no network cable is connected.

### Wi-Fi interface

My Wi-Fi interface is:

`wlp7s0`

It showed:

- `UP`
- `LOWER_UP`
- `state UP`

This means the Wi-Fi interface is enabled and connected.

### Test Internet connectivity

`ping -c 4 8.8.8.8`

This command tests whether the computer can reach another IP address on the Internet.

`-c 4` means send four packets.

### Test DNS

`ping -c 4 google.com`

This command checks Internet connectivity and DNS resolution.

If `ping 8.8.8.8` works but `ping google.com` fails, the most likely problem is DNS resolution.

### Packet loss

The ping result showed:

`0% packet loss`

This means all packets were received successfully.

### Ports

A port identifies a service or application on a computer.

Examples:

- port `22` — SSH
- port `53` — DNS
- port `80` — HTTP
- port `443` — HTTPS
- port `631` — printing service

### Listening TCP ports

`ss -lnt`

This command shows listening TCP ports.

Options:

- `-l` — listening sockets
- `-n` — numeric addresses and ports
- `-t` — TCP sockets

### Show listening processes

`sudo ss -lntp`

This command shows listening TCP ports and the processes that use them.

`-p` means process.

### UDP sockets

`sudo ss -lnup`

This command shows UDP sockets and their processes.

`-u` means UDP.

### Local and external listening addresses

`127.0.0.1:631`

This means the service is available only on the local computer.

`0.0.0.0:631`

This means the service is listening on all IPv4 network interfaces.

A firewall can still block external connections.

### DNS service

The `systemd-resolved` process was listening on port `53`.

It helps the system resolve domain names into IP addresses.

### Printing service

The `cupsd` process was listening on:

`127.0.0.1:631`

This means the printing service was available only locally.

### Default route

`ip route`

This command shows the routing table.

My default route was:

`default via 192.168.0.1 dev wlp7s0`

This means Internet traffic goes through the router `192.168.0.1` using the Wi-Fi interface `wlp7s0`.

### DNS configuration

`resolvectl status`

This command shows the current DNS configuration.

My current DNS server was:

`192.168.0.1`

This means my router handles DNS requests.

### Basic network troubleshooting workflow

1. Check the IP address with `hostname -I`.
2. Check interfaces with `ip addr` and `ip link`.
3. Check the default route with `ip route`.
4. Test Internet connectivity with `ping 8.8.8.8`.
5. Test DNS with `ping google.com`.
6. Check DNS configuration with `resolvectl status`.
7. Check listening ports with `sudo ss -lntp`.

### Important vocabulary

- network — мережа
- interface — мережевий інтерфейс
- IP address — IP-адреса
- MAC address — MAC-адреса
- loopback — зворотний локальний інтерфейс
- localhost — цей самий комп’ютер
- packet — пакет
- packet loss — втрата пакетів
- port — порт
- socket — мережевий сокет
- listening — очікує з’єднання
- route — маршрут
- default route — маршрут за замовчуванням
- router — роутер
- DNS resolution — перетворення доменного імені в IP-адресу
- connectivity — мережеве з’єднання
- TCP — протокол зі встановленням з’єднання
- UDP — протокол без постійного з’єднання

### My sentence

I learned how to check network interfaces, Internet connectivity, DNS, routes, and listening ports in Linux.
## Lesson 11 — DNS and HTTP connectivity tools

Today I learned how to inspect DNS records, test HTTP connectivity, follow redirects, download files, check command exit codes, and create a basic website health-check script.

### HTTP request and response

A client sends an HTTP request to a server.

The server processes the request and sends an HTTP response.

The response contains:

- an HTTP status code
- response headers
- an optional response body

### Display a webpage

`curl https://example.com`

This command sends an HTTP request and displays the response body in the terminal.

For a website, the response body is usually HTML.

### Display HTTP response headers

`curl -I https://example.com`

This command displays the HTTP response headers without displaying the page body.

The `-I` option normally sends a `HEAD` request.

### Verbose curl output

`curl -v https://example.com`

This command displays detailed information about the connection.

It can show:

- DNS resolution
- the selected IP address
- TCP connection details
- TLS connection details
- the HTTP request
- the HTTP response headers

Verbose mode is useful for troubleshooting connectivity problems.

### HTTP status code 200

The request to `https://example.com` returned:

`HTTP/2 200`

The `200 OK` status means the requested resource was found and returned successfully.

### HTTP status code 404

The request to:

`https://example.com/not-existing-page`

returned:

`HTTP/2 404`

The `404 Not Found` status means the server is available, but the requested page or resource does not exist.

A `404` response means:

- DNS resolution worked
- the server was reached
- the TLS connection worked
- the HTTP request was received
- the requested resource was not found

### Important HTTP headers

The response from `example.com` contained headers such as:

`content-type: text/html`

This means the response body contains HTML.

`content-length: 2108`

The `Content-Length` header shows the response-body size in bytes.

`server: cloudflare`

The `Server` header can identify the web server, proxy, or CDN that handled the request.

`last-modified: Wed, 01 Jul 2026 17:50:18 GMT`

The `Last-Modified` header shows when the resource was last changed.

`allow: GET, HEAD`

The `Allow` header shows which HTTP methods are supported by the resource.

`accept-ranges: bytes`

This means the server supports requests for selected parts of the resource.

### Cache headers

The response contained:

`cf-cache-status: HIT`

`HIT` means Cloudflare already had a cached copy of the resource and returned it from its cache.

The response also contained an `Age` header.

For example:

`Age: 2431`

The `Age` value is measured in seconds.

It shows how long the response has been stored in a proxy or CDN cache.

It does not show the file size.

### HTTP redirects

`curl -I http://github.com`

This command returned:

`HTTP/1.1 301 Moved Permanently`

It also returned:

`Location: https://github.com/`

The `301 Moved Permanently` status means the resource has permanently moved to another URL.

The `Location` header tells the client where the resource is now located.

### Follow redirects

`curl -IL http://github.com`

Options:

- `-I` — display response headers
- `-L` — follow redirects

The request produced two HTTP status lines:

`HTTP/1.1 301 Moved Permanently`

and then:

`HTTP/2 200`

This means curl followed one redirect from HTTP to HTTPS and successfully reached the final page.

### Service unavailable

A request to `httpbin.org` returned:

`HTTP/2 503`

The `503 Service Unavailable` status means the server or application is temporarily unable to handle the request.

This does not necessarily mean there is a problem with the local computer or Internet connection.

### Compact curl report

`curl -sIL -o /dev/null -w '...' http://github.com`

Important options:

- `-s` — silent mode
- `-I` — request headers only
- `-L` — follow redirects
- `-o /dev/null` — discard the normal response output
- `-w` — display selected information after the request

The compact report showed:

- final HTTP status
- final URL
- number of redirects
- remote IP address
- total request time

My result included:

`Final status: 200`

`Final URL: https://github.com/`

`Redirects: 1`

`Remote IP: 140.82.121.3`

### Silent mode with errors

`curl -sS`

Options:

- `-s` — hide progress and normal diagnostic output
- `-S` — still display errors

The combination `-sS` is useful in scripts because it hides unnecessary progress information but still shows failures.

### Discard the response body

`curl -o /dev/null https://example.com`

The `-o` option selects the output destination.

`/dev/null` is a special Linux device that discards everything written to it.

This is useful when only the response status or timing information is needed.

### Measure request timing

Curl can measure different connection stages with `-w`.

Important variables include:

- `%{time_namelookup}` — time until DNS resolution completed
- `%{time_connect}` — time until the TCP connection was established
- `%{time_appconnect}` — time until the TLS connection was ready
- `%{time_starttransfer}` — time until the first response byte arrived
- `%{time_total}` — total request duration
- `%{http_code}` — final HTTP status code

These timing values are cumulative.

Each value shows the time from the beginning of the request, not the separate duration of only that stage.

### Time to First Byte

`time_starttransfer` shows the time until the first byte was received.

This is often called:

`TTFB — Time to First Byte`

A high TTFB can indicate a slow server, application, database, proxy, or network path.

### Reusable curl format file

I created:

`DevOps/curl-format.txt`

It stores the long curl output format.

The file can be used with:

`curl -sS -o /dev/null -w '@DevOps/curl-format.txt' https://github.com`

This is easier than remembering and typing every curl timing variable manually.

### Download a file with wget

`wget https://example.com -O /tmp/example.html`

This command downloaded the webpage and saved it as:

`/tmp/example.html`

Options:

- `wget` — download a resource
- `-O` — choose the output filename
- `/tmp/example.html` — output file path

The response returned:

`200 OK`

The downloaded file size was:

`559 bytes`

### Inspect a downloaded file

`ls -lh /tmp/example.html`

This command displayed the file size and file information.

`head -n 5 /tmp/example.html`

This command displayed the first five lines of the file.

The HTML was mostly stored on one physical line, so `head` displayed almost the entire document.

### Check a resource without downloading it

`wget --spider https://example.com`

The `--spider` option checks whether a remote resource exists without saving it.

The existing page returned:

`200 OK`

The missing page returned:

`404 Not Found`

### Display response headers with wget

`wget -S --spider https://example.com/not-existing-page`

Options:

- `-S` — display server response headers
- `--spider` — check the resource without downloading it

This command is useful for checking a URL and inspecting its HTTP response.

### Detailed DNS lookup

`dig example.com`

This command performs a detailed DNS lookup.

The output contains sections such as:

- header
- question section
- answer section
- DNS server
- query time

The DNS status was:

`NOERROR`

This means the DNS query completed successfully.

### DNS A records

An `A` record maps a domain name to an IPv4 address.

The query returned two IPv4 addresses:

- `104.20.23.154`
- `172.66.147.243`

### DNS AAAA records

An `AAAA` record maps a domain name to an IPv6 address.

`dig +short AAAA example.com`

The query returned two IPv6 addresses.

### Compact DNS output

`dig +short example.com`

This command displays only the DNS answer values.

It is useful in shell scripts because it does not display the full diagnostic output.

The full `dig` command is better for detailed troubleshooting.

`dig +short` is better when only the returned IP addresses are needed.

### DNS TTL

The `dig` output showed a TTL value.

TTL means:

`Time To Live`

It tells a DNS resolver how long it may cache a DNS record before requesting it again.

The TTL value is measured in seconds.

### Local DNS resolver

The DNS server shown by `dig` and `nslookup` was:

`127.0.0.53#53`

This means:

- `127.0.0.53` — Ubuntu's local DNS stub resolver
- `53` — the standard DNS port

The local resolver is normally managed by `systemd-resolved`.

It receives DNS requests from local applications and forwards them to configured DNS servers.

### Simple DNS lookup

`nslookup example.com`

This command performs a simple DNS lookup.

It showed:

- the DNS server
- the domain name
- IPv4 addresses
- IPv6 addresses

`nslookup` is easier to read for a quick manual check.

`dig` provides more detailed information for DNS troubleshooting.

### Non-authoritative answer

The `nslookup` output showed:

`Non-authoritative answer`

This means the response came from a recursive DNS resolver or its cache, not directly from the authoritative DNS server for the domain.

This is normal for everyday DNS queries.

### Query a specific DNS record

`nslookup -type=AAAA example.com`

The `-type=AAAA` option requests only IPv6 records.

### Nonexistent domain

I tested:

`this-domain-should-not-exist-987654321.com`

The `dig` command returned:

`NXDOMAIN`

NXDOMAIN means:

`Non-Existent Domain`

It means DNS could not find the requested domain name.

### Curl DNS error

The curl request to the nonexistent domain returned:

`curl: (6) Could not resolve host`

Curl exit code `6` means the hostname could not be resolved into an IP address.

Because DNS failed:

- no IP address was found
- no TCP connection was created
- no TLS connection was created
- no HTTP request reached a web server

### NXDOMAIN and HTTP 404

`NXDOMAIN` and `404 Not Found` describe different failures.

`NXDOMAIN` means the domain name does not exist in DNS.

The connection cannot begin because no IP address is available.

`404 Not Found` means DNS worked and the server was reached, but the requested page or resource does not exist.

### Command exit codes

`echo $?`

This command displays the exit code of the most recently completed command.

An exit code of:

`0`

normally means the command succeeded.

A non-zero exit code normally means the command failed.

### Curl exit code 0

A successful request to `https://example.com` returned:

`0`

Without the `--fail` option, a request that receives HTTP `404` can also return exit code `0`.

This happens because curl successfully connected to the server and received a valid HTTP response.

### Curl exit code 6

A DNS resolution failure returned:

`6`

This means curl could not resolve the hostname.

### Curl exit code 22

`curl --fail -I https://example.com/not-existing-page`

The `--fail` option makes curl treat HTTP `4xx` and `5xx` responses as command failures.

The missing page returned:

`curl: (22) The requested URL returned error: 404`

Curl exit code `22` means an HTTP error was received while using `--fail`.

### Basic shell condition

A Bash `if` statement can check a command's exit code.

Example:

`if curl -fsS -o /dev/null URL; then`

If curl returns exit code `0`, Bash executes the `then` branch.

If curl returns a non-zero exit code, Bash executes the `else` branch.

The tests produced:

- available page — `then`
- missing page — `else`
- nonexistent domain — `else`

### Curl health-check options

The health check used:

`curl -fsS -o /dev/null`

Options:

- `-f` — fail on HTTP `4xx` and `5xx` responses
- `-s` — hide normal progress output
- `-S` — show errors
- `-o /dev/null` — discard the response body

### Health-check script

I created:

`DevOps/Scripts/check-url.sh`

The script checks whether a URL is available.

It can be run with:

`./DevOps/Scripts/check-url.sh`

Without an argument, it checks:

`https://example.com`

A custom URL can be passed as the first argument:

`./DevOps/Scripts/check-url.sh https://github.com`

### Script interpreter

The script begins with:

`#!/usr/bin/env bash`

This is the shebang.

It tells Linux to execute the script using Bash.

### Script argument and default value

The script contains:

`url="${1:-https://example.com}"`

`$1` is the first argument passed to the script.

If no first argument is provided, the script uses `https://example.com` as the default value.

### Save an exit code

The script contains:

`status=$?`

`$?` stores the exit code of the previous command.

The value is saved immediately because the next command would replace it.

### Return the curl exit code

The script contains:

`exit "$status"`

This makes the script return the same failure exit code as curl.

This is useful for:

- monitoring
- CI/CD pipelines
- cron jobs
- other shell scripts
- automated health checks

### Make the script executable

`chmod +x DevOps/Scripts/check-url.sh`

This command added execute permission to the script.

The file permissions showed:

`-rwx------`

The `x` means the file can be executed.

### Health-check results

The available page returned:

- `Website check: OK`
- exit code `0`

The missing page returned:

- `Website check: FAILED`
- curl exit code `22`

The nonexistent domain returned:

- `Website check: FAILED`
- curl exit code `6`

### Basic DNS and HTTP troubleshooting workflow

1. Check DNS records with `dig DOMAIN`.
2. Use `dig +short DOMAIN` for a compact IP address result.
3. Use `nslookup DOMAIN` for a simple DNS check.
4. Check response headers with `curl -I URL`.
5. Use `curl -v URL` for detailed connection information.
6. Use `curl -L URL` when redirects must be followed.
7. Check the HTTP status and timing with `curl -w`.
8. Use `wget --spider URL` to test a resource without downloading it.
9. Check the previous command's exit code with `echo $?`.
10. Use `curl --fail` when HTTP `4xx` and `5xx` responses must count as command failures.

### Important vocabulary

- request — запит
- response — відповідь
- response body — тіло відповіді
- response header — заголовок відповіді
- status code — код стану
- redirect — перенаправлення
- permanent redirect — постійне перенаправлення
- resource — ресурс
- content type — тип вмісту
- content length — розмір вмісту
- cache — кеш
- cached copy — кешована копія
- DNS record — DNS-запис
- A record — запис IPv4-адреси
- AAAA record — запис IPv6-адреси
- resolver — DNS-резолвер
- authoritative server — авторитетний DNS-сервер
- hostname — ім’я хоста
- resolve — перетворити доменне ім’я в IP-адресу
- NXDOMAIN — домен не існує
- exit code — код завершення
- success — успішне виконання
- failure — невдале виконання
- health check — перевірка працездатності
- script argument — аргумент скрипта
- default value — значення за замовчуванням
- shebang — рядок, який визначає інтерпретатор скрипта
- troubleshooting — пошук і усунення несправностей

### My sentence

I learned how to inspect DNS records, check HTTP responses, follow redirects, identify DNS and HTTP failures, use command exit codes, and create a basic website health-check script.