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
## Lesson 12 — Bash scripting fundamentals

Today I learned how Bash scripts use variables, arguments, conditions, command output, file checks, logical operators, and exit codes.

I also improved my website health-check script so that it displays the HTTP status and response time.

### Bash script

A Bash script is a text file containing commands that Bash executes in order.

Bash scripts normally use the `.sh` filename extension.

My script is:

`DevOps/Scripts/check-url.sh`

### Shebang

The script begins with:

`#!/usr/bin/env bash`

This line is called the shebang.

It tells Linux to execute the script using Bash.

`/usr/bin/env` searches for Bash using the current `PATH`.

### Bash location

`which bash`

This command shows the location of Bash.

My result was:

`/usr/bin/bash`

### Run a script with Bash

`bash DevOps/Scripts/check-url.sh`

This command explicitly starts Bash and gives the script file to it.

The script does not need executable permission when it is started this way.

### Run a script directly

`./DevOps/Scripts/check-url.sh`

This command asks Linux to execute the file directly.

For this method, the script needs:

- executable permission
- a valid shebang

### Executable permission

`chmod +x DevOps/Scripts/check-url.sh`

This command adds executable permission to the script.

`+x` means add execute permission.

`-x` would remove execute permission.

### Variables

A variable stores a value under a name.

Example:

`name="Artem"`

The variable name is:

`name`

The stored value is:

`Artem`

### Variable assignment

A correct variable assignment has no spaces around `=`:

`project="Learning Journey"`

This is incorrect:

`project = "Learning Journey"`

With spaces, Bash interprets `project` as a command instead of a variable assignment.

The result was:

`Command 'project' not found`

### Read a variable

`echo "$project"`

The `$` tells Bash to read or expand the value stored in the variable.

Without `$`, Bash prints the variable name as normal text.

### Quote variables

Variables should normally be placed inside double quotes:

`"$project"`

Quotes preserve the complete value as one argument.

Without quotes, Bash can split a value at spaces.

For example:

`Learning Journey`

could be interpreted as two separate arguments:

- `Learning`
- `Journey`

With quotes, it remains one argument.

### Curly braces around variables

Curly braces can clearly separate a variable name from surrounding text.

Example:

`echo "${project}.md"`

The result was:

`Learning Journey.md`

### Script arguments

Arguments are values provided when starting a script.

Example:

`bash /tmp/arguments.sh Artem DevOps`

The script received:

- first argument — `Artem`
- second argument — `DevOps`

### Special argument variables

Bash provides special variables for script arguments:

- `$0` — script name or path
- `$1` — first argument
- `$2` — second argument
- `$#` — number of arguments
- `$@` — all arguments

My script name appeared as:

`/tmp/arguments.sh`

### Script name and argument count

The script name in `$0` is not included in `$#`.

For:

`bash /tmp/arguments.sh Artem DevOps`

the number of arguments was:

`2`

### Arguments containing spaces

`bash /tmp/arguments.sh "Learning Journey" 12`

The quotes keep `Learning Journey` together as one argument.

Without quotes, Bash would treat it as two arguments.

With quotes, the result was:

- `$1` — `Learning Journey`
- `$2` — `12`
- `$#` — `2`

### Default values

Bash can use a default value when an argument or variable is missing.

Example:

`name="${1:-Guest}"`

This means:

- use `$1` when it contains a value
- use `Guest` when `$1` is missing or empty

Without an argument, the result was:

`Hello, Guest!`

With `Artem` as an argument, the result was:

`Hello, Artem!`

### Empty argument

`bash /tmp/default-value.sh ""`

The empty quotes pass one argument, but its value is an empty string.

The expression:

`${1:-Guest}`

uses the default value when the first argument is missing or empty.

Therefore, the result was:

`Hello, Guest!`

### Default URL

My health-check script uses:

`url="${1:-https://example.com}"`

Without an argument, it checks:

`https://example.com`

When a custom URL is provided, it checks that URL instead.

### Read keyboard input

`read` allows a Bash script to receive input from the keyboard.

Example:

`read -r -p "Enter your name: " name`

Options:

- `read` — read user input
- `-r` — treat backslashes as normal characters
- `-p` — display a prompt
- `name` — variable where the entered text is stored

### Variable name in read

There is no `$` before the variable in:

`read -r name`

The `read` command needs the variable name where it should store the input.

The `$` is used later when reading the stored value:

`echo "$name"`

### User input with a default value

A script can first read input:

`read -r -p "Enter a URL [https://example.com]: " url`

Then apply a default value:

`url="${url:-https://example.com}"`

When Enter is pressed without typing anything, the default URL is selected.

### Check an empty string

`[[ -z "$name" ]]`

The `-z` operator checks whether a string has zero characters.

It is true when the value is empty.

Examples:

- `name=""` — true
- `name="Artem"` — false

### Check a non-empty string

`[[ -n "$value" ]]`

The `-n` operator checks whether a string contains one or more characters.

Examples:

- `value=""` — false
- `value="DevOps"` — true

### Bash condition

A basic Bash condition has this structure:

`if [[ condition ]]; then`

If the condition is true, Bash executes the `then` branch.

If the condition is false, Bash can execute the `else` branch.

The condition is closed with:

`fi`

### Compare strings

`[[ "$environment" == "production" ]]`

The `==` operator checks whether two string values are equal.

The `!=` operator checks whether two string values are different.

### Multiple conditions with elif

`elif` checks another condition when the previous condition was false.

The structure is:

`if`

`elif`

`else`

`fi`

I used it to distinguish:

- production
- staging
- development
- invalid values

### Invalid values

An unsupported environment produced:

`Invalid environment: testing`

The script then used:

`exit 1`

This indicates that the script did not complete successfully.

### File tests

Bash can check different types of filesystem paths.

Important operators:

- `-f` — a regular file exists
- `-d` — a directory exists
- `-e` — any type of path exists
- `-x` — a path exists and is executable

### Check a regular file

`[[ -f DevOps/Linux.md ]]`

This condition checks whether `DevOps/Linux.md` exists as a regular file.

My result was:

`Regular file exists: DevOps/Linux.md`

### Check a directory

`[[ -d DevOps ]]`

This condition checks whether `DevOps` exists as a directory.

My result was:

`Directory exists: DevOps`

### Check a missing path

The test for:

`missing-file.txt`

entered the `else` branch.

The result was:

`Path does not exist: missing-file.txt`

### Check executable permission

`[[ -x DevOps/Scripts/check-url.sh ]]`

This condition checks whether the health-check script is executable.

My result was:

`The script is executable.`

A script can be both:

- a regular file
- an executable file

### Logical AND operator

`command1 && command2`

The command after `&&` runs only when the first command succeeds.

A successful command normally returns exit code `0`.

Example:

`ls DevOps/Linux.md && echo "The file exists."`

Because the file exists, the second command runs.

### Logical OR operator

`command1 || command2`

The command after `||` runs only when the first command fails.

Example:

`ls missing-file.txt || echo "The file was not found."`

Because `ls` fails, the second command runs.

### Combine logical operators

`command && success_command || failure_command`

This can produce a simple success or failure result.

My website tests produced:

- available page — `HEALTHY`
- missing page — `UNHEALTHY`

### Command substitution

`$(command)`

Command substitution runs a command and captures its output.

Example:

`current_date="$(date)"`

The `date` command runs, and its output is stored in `current_date`.

### Store the kernel version

`kernel_version="$(uname -r)"`

This command stores the kernel version in a variable.

My result was:

`6.17.0-35-generic`

### Capture an HTTP status

`http_status="$(curl -sS -o /dev/null -w '%{http_code}' https://example.com)"`

This command runs curl and stores only the HTTP status code.

My result was:

`200`

### Capture response time

`response_time="$(curl -sS -o /dev/null -w '%{time_total}' https://example.com)"`

This command stores the total request duration.

One of my results was:

`0.206552`

The value is measured in seconds.

### Capture multiple values

Curl can print multiple values during one request:

`result="$(curl -sS -o /dev/null -w '%{http_code} %{time_total}' https://example.com)"`

The result looked like:

`200 0.181285`

The first value was the HTTP status.

The second value was the response time.

### Read multiple values

`read -r http_status response_time <<< "$result"`

This command separates the result and stores it in two variables.

The first value is stored in:

`http_status`

The second value is stored in:

`response_time`

### Here string

`<<< "$result"`

This is called a here string.

It sends the contents of a variable as input to a command.

In this example, it sends the value of `result` to `read`.

### HTTP health result

I compared the captured HTTP status:

`[[ "$http_status" == "200" ]]`

Status `200` entered the `then` branch and printed:

`Result: HEALTHY`

Status `404` entered the `else` branch and printed:

`Result: UNHEALTHY`

### Numeric comparisons

Bash provides operators for comparing numbers:

- `-eq` — equal
- `-ne` — not equal
- `-gt` — greater than
- `-ge` — greater than or equal
- `-lt` — less than
- `-le` — less than or equal

### Successful HTTP range

`[[ "$status" -ge 200 && "$status" -lt 300 ]]`

This condition checks whether the status is between `200` and `299`.

Both comparisons must be true.

This accepts all successful HTTP `2xx` status codes.

### HTTP status 204

Status `204` is successful because it is:

- greater than or equal to `200`
- less than `300`

`204 No Content` is a valid successful HTTP response.

### HTTP status 301

Status `301` is not considered successful by this condition because it is not less than `300`.

It is an HTTP redirect in the `3xx` range.

### Improved health-check script

I updated:

`DevOps/Scripts/check-url.sh`

The script now displays:

- checked URL
- HTTP status
- response time
- health result
- curl exit code for connection failures

### Capture curl result

The improved script uses:

`result="$(curl -sS -o /dev/null -w '%{http_code} %{time_total}' "$url")"`

Curl prints the HTTP status and response time.

Command substitution stores both values in `result`.

### Save curl exit status

Immediately after curl, the script uses:

`curl_status=$?`

This saves curl's exit code before another command changes `$?`.

### Check curl failure

`[[ "$curl_status" -ne 0 ]]`

The `-ne` operator means not equal.

This condition checks whether curl returned an error.

If curl failed, the script:

- prints `FAILED`
- displays the curl exit code
- exits with the same code

### Split the curl result

When curl succeeds, the script uses:

`read -r http_status response_time <<< "$result"`

This stores the HTTP status and response time in separate variables.

### Check the 2xx range

The improved script uses:

`[[ "$http_status" -ge 200 && "$http_status" -lt 300 ]]`

All HTTP responses from `200` to `299` are considered healthy.

Other HTTP statuses are considered unhealthy.

### Improved health-check results

The successful page returned:

- HTTP status `200`
- result `HEALTHY`
- script exit code `0`

The missing page returned:

- HTTP status `404`
- result `UNHEALTHY`
- script exit code `1`

The nonexistent domain returned:

- result `FAILED`
- curl exit code `6`
- script exit code `6`

### Exit code 0

The script returns:

`0`

when the HTTP response is in the `2xx` range.

This means the health check succeeded.

### Exit code 1

The script returns:

`1`

when the server responds, but the HTTP status is outside the `2xx` range.

For example, HTTP `404` produces script exit code `1`.

### Preserve curl errors

When curl itself fails, the script preserves curl's error code.

For example:

`curl: (6) Could not resolve host`

The script also returns:

`6`

This distinguishes an HTTP failure from a DNS or connection failure.

### Why 404 returns 1 instead of 22

The updated curl command does not use:

`-f`

Therefore, curl can successfully receive HTTP `404` and return exit code `0`.

The script then reads the HTTP status and decides that `404` is unhealthy.

The `else` branch explicitly contains:

`exit 1`

Therefore, HTTP `404` now returns script exit code `1`, not curl exit code `22`.

### Basic Bash script workflow

1. Add a shebang.
2. Define variables.
3. Read script arguments.
4. Apply default values when needed.
5. Quote variable expansions.
6. Run commands and capture their output.
7. Save command exit codes immediately.
8. Use `if`, `elif`, and `else` to make decisions.
9. Use string or numeric comparisons.
10. Return a meaningful exit code.

### Important vocabulary

- Bash script — Bash-скрипт
- interpreter — інтерпретатор
- shebang — рядок, який визначає інтерпретатор
- executable — виконуваний
- permission — право доступу
- variable — змінна
- variable assignment — присвоєння значення змінній
- variable expansion — підстановка значення змінної
- quote — лапка
- argument — аргумент
- positional argument — позиційний аргумент
- default value — значення за замовчуванням
- empty string — порожній рядок
- user input — введення користувача
- condition — умова
- string comparison — порівняння рядків
- numeric comparison — числове порівняння
- regular file — звичайний файл
- directory — директорія
- logical operator — логічний оператор
- command substitution — підстановка команди
- command output — результат команди
- here string — передавання рядка як вводу
- exit status — код завершення
- successful — успішний
- unsuccessful — неуспішний
- healthy — працездатний
- unhealthy — непрацездатний
- invalid value — неправильне значення

### My sentence

I learned how to create Bash scripts with variables, arguments, default values, conditions, command substitution, file tests, logical operators, and meaningful exit codes.
## Lesson 13 — Bash loops and functions

Today I learned how to repeat commands with loops, store multiple values in arrays, create reusable functions, check several URLs, count results, and return one overall exit code.

I also created a multi-URL health-check script:

`DevOps/Scripts/check-urls.sh`

### Bash loop

A loop repeats the same commands several times.

A basic `for` loop has this structure:

```bash
for variable in value1 value2 value3; do
    commands
done
```

During every iteration, Bash stores the current value in the loop variable.

### Loop through words

```bash
for word in Linux Bash DevOps; do
    echo "Topic: $word"
done
```

The loop ran three times.

The values were:

- first iteration — `Linux`
- second iteration — `Bash`
- third iteration — `DevOps`

The output was:

```text
Topic: Linux
Topic: Bash
Topic: DevOps
```

### The do and done keywords

`do` begins the commands that Bash should repeat.

`done` closes the loop.

### Loop through numbers

```bash
for number in 1 2 3 4 5; do
    echo "Number: $number"
done
```

This loop printed the numbers from `1` to `5`.

### Brace expansion

```bash
for number in {1..5}; do
    echo "Number: $number"
done
```

The expression:

`{1..5}`

expands into:

```text
1 2 3 4 5
```

Brace expansion is useful for generating a simple sequence of values.

### Loop through URLs

```bash
for url in \
    https://example.com \
    https://github.com \
    https://example.com/not-existing-page
do
    echo "Checking: $url"
done
```

This loop processed every URL one at a time.

The backslash:

`\`

continues the same command on the next line.

### Why loops are useful

Without a loop, the same command must be copied for every value.

A loop reduces repeated code and applies the same operation consistently to every URL.

### Run a script inside a loop

```bash
for url in \
    https://example.com \
    https://example.com/not-existing-page
do
    ./DevOps/Scripts/check-url.sh "$url"
    script_status=$?
done
```

The current URL is passed to the script as its first argument.

The exit code is saved immediately with:

`script_status=$?`

This is important because the next command would replace the value of `$?`.

### Loop continues after a failure

The health-check script returned different exit codes:

- `0` — healthy URL
- `1` — unhealthy HTTP result
- `6` — DNS resolution failure

The parent loop continued after every result.

An exit code returned by a separately executed script does not automatically stop the loop.

### Bash array

An array stores several values under one variable name.

Example:

```bash
urls=(
    "https://example.com"
    "https://github.com"
    "https://example.com/not-existing-page"
)
```

The `urls` array contained three elements.

### Array indexes

Bash arrays are zero-indexed.

This means the first element has index `0`.

```text
urls[0] — first element
urls[1] — second element
urls[2] — third element
```

For my array:

```bash
echo "${urls[1]}"
```

returned:

```text
https://github.com
```

### Display all array elements

```bash
printf '%s\n' "${urls[@]}"
```

The expression:

`"${urls[@]}"`

expands all elements of the array.

Each element remains a separate, safely quoted argument.

### Count array elements

```bash
echo "${#urls[@]}"
```

`${#urls[@]}` returns the number of elements stored in the array.

My result was:

```text
3
```

### Loop through an array

```bash
for url in "${urls[@]}"; do
    echo "Checking: $url"
done
```

The loop processes every array element one at a time.

### Bash function

A function stores reusable commands under one name.

A basic function has this structure:

```bash
function_name() {
    commands
}
```

Calling the function name executes the commands inside it.

### Simple function

```bash
greet() {
    echo "Hello from Bash!"
}
```

The function is called with:

```bash
greet
```

The result was:

```text
Hello from Bash!
```

### Function arguments

Functions can receive arguments.

```bash
greet_user() {
    local name="${1:-Guest}"
    echo "Hello, $name!"
}
```

Inside a function:

- `$1` — first function argument
- `$2` — second function argument
- `$#` — number of function arguments

For:

```bash
greet_user Artem
```

the value of `$1` was:

```text
Artem
```

### Function default value

```bash
local name="${1:-Guest}"
```

When no argument is provided, the function uses:

```text
Guest
```

When an argument is provided, the function uses that value instead.

### Local variable

```bash
local name="Local value"
```

The `local` keyword creates a variable that belongs only to the function.

It prevents the function from accidentally changing a variable with the same name outside the function.

### Return from a function

```bash
return 0
```

`return` ends the current function and provides a function exit status.

It does not end the complete script.

### Exit from a script

```bash
exit 1
```

`exit` ends the complete script.

Commands written after `exit` are not executed.

### Return and exit

The difference is:

- `return` — ends only the current function
- `exit` — ends the complete script

The multi-URL checker uses `return` inside its function so that the loop can continue checking the remaining URLs.

### File-check function

```bash
check_file() {
    local path="${1:-DevOps/Linux.md}"

    if [[ -f "$path" ]]; then
        echo "File found: $path"
        return 0
    else
        echo "File not found: $path"
        return 1
    fi
}
```

An existing file returned:

```text
0
```

A missing file returned:

```text
1
```

### URL-check function

I moved the website-checking logic into a function:

```bash
check_url() {
    ...
}
```

The function receives the URL through:

```bash
local url="$1"
```

It uses local variables for:

- curl result
- curl exit code
- HTTP status
- response time

### Capture curl information

The function uses:

```bash
result="$(curl -sS -o /dev/null \
    -w '%{http_code} %{time_total}' \
    "$url")"
```

Curl prints:

- HTTP status
- total response time

Command substitution stores both values in `result`.

### Save curl exit code

Immediately after curl, the function uses:

```bash
curl_status=$?
```

This saves curl’s exit code before another command changes `$?`.

### Split the curl result

```bash
read -r http_status response_time <<< "$result"
```

The first value is stored in:

`http_status`

The second value is stored in:

`response_time`

### Function result codes

The `check_url` function returns:

- `0` — HTTP status is between `200` and `299`
- `1` — the server responded, but the HTTP status is unhealthy
- curl error code — curl could not complete the request

My results were:

```text
Healthy page       → 0
HTTP 404           → 1
DNS failure        → 6
```

### Why the function uses return

The function uses:

```bash
return "$curl_status"
```

instead of:

```bash
exit "$curl_status"
```

This allows the main loop to continue checking the next URL.

If the function used `exit`, the complete script would stop after the first technical failure.

### Command not found

I received:

```text
check_url: command not found
```

The exit code was:

```text
127
```

Exit code `127` means Bash could not find the command or function.

This happened because I ran the loop directly in the terminal without defining the `check_url` function in that terminal session.

### Function scope

The function was defined inside:

`/tmp/check-urls.sh`

It existed only inside the Bash process that ran that script.

After the script finished, the function was not available in the original terminal.

Therefore:

```bash
declare -F check_url
```

showed no output.

### Check Bash syntax

```bash
bash -n DevOps/Scripts/check-urls.sh
```

The `-n` option checks the syntax without executing the script.

No output means the syntax is valid.

### Bash debug mode

```bash
bash -x DevOps/Scripts/check-urls.sh
```

The `-x` option displays commands as Bash executes them.

Lines beginning with `+` show commands executed by Bash.

Lines beginning with `++` can show commands executed inside command substitution.

### Result counters

I created three counters:

```bash
healthy_count=0
unhealthy_count=0
failed_count=0
```

They begin at zero because no URLs have been checked yet.

### Increment a counter

```bash
((healthy_count++))
```

This increases `healthy_count` by one.

It is similar to:

```bash
healthy_count=$((healthy_count + 1))
```

The same logic is used for the other counters.

### Select a counter

```bash
if [[ "$function_status" -eq 0 ]]; then
    ((healthy_count++))
elif [[ "$function_status" -eq 1 ]]; then
    ((unhealthy_count++))
else
    ((failed_count++))
fi
```

The script selects a counter according to the function exit code.

### Summary

The script prints a final summary.

One result was:

```text
Summary
Total URLs: 3
Healthy: 1
Unhealthy: 1
Failed: 1
```

The total number of URLs is calculated with:

```bash
${#urls[@]}
```

### Default URL list

The script contains a default array of URLs.

It uses that list when no arguments are provided:

```bash
./DevOps/Scripts/check-urls.sh
```

### Script argument count

```bash
$#
```

`$#` contains the number of arguments passed to the script.

The condition:

```bash
[[ "$#" -gt 0 ]]
```

checks whether one or more arguments were provided.

`-gt` means greater than.

### All script arguments

```bash
"$@"
```

`"$@"` represents all arguments passed to the script.

Every argument remains separate.

### Store arguments in an array

```bash
urls=("$@")
```

This stores all provided arguments in the `urls` array.

It allows the script to check one URL, several URLs, or only a specific failing URL without editing the script.

### Default and custom URLs

The script uses this logic:

```bash
if [[ "$#" -gt 0 ]]; then
    urls=("$@")
else
    urls=(
        "https://example.com"
        "https://example.com/not-existing-page"
        "https://this-domain-should-not-exist-987654321.com"
    )
fi
```

Custom arguments are used when they are provided.

The default array is used when the script receives no arguments.

### Check custom URLs

```bash
./DevOps/Scripts/check-urls.sh \
    https://example.com \
    https://github.com
```

The result was:

```text
Total URLs: 2
Healthy: 2
Unhealthy: 0
Failed: 0
```

### Overall script status

I created:

```bash
overall_status=0
```

This variable stores the final result of all URL checks.

### Overall exit codes

The multi-URL script defines:

- `0` — all URLs are healthy
- `1` — at least one URL returned an unhealthy HTTP status
- `2` — at least one technical check failed

These are summary exit codes created for the multi-URL script.

### All URLs healthy

Two healthy URLs produced:

```text
Healthy: 2
Unhealthy: 0
Failed: 0
Whole script exit code: 0
```

### Unhealthy HTTP result

One healthy page and one `404` page produced:

```text
Healthy: 1
Unhealthy: 1
Failed: 0
Whole script exit code: 1
```

### Technical failure

One healthy page and one DNS failure produced:

```text
Healthy: 1
Unhealthy: 0
Failed: 1
Whole script exit code: 2
```

The `check_url` function returned curl exit code `6`.

The main script converted the technical failure into its overall exit code `2`.

### Exit must be last

I originally placed:

```bash
exit "$overall_status"
```

before the summary information.

The script stopped immediately, so the remaining `echo` commands did not run.

The correct position is at the end:

```bash
echo "Summary"
echo "Total URLs: ${#urls[@]}"
echo "Healthy: $healthy_count"
echo "Unhealthy: $unhealthy_count"
echo "Failed: $failed_count"

exit "$overall_status"
```

### Multi-URL health-check script

I created:

`DevOps/Scripts/check-urls.sh`

The script:

1. defines a reusable `check_url` function;
2. accepts custom URL arguments;
3. uses default URLs when no arguments are provided;
4. loops through every URL;
5. saves each function exit code;
6. counts healthy, unhealthy, and failed results;
7. prints a summary;
8. returns one overall exit code.

### Basic loop and function workflow

1. Store values in an array.
2. Loop through every array element.
3. Pass the current value to a function.
4. Use local variables inside the function.
5. Return a meaningful function status.
6. Save `$?` immediately.
7. Update the correct counter.
8. Continue processing the remaining values.
9. Print a final summary.
10. Exit with one overall script status.

### Important vocabulary

- loop — цикл
- iteration — ітерація, один прохід циклу
- repeat — повторювати
- array — масив
- array element — елемент масиву
- index — індекс
- zero-indexed — індексація починається з нуля
- function — функція
- reusable — придатний для повторного використання
- function argument — аргумент функції
- local variable — локальна змінна
- global variable — глобальна змінна
- return — завершити функцію та повернути статус
- exit — завершити весь скрипт
- counter — лічильник
- increment — збільшити на одиницю
- summary — підсумок
- default list — список за замовчуванням
- custom argument — користувацький аргумент
- overall status — загальний статус
- syntax check — перевірка синтаксису
- debug mode — режим налагодження
- command not found — команду не знайдено
- function scope — область видимості функції
- technical failure — технічна помилка

### My sentence

I learned how to use Bash loops, arrays, functions, local variables, counters, script arguments, and exit codes to check multiple websites and produce one overall health result.
## Lesson 14 — Linux processes and job control

Today I learned how Linux represents running programs as processes, how to inspect process relationships, manage foreground and background jobs, send signals, monitor resource usage, and change process priority.

### Linux process

A process is a running instance of a program.

For example, when I run:

```bash
curl https://example.com
```

Linux creates a `curl` process.

When the command finishes, the process ends.

### Process ID

Every process has a unique process ID called a PID.

```text
PID — Process ID
```

A PID identifies one currently running process.

PIDs can be reused after a process finishes.

### Parent process ID

A process can be started by another process.

```text
PPID — Parent Process ID
```

The process that starts another process is called the parent.

The new process is called the child.

Example:

```text
bash
└── curl
```

Bash is the parent process, and curl is its child.

### Current Bash PID

Bash provides:

```bash
$$
```

`$$` contains the PID of the current shell.

I ran:

```bash
echo "Current Bash PID: $$"
```

My result was:

```text
Current Bash PID: 5114
```

### Inspect the current Bash process

```bash
ps -p $$ -f
```

The command showed:

```text
UID    PID   PPID  C  STIME  TTY    TIME      CMD
artem  5114  3327  0  14:44  pts/0  00:00:00 bash
```

### The ps command

`ps` displays information about running processes.

In:

```bash
ps -p $$ -f
```

the options mean:

- `-p` — select a process by PID
- `$$` — current Bash PID
- `-f` — display the full output format

### Important ps columns

Important process columns include:

- `UID` — user who owns the process
- `PID` — process ID
- `PPID` — parent process ID
- `C` — CPU usage indicator
- `STIME` — process start time
- `TTY` — associated terminal
- `TIME` — total CPU time used
- `CMD` — command that started the process

### CPU time and elapsed time

The `TIME` column shows CPU time consumed by the process.

It does not show how long the process has existed in real time.

The `ETIME` or `ELAPSED` column shows the real elapsed time since the process started.

### Current parent PID

Bash provides:

```bash
$PPID
```

`$PPID` contains the PID of the current shell’s parent process.

I ran:

```bash
echo "Current PID: $$"
echo "Parent PID: $PPID"
ps -p "$PPID" -f
```

My result was:

```text
Current PID: 5114
Parent PID: 3327
```

The parent process was also Bash.

### Nested Bash process

My relationship was:

```text
bash, PID 3327
└── bash, PID 5114
```

This means one Bash process started another Bash process.

This can happen after running:

```bash
bash
```

inside an existing Bash shell.

### Display several PIDs

```bash
ps -o pid,ppid,tty,stat,cmd -p "$$,$PPID"
```

The PID values must be passed as one comma-separated argument.

This is correct:

```bash
-p "$$,$PPID"
```

This produced an error:

```bash
-p "$$", "$PPID"
```

The space caused `ps` to receive an improper PID list.

### Custom ps output

The `-o` option selects which columns to display.

Example:

```bash
ps -o pid,ppid,tty,stat,cmd -p "$$,$PPID"
```

This displays:

- PID
- PPID
- terminal
- process state
- command

### Process state

The `STAT` column shows the process state.

Common states include:

- `R` — running
- `S` — sleeping or waiting
- `T` — stopped
- `Z` — zombie
- `I` — idle kernel thread

A Bash shell waiting for keyboard input normally has state:

```text
S
```

This is normal.

### Additional STAT characters

Process states can contain additional characters.

Examples:

- `s` — session leader
- `l` — multithreaded process
- `+` — foreground process group
- `N` — increased niceness, lower priority
- `<` — higher priority

For example:

```text
Ss
```

means the process is sleeping and is also a session leader.

### Process tree with ps

```bash
ps -f --forest -p "$$,$PPID"
```

The `--forest` option displays parent-child relationships visually.

My result showed:

```text
bash
 \_ bash
```

The `\_` symbol marks the child process.

### Foreground process

A foreground process controls the terminal.

When a foreground command runs, the shell normally waits for it to finish.

Example:

```bash
sleep 300
```

The terminal cannot accept another command until `sleep` finishes or is stopped.

### Background process

The ampersand starts a command in the background:

```bash
sleep 300 &
```

The shell immediately returns the command prompt.

My output looked like:

```text
[1] 5761
```

This contained:

- `[1]` — shell job number
- `5761` — process PID

### Job number and PID

A job number belongs to the current shell’s job-control system.

A PID belongs to the Linux process system.

They are not the same thing.

Example:

```text
Job number: 1
PID: 5761
```

A job is referenced with `%`:

```bash
%1
```

A process is referenced by its PID:

```bash
5761
```

### Last background PID

Bash provides:

```bash
$!
```

`$!` contains the PID of the most recently started background process.

Example:

```bash
sleep 300 &
sleep_pid=$!
```

This saves the new process PID in `sleep_pid`.

### Display shell jobs

```bash
jobs -l
```

The `jobs` command displays jobs managed by the current shell.

The `-l` option also displays their PIDs.

My output looked like:

```text
[1]+ 5761 Running    sleep 300 &
```

### Current job marker

In `jobs` output:

```text
+
```

marks the current or default job.

It is the job used when a job-control command does not specify another job.

### Bring a job to the foreground

```bash
fg %1
```

`fg` moves job number `1` into the foreground.

The terminal then waits for that job.

### Stop a foreground job

I pressed:

```text
Ctrl+Z
```

This paused the foreground process.

The result was:

```text
[1]+ Stopped    sleep 300
```

`Ctrl+Z` does not terminate the process.

It normally sends:

```text
SIGTSTP
```

### Resume a job in the background

```bash
bg %1
```

`bg` resumes stopped job number `1` in the background.

My job state changed:

```text
Running → Stopped → Running
```

### Commands are case-sensitive

I accidentally entered:

```bash
BG %1
```

Bash returned:

```text
BG: command not found
```

The correct command was:

```bash
bg %1
```

Linux and Bash commands are case-sensitive.

### Terminate a job

```bash
kill %1
```

This sends a termination signal to job number `1`.

Here `%1` means shell job number `1`, not Linux PID `1`.

### Normal completion

A background command that finishes naturally can show:

```text
Done
```

`Done` means the command completed normally.

### Terminated process

A process stopped by `SIGTERM` can show:

```text
Terminated
```

The difference is:

```text
Done        — process completed normally
Terminated  — process ended because of a signal
```

### The kill command

Despite its name, `kill` sends signals to processes.

A plain command:

```bash
kill "$process_pid"
```

sends:

```text
SIGTERM
```

`SIGTERM` is signal number:

```text
15
```

### SIGTERM

`SIGTERM` asks a process to terminate.

A program can catch this signal and perform cleanup before exiting.

It should normally be the first signal used to stop a process.

### SIGKILL

```bash
kill -KILL "$process_pid"
```

sends:

```text
SIGKILL
```

`SIGKILL` is signal number:

```text
9
```

It stops a process immediately.

A process cannot catch, handle, or ignore `SIGKILL`.

`SIGKILL` should normally be used only when `SIGTERM` does not work.

### Wait for a background process

```bash
wait "$process_pid"
```

`wait` waits for a background process to finish.

It then returns that process’s exit status.

The status must be saved immediately:

```bash
wait "$process_pid"
process_status=$?
```

### Signal-related exit status

When a process is terminated by a signal, Bash commonly reports:

```text
128 + signal number
```

For `SIGTERM`:

```text
128 + 15 = 143
```

My result was:

```text
Process exit status: 143
```

For `SIGKILL`:

```text
128 + 9 = 137
```

My result was:

```text
Process exit status: 137
```

### Wait for several processes

I started two background processes:

```bash
sleep 500 &
first_pid=$!

sleep 600 &
second_pid=$!
```

I terminated both:

```bash
kill "$first_pid" "$second_pid"
```

Then I waited for them separately:

```bash
wait "$first_pid"
first_status=$?

wait "$second_pid"
second_status=$?
```

Both returned:

```text
143
```

Waiting separately allowed me to save each process status.

### Find processes with pgrep

```bash
pgrep -a -x sleep
```

Options:

- `pgrep` — search for processes
- `-a` — show PID and command arguments
- `-x` — require an exact process-name match

My result showed:

```text
6009 sleep 500
6010 sleep 600
```

### Find processes with ps

```bash
ps -C sleep -o pid,ppid,stat,etime,cmd
```

The `-C sleep` option selects processes whose command name is `sleep`.

The output included:

- PID
- PPID
- state
- elapsed time
- command

### System-wide process list

```bash
ps aux
```

This displays processes from all users.

Important columns include:

- `USER` — process owner
- `PID` — process ID
- `%CPU` — CPU usage
- `%MEM` — memory usage
- `VSZ` — virtual memory size
- `RSS` — physical memory currently used
- `TTY` — controlling terminal
- `STAT` — process state
- `START` — process start time
- `TIME` — CPU time
- `COMMAND` — complete command

### Virtual memory

`VSZ` shows the total virtual address space used by a process.

It is not the same as physical RAM currently occupied.

### Resident memory

`RSS` shows the physical RAM currently used by a process.

It is normally measured in KiB.

For example:

```text
920084 KiB
```

is approximately:

```text
898 MiB
```

### Sort ps output by CPU

```bash
ps aux --sort=-%cpu | head
```

The minus sign sorts in descending order.

Processes with the highest CPU usage appear first.

### Sort ps output by memory

```bash
ps aux --sort=-%mem | head
```

Processes with the highest memory usage appear first.

### Cleaner ps output

Long graphical-application arguments made `ps aux` difficult to read.

I used:

```bash
ps -eo user,pid,ppid,pcpu,pmem,stat,comm --sort=-pcpu | head
```

and:

```bash
ps -eo user,pid,ppid,pcpu,pmem,rss,stat,comm --sort=-pmem | head
```

The `comm` field displays a short process name instead of the complete command line.

### Full command and short command

The difference is:

- `cmd` or `args` — complete command and arguments
- `comm` — short executable name

Some values in `comm` can appear shortened.

To see a full command for one PID:

```bash
ps -p PID -o pid,ppid,cmd
```

### Processes without a terminal

Graphical processes often showed:

```text
TTY: ?
```

This means they do not have a controlling terminal.

For example, Firefox launched from the desktop is not connected to my current terminal.

### Multiple application processes

Firefox and VS Code used several processes.

A modern application may use separate processes for:

- the main application
- web pages or tabs
- extensions
- GPU work
- utility services

This improves isolation and stability.

### Monitor processes with top

```bash
top
```

`top` displays a continuously updating process list.

Unlike `ps`, which shows one snapshot, `top` refreshes automatically.

### Top summary

The top section includes:

- system uptime
- number of users
- load average
- process totals
- CPU usage
- memory usage
- swap usage

### Top process columns

Important `top` columns include:

- `PID`
- `USER`
- `PR`
- `NI`
- `VIRT`
- `RES`
- `SHR`
- `S`
- `%CPU`
- `%MEM`
- `TIME+`
- `COMMAND`

### Sort processes in top

The following uppercase keys change the sorting field:

```text
P — sort by CPU usage
M — sort by memory usage
N — sort by PID
T — sort by total CPU time
```

Uppercase `P` means:

```text
Shift+p
```

Lowercase `p` does not perform the same action.

### Reverse top sorting

```text
R
```

reverses the current sorting direction.

For example, after sorting by memory:

```text
M
```

pressing:

```text
R
```

changes highest-first sorting to lowest-first sorting.

### Highlight the sorting column

In `top`:

```text
x
```

highlights the current sorting column.

This helps confirm whether the list is sorted by `%CPU`, `%MEM`, or another field.

### Filter top by user

The `U` command can filter the displayed process list by username.

It filters processes; it does not sort them alphabetically by username.

### Toggle command display in top

Lowercase:

```text
c
```

switches between a short command name and the complete command line.

It does not sort by CPU usage.

### Quit top

```text
q
```

closes `top`.

### Process niceness

Linux processes can have a niceness value.

The common range is:

```text
-20 — highest priority
  0 — default niceness
 19 — lowest priority
```

A process with a larger positive niceness value is “nicer” to other processes because it receives a lower scheduling priority.

### NI column

```text
NI
```

shows the process niceness value.

A normal process commonly starts with:

```text
NI: 0
```

### PR or PRI column

```text
PR
```

or:

```text
PRI
```

shows the scheduler’s process priority representation.

For ordinary process management, the `NI` column is usually easier to interpret.

### Change an existing process priority

```bash
renice 10 -p "$sleep_pid"
```

`renice` changes the niceness of an existing process.

My result was:

```text
old priority 0, new priority 10
```

The `NI` value changed:

```text
0 → 10
```

### Niceness process state

After increasing the niceness value, the process state showed:

```text
SN
```

This means:

- `S` — sleeping
- `N` — lower priority because of increased niceness

### User priority permissions

As a regular user, I could increase the niceness value:

```text
0 → 10
```

This lowered the process priority.

I then tried:

```bash
renice 0 -p "$sleep_pid"
```

The result was:

```text
Permission denied
renice exit status: 1
```

Changing:

```text
10 → 0
```

would increase the process priority.

A regular user normally cannot increase process priority without additional privileges.

### Start a process with nice

```bash
nice -n 15 sleep 300 &
```

`nice` starts a new command with a selected niceness value.

The command means:

- `nice` — start a command with modified niceness
- `-n 15` — use niceness value `15`
- `sleep 300` — command to run
- `&` — run it in the background

My process started with:

```text
NI: 15
STAT: SN
```

### Nice and renice

The difference is:

```text
nice    — start a new process with modified niceness
renice  — change the niceness of an existing process
```

### Process tree with pstree

```bash
pstree -p "$$"
```

`pstree` displays parent-child relationships as a tree.

The `-p` option includes PIDs.

My output showed:

```text
bash(5114)─┬─pstree(7024)
           └─sleep(7022)
```

This meant:

```text
bash, PID 5114
├── pstree, PID 7024
└── sleep, PID 7022
```

### Why pstree displayed itself

Bash created a `pstree` process to run the command.

While `pstree` inspected the process tree, it could see itself as a child of Bash.

After printing the output, the `pstree` process ended.

### The proc filesystem

Linux exposes process and kernel information through:

```text
/proc
```

`/proc` is a virtual filesystem generated by the kernel.

It is not a normal directory of files permanently stored on disk.

### Process directory in proc

Every running process has a directory:

```text
/proc/PID
```

For my process with PID `7057`, Linux created:

```text
/proc/7057
```

I checked it with:

```bash
ls -ld "/proc/$sleep_pid"
```

### Process command line in proc

```bash
tr '\0' ' ' < "/proc/$sleep_pid/cmdline"
echo
```

The `cmdline` file stores command arguments separated by null characters.

`tr` replaced the null characters with spaces.

My result was:

```text
sleep 300
```

### Process status in proc

```bash
grep -E '^(Name|State|Pid|PPid|Threads):' "/proc/$sleep_pid/status"
```

My result was:

```text
Name:    sleep
State:   S (sleeping)
Pid:     7057
PPid:    5114
Threads: 1
```

This showed:

- process name
- current state
- process PID
- parent PID
- number of threads

### Proc directory disappears

After terminating the process, I ran:

```bash
ls -ld "/proc/$sleep_pid"
```

The result was:

```text
No such file or directory
```

When a process ends, its `/proc/PID` directory disappears.

This shows that `/proc` represents the processes that currently exist.

### Pause a process with SIGSTOP

```bash
kill -STOP "$sleep_pid"
```

This sends:

```text
SIGSTOP
```

The signal pauses the process.

`SIGSTOP` cannot be caught, handled, or ignored by the process.

### Stopped process state

After `SIGSTOP`, my process showed:

```text
STAT: T
State: T (stopped)
jobs: Stopped (signal)
```

The `T` state means the process is stopped.

### Resume a process with SIGCONT

```bash
kill -CONT "$sleep_pid"
```

This sends:

```text
SIGCONT
```

The signal resumes the existing process.

It does not create a new process, and the PID remains the same.

### Resumed process state

After `SIGCONT`, the process showed:

```text
STAT: S
State: S (sleeping)
jobs: Running
```

The state transition was:

```text
S (sleeping)
→ T (stopped)
→ S (sleeping)
→ terminated
```

### SIGTSTP and SIGSTOP

Both can pause a process, but they are different.

```text
Ctrl+Z       → SIGTSTP
kill -STOP   → SIGSTOP
```

`SIGTSTP` is a terminal stop request and can potentially be handled by a program.

`SIGSTOP` is enforced by the kernel and cannot be handled or ignored.

### SIGCONT

`SIGCONT` resumes a stopped process.

It works for a process stopped by either `SIGTSTP` or `SIGSTOP`.

### Basic process-management workflow

1. Start a process.
2. Save its PID with `$!` when it runs in the background.
3. Inspect it with `ps`, `pgrep`, `pstree`, `top`, or `/proc`.
4. Check its parent PID and process state.
5. Move jobs between foreground and background when necessary.
6. Pause a process with `Ctrl+Z` or `SIGSTOP`.
7. Resume it with `bg`, `fg`, or `SIGCONT`.
8. Send `SIGTERM` for a normal shutdown.
9. Use `SIGKILL` only when necessary.
10. Use `wait` to collect the final exit status.

### Important signal summary

```text
SIGTERM  15 — request normal termination
SIGKILL   9 — terminate immediately
SIGSTOP  19 — pause immediately on Linux
SIGCONT  18 — resume a stopped process on Linux
SIGTSTP  20 — terminal stop request on Linux
```

Signal numbers can differ on some Unix-like systems, so signal names are usually clearer in commands.

### Important exit statuses

```text
0   — successful completion
1   — general failure
127 — command not found
137 — process terminated by SIGKILL
143 — process terminated by SIGTERM
```

### Important vocabulary

- process — процес
- running program — запущена програма
- process ID — ідентифікатор процесу
- parent process — батьківський процес
- child process — дочірній процес
- process tree — дерево процесів
- foreground — передній план
- background — фоновий режим
- job — завдання оболонки
- job number — номер завдання
- process state — стан процесу
- running — виконується
- sleeping — очікує
- stopped — призупинений
- zombie — зомбі-процес
- signal — сигнал
- terminate — завершити
- pause — призупинити
- resume — продовжити
- elapsed time — час, що минув
- CPU time — процесорний час
- memory usage — використання пам’яті
- virtual memory — віртуальна пам’ять
- resident memory — фізична пам’ять процесу
- process priority — пріоритет процесу
- niceness — значення поступливості процесу
- permission denied — доступ заборонено
- virtual filesystem — віртуальна файлова система
- thread — потік виконання
- cleanup — очищення ресурсів
- exit status — код завершення

### My sentence

I learned how to inspect and manage Linux processes, work with foreground and background jobs, send process signals, monitor CPU and memory usage, change process niceness, and read process information from the `/proc` filesystem.
## Lesson 15 — Linux users, groups, and ownership

Today I learned how Linux identifies users and groups, how file ownership affects access, how shared directories work, and how to manage users and groups safely.

### Linux users

A Linux user is an account that can own files, run processes, and receive permissions.

I checked my current username with:

```bash
whoami
```

My result was:

```text
artem
```

### User ID

Every Linux user has a numeric identifier:

```text
UID — User ID
```

I ran:

```bash
id
```

My user information included:

```text
uid=1000(artem)
```

This means:

```text
Username: artem
UID:      1000
```

Linux internally uses numeric IDs, while usernames provide readable names for people.

### Group ID

Every Linux group also has a numeric identifier:

```text
GID — Group ID
```

My primary group information was:

```text
gid=1000(artem)
```

This means:

```text
Group name: artem
GID:        1000
```

UIDs and GIDs use separate namespaces.

For example:

```text
UID 1000 → user artem
GID 1000 → group artem
```

The same number does not mean that the user and group are the same object.

### Primary group

A user has one primary group.

I checked mine with:

```bash
id -gn
```

My primary group was:

```text
artem
```

The primary group is normally assigned to newly created files unless another mechanism, such as directory setgid, changes the inherited group.

### Supplementary groups

A user can also belong to several supplementary groups.

I checked all my groups with:

```bash
groups
```

and:

```bash
id -Gn
```

My groups included:

```text
artem adm cdrom sudo dip plugdev users lpadmin
```

Examples:

- `sudo` — permits authorized administrative commands through `sudo`
- `adm` — can provide access to some system logs
- `plugdev` — access related to connected devices
- `lpadmin` — printer administration
- `users` — a general supplementary group

### Numeric group IDs

I ran:

```bash
id -G
```

My numeric group IDs were:

```text
1000 4 24 27 30 46 100 114
```

The group names and IDs appeared in the same order:

```text
artem   → 1000
adm     → 4
cdrom   → 24
sudo    → 27
dip     → 30
plugdev → 46
users   → 100
lpadmin → 114
```

### The Linux user database

I inspected my account with:

```bash
getent passwd "$USER"
```

My record was:

```text
artem:x:1000:1000:Artem:/home/artem:/bin/bash
```

The fields are separated by colons:

```text
username:password:UID:GID:comment:home:shell
```

My fields mean:

```text
artem          → username
x              → protected password data is stored elsewhere
1000           → UID
1000           → primary GID
Artem          → account description
/home/artem    → home directory
/bin/bash      → login shell
```

### The Linux group database

I inspected my primary group with:

```bash
getent group "$(id -gn)"
```

The result was:

```text
artem:x:1000:
```

The group fields are:

```text
group_name:password:GID:explicit_members
```

The empty final field does not mean that I am not a member.

My primary membership is defined by the GID in my user account record.

### Explicit supplementary membership

I checked the `users` group:

```bash
getent group users
```

The result was:

```text
users:x:100:artem
```

This means that `artem` is explicitly listed as a supplementary member of the `users` group.

### File ownership

Every file has:

- one owner;
- one assigned group;
- permissions for the owner;
- permissions for the group;
- permissions for others.

I created a temporary file:

```bash
touch /tmp/lesson15-file
```

I inspected it with:

```bash
ls -l /tmp/lesson15-file
```

The result was similar to:

```text
-rw-rw-r-- 1 artem artem 0 ... /tmp/lesson15-file
```

The first `artem` was the owner.

The second `artem` was the group.

### Inspect ownership with stat

I used:

```bash
stat -c 'Owner: %U (%u), Group: %G (%g), Permissions: %A' \
    /tmp/lesson15-file
```

The result was:

```text
Owner: artem (1000), Group: artem (1000), Permissions: -rw-rw-r--
```

Format symbols:

```text
%U → owner name
%u → numeric UID
%G → group name
%g → numeric GID
%A → symbolic permissions
%a → numeric permissions
%n → filename
```

### Permission categories

The permissions:

```text
-rw-rw-r--
```

can be divided into:

```text
-  rw-  rw-  r--
│   │    │    └── others
│   │    └─────── group
│   └──────────── owner
└──────────────── file type
```

For this file:

```text
Owner:  read and write
Group:  read and write
Others: read only
```

### Change a file group with chgrp

I changed the group from `artem` to `users`:

```bash
chgrp users /tmp/lesson15-file
```

The result changed from:

```text
artem:artem
```

to:

```text
artem:users
```

The owner and permissions remained unchanged.

A regular user can normally assign a file to a group that the user belongs to.

### Change only the group with chown

I also used:

```bash
chown :users /tmp/lesson15-file
```

The empty owner field before the colon means that only the group is changed.

These commands can have the same effect:

```bash
chgrp users FILE
chown :users FILE
```

### Forms of chown

```bash
chown USER FILE
```

Changes the owner.

```bash
chown USER:GROUP FILE
```

Changes the owner and group.

```bash
chown :GROUP FILE
```

Changes only the group.

### Changing ownership without privileges

I tried:

```bash
chown root:root /tmp/lesson15-file
```

The command failed:

```text
Operation not permitted
```

The exit status was:

```text
1
```

A regular user normally cannot transfer file ownership to another user.

### Administrative commands with sudo

My user belongs to the `sudo` group.

I changed the ownership with:

```bash
sudo chown root:root /tmp/lesson15-file
```

The result was:

```text
Owner: root (0)
Group: root (0)
```

`sudo` runs one command with elevated privileges, normally as `root`.

It does not permanently change the user of the current terminal.

### Password entry with sudo

When `sudo` requests a password, typed characters are not displayed.

This is normal security behaviour.

If the password is incorrect, `sudo` prints:

```text
Sorry, try again.
```

### Permission selection order

Linux checks permissions in this order:

1. If the process user is the file owner, use owner permissions.
2. Otherwise, if the user belongs to the file group, use group permissions.
3. Otherwise, use others permissions.

Linux does not combine owner, group, and others permissions.

### Access as others

After the file became:

```text
root:root
-rw-rw-r--
```

my user `artem` was neither the owner nor a member of the `root` group.

Linux therefore used:

```text
others: r--
```

Reading was allowed, but writing failed:

```text
Permission denied
Write exit status: 1
```

### Group-based write access

I changed the ownership to:

```bash
sudo chown root:users /tmp/lesson15-file
```

The file became:

```text
Owner: root
Group: users
Permissions: -rw-rw-r--
```

Because `artem` belongs to `users`, Linux applied group permissions:

```text
rw-
```

The write succeeded:

```text
Write exit status: 0
```

This demonstrated:

```text
group membership + group write permission = shared write access
```

### Remove and restore group write permission

I removed group write permission:

```bash
sudo chmod g-w /tmp/lesson15-file
```

The permissions became:

```text
-rw-r--r--
```

Writing failed because the group had only:

```text
r--
```

Reading still worked.

I restored group write permission:

```bash
sudo chmod g+w /tmp/lesson15-file
```

The permissions returned to:

```text
-rw-rw-r--
```

### File and directory permissions are different

I created a directory and a file:

```bash
mkdir /tmp/lesson15-dir
touch /tmp/lesson15-dir/first-file
```

The directory had:

```text
drwxrwxr-x
```

For directories:

```text
r → list entry names
w → create, delete, or rename entries
x → traverse the directory and access objects by name
```

The `x` permission on a directory does not mean running the directory.

### Directory execute permission

I removed execute permission from the directory owner:

```bash
chmod u-x /tmp/lesson15-dir
```

The owner permissions became:

```text
rw-
```

I could see the filename because the directory still had `r`.

However, I could not access the file itself:

```text
Permission denied
```

Reading the file failed even though the file had read permission because the directory lacked `x`.

Creating another file also failed.

Creating or deleting entries normally requires:

```text
w + x
```

on the directory.

### Owner permissions do not fall back to group permissions

I was both:

- the directory owner;
- a member of its group.

However, because I matched the owner category, Linux used only the owner permissions.

It did not add the group’s permissions.

After restoring:

```bash
chmod u+x /tmp/lesson15-dir
```

access worked again.

### Shared directories and setgid

I created a shared directory:

```bash
sudo mkdir /tmp/lesson15-shared
sudo chown root:users /tmp/lesson15-shared
sudo chmod 2775 /tmp/lesson15-shared
```

Its permissions were:

```text
drwxrwsr-x
```

Its numeric mode was:

```text
2775
```

The leading `2` enables the setgid bit on the directory.

### Setgid on a directory

The `s` in:

```text
rws
```

means:

- group execute permission is enabled;
- the directory has setgid;
- new files and subdirectories inherit the directory group.

I created:

```bash
touch /tmp/lesson15-shared/artem-file
```

The file became:

```text
Owner: artem
Group: users
```

The owner was the user who created it.

The group was inherited from the setgid directory.

### Setgid and umask are separate

Setgid controls the inherited group.

It does not automatically grant group write permission.

```text
setgid → determines the inherited group
umask  → determines initial permission bits
```

### The sticky bit

I inspected `/tmp`:

```bash
ls -ld /tmp
```

Its permissions were:

```text
drwxrwxrwt
```

Its numeric mode was:

```text
1777
```

The leading `1` enables the sticky bit.

The final `t` shows that the sticky bit is active.

### Sticky-bit behaviour

A sticky shared directory allows many users to create files.

However, a file can normally be deleted only by:

- the file owner;
- the directory owner;
- `root`.

I created a file owned by `root`:

```bash
sudo touch /tmp/lesson15-root-file
sudo chmod 666 /tmp/lesson15-root-file
```

Although all users could modify the file contents, I could not delete it as `artem`:

```text
Operation not permitted
rm exit status: 1
```

Deleting a file modifies the parent directory entry.

The sticky bit prevented me from deleting a file owned by another user.

I removed it with:

```bash
sudo rm /tmp/lesson15-root-file
```

### Operation not permitted and no such file

These errors mean different things:

```text
Operation not permitted
```

The file exists, but the requested action is not allowed.

```text
No such file or directory
```

The path does not exist.

### Default permissions and umask

I checked my current mask:

```bash
umask
umask -S
```

My result was:

```text
0002
u=rwx,g=rwx,o=rx
```

Maximum initial permissions are:

```text
Regular file: 666 → rw-rw-rw-
Directory:    777 → rwxrwxrwx
```

Regular files do not receive execute permission automatically.

With `umask 0002`, new objects normally receive:

```text
File:      664 → -rw-rw-r--
Directory: 775 → drwxrwxr-x
```

`umask` removes selected permission bits.

It is a bit mask, not ordinary decimal subtraction.

### Temporary umask with a subshell

I safely tested another mask in a child shell:

```bash
(
    umask 0027

    mkdir "$test_dir"
    touch "$test_dir/test-file"
)
```

Parentheses run the commands in a subshell.

The temporary `umask` did not change my current shell permanently.

With:

```text
umask 0027
```

the results were:

```text
New file:      640 → -rw-r-----
New directory: 750 → drwxr-x---
```

After the subshell ended, my main shell still had:

```text
0002
```

### The root account

I inspected `root`:

```bash
getent passwd root
id root
```

The account information included:

```text
Username:       root
UID:            0
Primary GID:    0
Home directory: /root
Login shell:    /bin/bash
```

`root` is the administrative superuser.

Commands run as `root` must be used carefully.

### The nobody account

I inspected the restricted account:

```bash
getent passwd nobody
id nobody
```

Its record included:

```text
Username:       nobody
UID:            65534
Primary group:  nogroup
Home directory: /nonexistent
Login shell:    /usr/sbin/nologin
```

The account does not have a normal home directory or interactive login shell.

### Run one command as another user

I ran:

```bash
sudo -u nobody whoami
sudo -u nobody id
```

The results confirmed that only those commands ran as `nobody`.

Afterwards:

```bash
whoami
```

still returned:

```text
artem
```

The form is:

```bash
sudo -u USER COMMAND
```

It runs one command as the selected user.

### Account database files

Linux traditionally stores user and group information in:

```text
/etc/passwd
/etc/group
/etc/shadow
```

I inspected their permissions:

```bash
ls -l /etc/passwd /etc/group /etc/shadow
```

On my system:

```text
/etc/passwd → readable by ordinary users
/etc/group  → readable by ordinary users
/etc/shadow → restricted
```

### The passwd file

`/etc/passwd` stores public account information such as:

- username;
- UID;
- primary GID;
- home directory;
- login shell.

It does not contain the real password hash.

The `x` field points to protected password information stored in `/etc/shadow`.

### The group file

`/etc/group` stores:

- group names;
- GIDs;
- explicit supplementary members.

My `users` record was:

```text
users:x:100:artem
```

### The shadow file

My `/etc/shadow` permissions were:

```text
-rw-r----- root shadow
```

The owner `root` had read and write access.

The group `shadow` had read access.

Others had no access.

As `artem`, reading it failed:

```text
Permission denied
Shadow read status: 1
```

### Create a group

I created a temporary group:

```bash
sudo groupadd lesson15team
```

The group received:

```text
GID: 1001
```

### Create a restricted user

I created a temporary user:

```bash
sudo useradd \
    --no-create-home \
    --shell /usr/sbin/nologin \
    --gid lesson15team \
    lesson15user
```

Options:

```text
--no-create-home
```

Does not create the home directory.

The account record can still contain a home-directory path.

```text
--shell /usr/sbin/nologin
```

Prevents normal interactive login.

```text
--gid lesson15team
```

Sets `lesson15team` as the primary group.

### Temporary user information

The result was:

```text
uid=1001(lesson15user)
gid=1001(lesson15team)
groups=1001(lesson15team)
```

The user initially had no supplementary groups.

### Add a supplementary group

I added the user to `users`:

```bash
sudo usermod -aG users lesson15user
```

The result was:

```text
Primary group:       lesson15team
Supplementary group: users
```

The `users` group record became:

```text
users:x:100:artem,lesson15user
```

### usermod -G and -aG

```bash
usermod -G GROUPS USER
```

Replaces the user’s supplementary-group list with the specified list.

```bash
usermod -aG GROUPS USER
```

Appends groups while preserving existing supplementary groups.

The options mean:

```text
-a → append
-G → supplementary groups
-g → primary group
```

Neither `-G` nor `-aG` changes the primary group.

To change the primary group:

```bash
usermod -g GROUP USER
```

Existing login sessions may need to be restarted before new group memberships become active.

### Supplementary groups grant filesystem access

The temporary user belonged to `users` as a supplementary member.

It could create a file in:

```text
/tmp/lesson15-shared
```

because the directory group was `users` and group permissions allowed writing.

The new file became:

```text
Owner: lesson15user
Group: users
```

This proved that supplementary-group membership grants real filesystem access.

### Collaboration between users

The file initially had:

```text
-rw-r--r--
```

The group had only read permission.

My first write attempt as `artem` failed:

```text
Permission denied
Append status: 1
```

The file owner added group write permission:

```bash
sudo -u lesson15user chmod g+w FILE
```

The permissions became:

```text
-rw-rw-r--
```

After that, `artem` could append text because both users belonged to the `users` group.

### Principle of least privilege

The principle of least privilege means:

> A user or process should receive only the permissions required to perform its task.

Services should not normally run as `root` when they can run under a restricted service account.

Separate users and groups reduce the damage caused by:

- software bugs;
- incorrect commands;
- compromised applications;
- accidental file modification.

### Safe cleanup

At the end of the lesson, I removed the temporary resources.

I removed files and directories first:

```bash
sudo rm -rf /tmp/lesson15-shared
rm -rf /tmp/lesson15-dir
sudo rm -f /tmp/lesson15-file
```

Then I removed the temporary user:

```bash
sudo userdel lesson15user
```

Then I removed the temporary group:

```bash
sudo groupdel lesson15team
```

### Verify removed users and groups

I checked:

```bash
id lesson15user
```

The result was:

```text
no such user
```

I checked:

```bash
getent group lesson15team
```

It returned no group record.

The `users` group returned to:

```text
users:x:100:artem
```

All temporary filesystem paths were also removed.

### Important command summary

```bash
whoami
```

Show the current username.

```bash
id
```

Show UID, primary GID, and groups.

```bash
id -gn
```

Show the primary group name.

```bash
id -Gn
```

Show all group names.

```bash
id -G
```

Show all numeric group IDs.

```bash
groups
```

Show the user’s groups.

```bash
getent passwd USER
```

Read a user-database entry.

```bash
getent group GROUP
```

Read a group-database entry.

```bash
chgrp GROUP FILE
```

Change a file’s group.

```bash
chown USER:GROUP FILE
```

Change a file’s owner and group.

```bash
chown :GROUP FILE
```

Change only the group.

```bash
chmod g+w FILE
```

Add group write permission.

```bash
chmod g-w FILE
```

Remove group write permission.

```bash
sudo -u USER COMMAND
```

Run one command as another user.

```bash
groupadd GROUP
```

Create a group.

```bash
useradd OPTIONS USER
```

Create a user.

```bash
usermod -aG GROUP USER
```

Append a supplementary group.

```bash
userdel USER
```

Delete a user.

```bash
groupdel GROUP
```

Delete a group.

```bash
umask
```

Display the current permission mask.

### Important numeric modes

```text
664  → -rw-rw-r--
640  → -rw-r-----
644  → -rw-r--r--
750  → drwxr-x---
775  → drwxrwxr-x
1777 → sticky shared directory
2775 → setgid shared directory
```

### Important vocabulary

- user — користувач
- user account — обліковий запис користувача
- user ID — ідентифікатор користувача
- group — група
- group ID — ідентифікатор групи
- primary group — основна група
- supplementary group — додаткова група
- owner — власник
- ownership — право власності
- permissions — права доступу
- read — читання
- write — запис
- execute — виконання
- traverse a directory — проходити через директорію
- access denied — доступ заборонено
- operation not permitted — операція не дозволена
- administrative privileges — адміністративні привілеї
- superuser — суперкористувач
- restricted account — обмежений обліковий запис
- shared directory — спільна директорія
- inherit — успадковувати
- setgid bit — біт setgid
- sticky bit — sticky bit
- permission mask — маска прав доступу
- least privilege — найменші привілеї
- append — додати без заміни
- replace — замінити
- explicit member — явно вказаний учасник
- login shell — оболонка входу
- home directory — домашня директорія

### My sentence

I learned how Linux users and groups control file access, how ownership and permissions work, and how to create secure shared directories using group permissions, setgid, and the sticky bit.
