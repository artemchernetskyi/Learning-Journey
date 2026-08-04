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

## Lesson 16 — Linux package management with APT and dpkg

Today I learned how Ubuntu manages software packages, repositories, dependencies, package metadata, upgrades, local `.deb` archives, package caches, and safe package removal.

I also practised inspecting package-manager plans before making changes.

### Operating system information

I inspected the Linux distribution with:

```bash
cat /etc/os-release
```

My system reported:

```text
Ubuntu 24.04.4 LTS
Version codename: noble
ID_LIKE: debian
```

Ubuntu belongs to the Debian family, so it uses:

- Debian `.deb` package archives;
- the `dpkg` low-level package manager;
- APT as its high-level package manager.

`LTS` means Long-Term Support.

### Kernel and machine architecture

I inspected the kernel with:

```bash
uname -a
```

My system included:

```text
Kernel:       7.0.0-28-generic
Architecture: x86_64
```

In package-manager terminology, the same 64-bit PC architecture is normally called:

```text
amd64
```

The Linux distribution and Linux kernel are different:

```text
Ubuntu distribution → the complete operating system
Linux kernel         → the core that manages hardware and system resources
```

### Package-management commands

I located the main package-management tools:

```bash
command -v apt
command -v apt-get
command -v dpkg
command -v snap
```

The commands were located at:

```text
/usr/bin/apt
/usr/bin/apt-get
/usr/bin/dpkg
/usr/bin/snap
```

Their roles are different:

```text
apt      → convenient high-level package management
apt-get  → stable command interface often used in scripts
dpkg     → low-level management of installed packages and local .deb files
snap     → a separate package system managed by snapd
```

### Tool versions

I checked:

```bash
apt --version
dpkg --version | head -n 1
snap version
```

The versions included:

```text
APT:  2.8.3
dpkg: 1.22.6
snap: 2.76
```

### What is a package?

A package is an archive containing software and metadata.

Package metadata can include:

```text
package name
version
architecture
dependencies
description
maintainer
installed size
download size
list of files
configuration files
```

On Ubuntu and Debian systems, package archives normally use the `.deb` extension.

### What is a repository?

A repository is a server or storage location containing:

- package archives;
- package metadata;
- version information;
- dependency information;
- cryptographic signatures.

APT reads repository metadata to determine which packages and versions are available.

### Repository configuration

I inspected:

```text
/etc/apt/sources.list
/etc/apt/sources.list.d/
```

Ubuntu 24.04 commonly uses files ending in:

```text
.sources
```

Older one-line repository definitions often use:

```text
.list
```

Backup files ending in `.save` or `.orig` may exist but are not necessarily active APT source files.

### Repository fields

The Ubuntu `.sources` files contained fields such as:

```text
Types
URIs
Suites
Components
Signed-By
```

They mean:

```text
Types       → package source type, such as deb
URIs        → repository server addresses
Suites      → release and update channels
Components  → package sections
Signed-By   → key used to verify repository signatures
```

### Configured repositories

My system included repositories from:

```text
archive.ubuntu.com
security.ubuntu.com
esm.ubuntu.com
downloads.claude.ai
```

The Claude Desktop repository is a third-party repository maintained by Anthropic.

Third-party repositories must be treated carefully because they are maintained outside Ubuntu.

### Ubuntu suites

The configured Ubuntu suites included:

```text
noble
noble-updates
noble-security
noble-backports
```

Their roles are:

```text
noble           → packages released with Ubuntu 24.04
noble-updates   → regular bug fixes and updates
noble-security  → security updates
noble-backports → newer packages rebuilt for the current Ubuntu release
```

### Ubuntu repository components

My system enabled:

```text
main
restricted
universe
multiverse
```

Their general meanings are:

```text
main        → officially supported software
restricted  → supported software with licensing restrictions
universe    → community-maintained software
multiverse  → software with additional legal or licensing restrictions
```

### Repository signatures

Repository definitions used `Signed-By` to identify trusted keyring files.

APT verifies repository signatures to help ensure that package metadata came from an expected source and was not modified in transit.

A valid signature does not guarantee that every package is safe, but it verifies the repository’s declared origin.

### APT package indexes

APT stores downloaded repository indexes in:

```text
/var/lib/apt/lists
```

These indexes allow APT to:

- search for packages;
- compare versions;
- calculate dependencies;
- determine upgrade candidates.

### Inspect package policy

I ran:

```bash
apt-cache policy
apt-cache policy bash curl
```

Important fields included:

```text
Installed
Candidate
Version table
```

They mean:

```text
Installed → version currently installed
Candidate → version APT would currently choose
Version table → available versions and their repository sources
```

### Package priorities

APT displayed priorities such as:

```text
500
100
```

In my output:

```text
500 → normal repository version
100 → installed version or lower-priority backports source
```

APT priorities help decide which available package version should become the candidate.

### Bash package policy

For Bash, the installed and candidate versions matched:

```text
Installed: 5.2.21-2ubuntu4
Candidate: 5.2.21-2ubuntu4
```

The `***` marker identified the installed version.

### Curl package policy

For Curl, the installed and candidate versions also matched:

```text
Installed: 8.5.0-2ubuntu10.11
Candidate: 8.5.0-2ubuntu10.11
```

APT also showed an older version from the original `noble` repository.

### Inspect repository metadata with apt show

I ran:

```bash
apt show bash
```

Important fields included:

```text
Package
Version
Priority
Essential
Section
Architecture
Installed-Size
Download-Size
Depends
Pre-Depends
Recommends
Suggests
```

### Dependency strengths

Package relationships have different strengths:

```text
Pre-Depends → must be satisfied before package configuration begins
Depends     → required for normal operation
Recommends  → strongly useful and normally installed
Suggests    → optional related software
```

For Bash, examples included:

```text
Pre-Depends: libc6, libtinfo6
Depends:     base-files, debianutils
Recommends:  bash-completion
Suggests:    bash-doc
```

### Essential packages

Bash reported:

```text
Essential: yes
Priority: required
```

Essential system packages should not be removed as ordinary exercises because doing so could seriously damage the operating system.

### apt show versus dpkg -s

These commands can show similar information but use different data sources:

```text
apt show PACKAGE → repository metadata known to APT
dpkg -s PACKAGE  → local installed-package database
```

`apt show` can describe an available package that is not installed.

`dpkg -s` describes the local package record.

### Query installed packages with dpkg-query

I inspected Bash and Curl with:

```bash
dpkg-query -W \
    -f='Package: ${binary:Package}\nVersion: ${Version}\nStatus: ${db:Status-Abbrev} ${Status}\nArchitecture: ${Architecture}\n\n' \
    bash curl
```

Both packages showed:

```text
Status: ii install ok installed
Architecture: amd64
```

### Package-state abbreviations

Important `dpkg` package states include:

```text
ii → requested for installation and installed correctly
rc → package removed, configuration files remain
un → package not installed or unknown
```

The full healthy status is:

```text
install ok installed
```

### List files installed by a package

I ran:

```bash
dpkg -L bash
```

Examples included:

```text
/etc/bash.bashrc
/etc/skel/.bashrc
/usr/bin/bash
/usr/bin/bashbug
/usr/share/doc/bash
```

`dpkg -L PACKAGE` answers:

> Which files and directories are registered for this installed package?

Directories such as `/usr/bin` can appear in many package file lists because many packages place files there.

### Find which package owns a file

I ran:

```bash
dpkg -S /usr/bin/bash
```

The result was:

```text
bash: /usr/bin/bash
```

`dpkg -S PATH` answers:

> Which installed package registered this path?

### Inspect installed package status

I ran:

```bash
dpkg -s bash
```

The local record included:

```text
Package: bash
Essential: yes
Status: install ok installed
Architecture: amd64
Version: 5.2.21-2ubuntu4
```

### Configuration files

The Bash package listed files under:

```text
Conffiles:
```

`dpkg` tracks package-managed configuration files specially.

The checksums beside conffiles help determine whether a local administrator modified them.

During an upgrade, `dpkg` may ask whether to keep a locally modified configuration file or install the package maintainer’s new version.

### Search for packages

I searched for the exact package name `tree`:

```bash
apt search '^tree$'
```

The regular-expression anchors mean:

```text
^ → beginning
$ → end
```

Therefore:

```text
^tree$ → exactly the package named tree
```

APT found:

```text
tree 2.1.1-2ubuntu3.24.04.2
```

The package belonged to:

```text
universe/utils
```

### Check whether a package is installed

I ran:

```bash
dpkg-query -W tree
```

Before installation, the command returned:

```text
no packages found matching tree
Exit status: 1
```

The package existed in the repository but was not installed.

### Simulate package installation

Before changing the system, I ran:

```bash
apt install --simulate tree
```

A simulation:

- displays the planned actions;
- shows dependencies;
- reports packages that would be installed or removed;
- does not download or install packages;
- does not change the package database.

The simulation planned:

```text
0 upgraded
1 newly installed
0 to remove
1 not upgraded
```

The package was not really installed until I ran the non-simulated command.

### Simulation limitations

APT warns that locking is disabled during simulation.

The real system state could change between simulation and execution, so a simulation is valuable but not an absolute guarantee.

### apt update

I refreshed package metadata with:

```bash
sudo apt update
```

`apt update`:

- contacts configured repositories;
- downloads current repository metadata;
- updates local package indexes;
- does not upgrade installed applications.

Important distinction:

```text
apt update  → refresh available-package information
apt upgrade → install available package upgrades
```

### Upgradable packages

After updating the indexes, APT reported one available upgrade:

```text
snapd 2.75.2+ubuntu24.04 → 2.76+ubuntu24.04
```

I did not perform this unrelated upgrade during the lesson.

### Install a package with APT

I installed `tree` with:

```bash
sudo apt install tree
```

APT displayed stages such as:

```text
Selecting previously unselected package
Preparing to unpack
Unpacking
Setting up
Processing triggers
```

The installation completed successfully.

### Installation triggers

APT processed a trigger for:

```text
man-db
```

Package triggers allow one package to notify another subsystem that related data should be updated.

Installing a manual page can cause the manual-page database to be refreshed.

### Verify an installation

I verified `tree` with:

```bash
command -v tree
tree --version
dpkg-query -W tree
apt-cache policy tree
```

The results included:

```text
Executable:   /usr/bin/tree
Version:      2.1.1-2ubuntu3.24.04.2
Status:       install ok installed
Architecture: amd64
```

The installed and candidate versions matched.

### Manual package classification

I checked:

```bash
apt-mark showmanual | grep -x tree
```

APT classified `tree` as manually installed because I explicitly requested it.

```text
manual package    → explicitly requested
automatic package → installed as a dependency
```

### Use the installed command

I ran:

```bash
tree -L 2 ~/Projects/Learning-Journey
```

The `-L 2` option limited recursion to two directory levels.

The output reported:

```text
8 directories, 15 files
```

### APT history log

High-level APT actions are recorded in:

```text
/var/log/apt/history.log
```

I inspected it with:

```bash
sudo tail -n 25 /var/log/apt/history.log
```

The `tree` installation entry included:

```text
Commandline: apt install tree
Requested-By: artem (1000)
Install: tree:amd64 (2.1.1-2ubuntu3.24.04.2)
```

The log records:

- command line;
- requesting user;
- package action;
- version;
- start and end times.

### Unattended upgrades

Other history entries used:

```text
/usr/bin/unattended-upgrade
```

Ubuntu can automatically apply selected updates through its unattended-upgrade mechanism.

### dpkg log

Low-level package transitions are recorded in:

```text
/var/log/dpkg.log
```

The installation passed through states such as:

```text
half-installed
unpacked
half-configured
installed
```

Temporary intermediate states are normal during package installation.

A problem would exist if a package remained permanently in an incomplete state.

### Inspect files installed by tree

I ran:

```bash
dpkg -L tree
```

The package installed files including:

```text
/usr/bin/tree
/usr/share/doc/tree/README.gz
/usr/share/doc/tree/copyright
/usr/share/man/man1/tree.1.gz
```

### Inspect the executable

I ran:

```bash
ls -lh /usr/bin/tree
file /usr/bin/tree
```

The executable was approximately:

```text
84 KiB
Owner: root
Group: root
Permissions: -rwxr-xr-x
```

The `file` command reported terms such as:

```text
ELF 64-bit
x86-64
PIE executable
dynamically linked
stripped
```

### Executable terminology

```text
ELF                → standard executable format used by Linux
64-bit x86-64      → built for the amd64 architecture
PIE                → position-independent executable
dynamically linked → uses shared libraries
stripped           → unnecessary debugging symbols were removed
```

### Package configuration files for tree

I checked:

```bash
dpkg-query -W \
    -f='Conffiles:\n${Conffiles}\n' \
    tree
```

The result contained no registered conffiles.

This meant that the difference between removing and purging `tree` was very small.

### Runtime library dependencies

I inspected the executable with:

```bash
ldd /usr/bin/tree
```

Important results included:

```text
libc.so.6
ld-linux-x86-64.so.2
linux-vdso.so.1
```

Their roles are:

```text
libc.so.6            → GNU C library used by many Linux programs
ld-linux...          → dynamic loader
linux-vdso.so.1      → virtual kernel-supplied library interface
```

### Dynamic linking

A dynamically linked executable does not contain every required library function internally.

The dynamic loader locates and loads required shared libraries when the program starts.

### Merged /usr filesystem

`ldd` displayed a compatibility path:

```text
/lib/x86_64-linux-gnu/libc.so.6
```

A direct `dpkg -S` lookup did not find that exact path.

I resolved the canonical path with:

```bash
readlink -f PATH
```

Modern Ubuntu uses a merged `/usr` layout in which paths such as:

```text
/lib
/bin
/sbin
```

are compatibility links to locations under:

```text
/usr/lib
/usr/bin
/usr/sbin
```

After resolving the canonical path, `dpkg -S` identified the owning `libc6` package.

### dpkg diversions

The dynamic loader lookup also showed a `dpkg` diversion related to the merged `/usr` transition.

A diversion tells `dpkg` that a path has been redirected so another file can safely occupy or manage its original location.

### Download a package without installing it

I created a temporary directory with:

```bash
mktemp -d /tmp/lesson16-package-XXXXXX
```

Then I downloaded the package archive:

```bash
apt download tree
```

This downloaded a `.deb` file without installing it.

The archive was owned by my normal user because `apt download` did not run with `sudo`.

### Inspect a .deb archive

I inspected package metadata with:

```bash
dpkg-deb --info package.deb
```

and:

```bash
dpkg-deb --field \
    package.deb \
    Package Version Architecture Depends
```

Important fields included:

```text
Package: tree
Version: 2.1.1-2ubuntu3.24.04.2
Architecture: amd64
Depends: libc6 (>= 2.38)
```

### Inspect files inside a .deb

I ran:

```bash
dpkg-deb --contents package.deb
```

This displayed archive paths such as:

```text
/usr/bin/tree
/usr/share/doc/tree/
usr/share/man/man1/tree.1.gz
```

Important distinction:

```text
dpkg-deb --contents PACKAGE.deb → files inside an archive
dpkg -L PACKAGE                 → files registered for an installed package
```

### Package control archive

The `.deb` control information included files such as:

```text
control
md5sums
```

`control` stores package metadata.

`md5sums` stores checksums for packaged files.

### Archive ownership

The `.deb` archive recorded installed system files as:

```text
root:root
```

When `dpkg` installs the package with administrative privileges, it applies the ownership and permissions stored in the archive.

### Remove versus purge

I simulated:

```bash
apt remove --simulate tree
apt purge --simulate tree
```

The difference is:

```text
remove → remove program files but normally preserve conffiles
purge  → remove program files and package-managed configuration
```

Because `tree` had no registered conffiles, the practical difference was minimal.

### Remove tree with APT

I removed the package with:

```bash
sudo apt remove tree
```

APT freed approximately:

```text
111 kB
```

After removal:

```text
Installed: (none)
Candidate: 2.1.1-2ubuntu3.24.04.2
```

The package was absent from the system but remained available from the repositories.

### Purge after removal

I then ran:

```bash
sudo apt purge tree
```

APT reported that the package was not installed.

The package had no remaining configuration files to purge.

### Bash command-path cache

After removal, this command temporarily returned:

```text
/usr/bin/tree
```

even though the executable no longer existed:

```bash
command -v tree
```

Bash had cached the command path in its command hash table.

This was not related to the Git repository or current directory.

### Inspect and clear the Bash command cache

Useful Bash commands include:

```bash
hash
hash -t COMMAND
hash -d COMMAND
hash -r
```

Their meanings are:

```text
hash             → display cached command paths
hash -t COMMAND  → show one cached path
hash -d COMMAND  → remove one cached entry
hash -r          → clear the complete command cache
```

After removing `tree`, trying the stale path returned exit status:

```text
127
```

After:

```bash
hash -r
```

`command -v tree` correctly returned status `1`.

### Package-system health checks

I ran:

```bash
dpkg --audit
```

A healthy result produced no warning and exit status:

```text
0
```

I also ran:

```bash
sudo apt-get check
```

This verified dependency consistency and returned:

```text
0
```

Without `sudo`, `apt-get check` could not acquire the frontend package lock and returned status `100`.

That error was caused by insufficient privileges, not broken dependencies.

### Simulate autoremove

I inspected:

```bash
apt autoremove --simulate
```

APT proposed removing:

```text
libfwupd2
libwoff1
nvidia-firmware-580-580.95.05
```

Nothing was removed because this was only a simulation.

### What autoremove means

`autoremove` removes installed packages that:

- were marked automatic;
- were originally installed as dependencies;
- are no longer required by a manually installed package.

An automatic classification does not automatically prove that removal is desirable.

Critical packages must be investigated first.

### Investigate automatic packages

I confirmed the candidates with:

```bash
apt-mark showauto
```

All three candidates were marked automatic.

I also inspected:

- installed versions;
- descriptions;
- reverse dependencies;
- current package dependency fields;
- related NVIDIA packages;
- the active NVIDIA driver.

### Dependency versus reverse dependency

```text
dependency         → a package required by the current package
reverse dependency → another package that requires the current package
```

I used:

```bash
apt-cache rdepends --installed PACKAGE
```

for reverse-dependency inspection.

I also inspected exact installed package records with:

```bash
dpkg-query -W -f='${Depends}\n' PACKAGE
```

Installed package metadata is more useful than a general repository relationship when checking the current system state.

### libfwupd2 investigation

The current installed `fwupd` package depended on:

```text
libfwupd3
```

It did not depend on the older:

```text
libfwupd2
```

APT therefore classified `libfwupd2` as no longer required.

### libwoff1 investigation

Current installed WebKit package records did not list `libwoff1` in their required dependencies.

APT classified it as an orphaned automatic dependency.

### NVIDIA package investigation

The installed packages included:

```text
nvidia-driver-550
nvidia-driver-580
nvidia-firmware-580-580.159.03
nvidia-firmware-580-580.95.05
nvidia-utils-580
```

I found:

```text
nvidia-driver-550
Depends: nvidia-driver-580
```

This showed that `nvidia-driver-550` was a transitional package leading to the current 580 driver stack.

### Current and old NVIDIA firmware

Two firmware revisions were installed:

```text
580.159.03 → current revision
580.95.05  → older revision
```

The current driver depended on the `580.159.03` package.

The older `580.95.05` package had no displayed installed reverse dependencies and was proposed for automatic removal.

I still did not remove it during the lesson.

### Verify the active NVIDIA driver

I ran:

```bash
nvidia-smi \
    --query-gpu=name,driver_version \
    --format=csv,noheader
```

The result was:

```text
NVIDIA GeForce GTX 1060 3GB, 580.159.03
```

Exit status was:

```text
0
```

The running driver matched the current version-580 package stack.

### Safe autoremove procedure

A safe process is:

```text
1. Simulate autoremove.
2. Inspect every proposed package.
3. Check dependencies and reverse dependencies.
4. Pay special attention to drivers, firmware, kernels, and services.
5. Verify currently active versions.
6. Run the real operation only after confirming safety.
```

I did not run a real `autoremove`.

### Held packages

I checked:

```bash
apt-mark showhold
```

The command succeeded but printed no package names.

This meant no packages were held.

A package hold prevents normal automatic upgrading of that package.

### Phased updates

The available `snapd` version showed:

```text
2.76+ubuntu24.04
phased 40%
```

Ubuntu was releasing the update gradually.

The normal upgrade simulation reported:

```text
The following upgrades have been deferred due to phasing:
  snapd
```

`deferred` means postponed or delayed.

### Why phased updates exist

A phased update is initially delivered to only part of the user population.

This gives maintainers time to detect problems before sending the update to every system.

The `snapd` package was not deferred because of:

- broken dependencies;
- a package hold;
- a package-manager error.

It was deferred because of the phased rollout.

### Simulate normal and full upgrades

I ran:

```bash
apt upgrade --simulate
apt full-upgrade --simulate
```

Both deferred `snapd` because of phasing.

The general difference is:

```text
apt upgrade      → upgrades packages while normally avoiding removals
apt full-upgrade → may install or remove packages to resolve dependency changes
```

Both plans should be inspected carefully on servers and production systems.

### Explicit package upgrade simulation

I ran:

```bash
apt install --simulate --only-upgrade snapd
```

Because I explicitly requested the installed package, APT included the phased candidate in the plan.

`--only-upgrade` means:

> Upgrade the package only if it is already installed; do not install it as a new package.

### Temporarily include phased updates

I simulated:

```bash
apt-get \
    --simulate \
    -o APT::Get::Always-Include-Phased-Updates=true \
    upgrade
```

This temporarily included the phased `snapd` update.

The `-o` setting affected only that command and did not permanently modify APT configuration.

### Package architectures

I checked:

```bash
dpkg --print-architecture
dpkg --print-foreign-architectures
```

The results were:

```text
Main architecture:    amd64
Foreign architecture: i386
```

`i386` support allows selected 32-bit packages and libraries to coexist on the 64-bit system.

### APT storage usage

I inspected:

```text
/var/lib/apt/lists
/var/cache/apt/archives
```

Observed usage was approximately:

```text
/var/lib/apt/lists      → 273 MB
/var/cache/apt/archives → 487 MB
```

The package archive cache contained:

```text
218 .deb files
```

### APT archive cache

Downloaded package archives may be retained in:

```text
/var/cache/apt/archives
```

A cached `.deb` archive is not necessarily currently installed.

The cache contained large kernel and NVIDIA package archives.

### tree archive cache check

I searched for:

```text
tree_*.deb
```

in the APT archive cache.

The exact count was:

```text
0
```

`find` can return status `0` even if it finds no matching files, because status `0` only means that the search completed successfully.

Counting results with `wc -l` gave the reliable answer.

### autoremove, autoclean, and clean

These commands perform different tasks:

```text
autoremove → remove installed unused automatic dependencies
autoclean  → remove obsolete cached .deb archives
clean      → remove all cached .deb archives
```

`autoclean` and `clean` do not uninstall software.

### Simulate autoclean

I ran:

```bash
sudo apt-get --simulate autoclean
```

APT displayed obsolete cached archives that a real `autoclean` would remove.

No files were deleted because this was a simulation.

### Simulate clean

I ran:

```bash
sudo apt-get --simulate clean
```

A real `clean` would clear retained `.deb` archives and generated package cache files.

It would not remove installed packages.

No real cache cleanup was performed during the lesson.

### Install a local .deb with dpkg

I downloaded `tree` again and installed the local archive with:

```bash
sudo dpkg -i ./tree_2.1.1-2ubuntu3.24.04.2_amd64.deb
```

The result included:

```text
Unpacking tree
Setting up tree
dpkg installation status: 0
```

The installation succeeded because the required `libc6` dependency was already installed.

### apt install versus dpkg -i

```text
apt install PACKAGE
```

can:

- find packages in repositories;
- download packages;
- calculate dependencies;
- install missing dependencies.

```text
dpkg -i PACKAGE.deb
```

installs the specified local archive but does not download missing dependencies.

### Repair missing dependencies

If `dpkg -i` leaves a package unconfigured because dependencies are missing, APT can often repair the situation with:

```bash
sudo apt-get install --fix-broken
```

APT can then download and configure the required dependency packages.

A local archive can also be installed through APT with:

```bash
sudo apt install ./package.deb
```

This allows APT to resolve dependencies.

### Toggle manual and automatic marks

I experimented with:

```bash
sudo apt-mark auto tree
```

After marking `tree` automatic, the autoremove simulation added it to the proposed removal list because no installed package required it.

I restored the mark with:

```bash
sudo apt-mark manual tree
```

This demonstrated that APT’s manual and automatic marks directly affect autoremove decisions.

### Remove with low-level dpkg

I removed `tree` directly with:

```bash
sudo dpkg --remove tree
```

The result was:

```text
dpkg removal status: 0
```

Afterwards:

```text
Installed: (none)
Candidate: 2.1.1-2ubuntu3.24.04.2
```

The package was removed locally but remained available from the repositories.

### Safe temporary cleanup

I created temporary directories using `mktemp`.

After each exercise, I returned to the repository and removed only the known temporary directory stored in the variable:

```bash
rm -rf "$package_dir"
```

I verified cleanup with:

```bash
test ! -e "$package_dir"
```

The result was:

```text
Temporary-directory cleanup status: 0
```

### Final package verification

At the end of the lesson:

```text
Final tree command status: 1
Executable absent status: 0
```

This confirmed:

- the `tree` command was no longer available;
- `/usr/bin/tree` did not exist.

### Final package-system health

The final checks returned:

```text
Final dpkg audit status: 0
Final APT dependency status: 0
```

The package database was healthy, and no broken dependencies remained.

### Final unchanged operations

During the lesson, I did not perform:

- a real `apt autoremove`;
- a real `apt clean`;
- a real `apt autoclean`;
- the unrelated `snapd` upgrade;
- any forced phased update.

The potentially destructive operations were inspected only through simulations.

### Final Git verification

I checked:

```bash
git status --short
git log -1 --oneline
```

Before adding these notes, the working tree was clean.

The latest previous commit was:

```text
a1cfa3f Complete Linux users, groups, and ownership lesson
```

### Important command summary

```bash
cat /etc/os-release
```

Show distribution information.

```bash
uname -a
```

Show kernel and machine information.

```bash
apt update
```

Refresh local repository indexes.

```bash
apt upgrade
```

Install available package upgrades.

```bash
apt full-upgrade
```

Upgrade packages and allow dependency-related removals when necessary.

```bash
apt search PATTERN
```

Search package names and descriptions.

```bash
apt show PACKAGE
```

Show repository metadata.

```bash
apt-cache policy PACKAGE
```

Show installed, candidate, and available versions.

```bash
apt install --simulate PACKAGE
```

Display an installation plan without applying it.

```bash
apt install PACKAGE
```

Install a package through APT.

```bash
apt install --only-upgrade PACKAGE
```

Upgrade the package only if it is already installed.

```bash
apt download PACKAGE
```

Download a `.deb` archive without installing it.

```bash
apt remove PACKAGE
```

Remove program files while normally preserving conffiles.

```bash
apt purge PACKAGE
```

Remove program files and package-managed configuration.

```bash
apt autoremove --simulate
```

Inspect unused automatic dependencies without removing them.

```bash
apt-get --simulate autoclean
```

Inspect obsolete cached archives.

```bash
apt-get --simulate clean
```

Inspect a complete archive-cache cleanup.

```bash
apt-mark showmanual
```

List manually installed packages.

```bash
apt-mark showauto
```

List automatically installed packages.

```bash
apt-mark manual PACKAGE
```

Mark a package as manually installed.

```bash
apt-mark auto PACKAGE
```

Mark a package as automatically installed.

```bash
apt-mark showhold
```

List held packages.

```bash
dpkg-query -W PACKAGE
```

Query an installed package record.

```bash
dpkg -s PACKAGE
```

Display installed package status.

```bash
dpkg -L PACKAGE
```

List files registered for an installed package.

```bash
dpkg -S PATH
```

Find which installed package owns a path.

```bash
dpkg -i PACKAGE.deb
```

Install a local `.deb` archive.

```bash
dpkg --remove PACKAGE
```

Remove a package using low-level `dpkg`.

```bash
dpkg --audit
```

Check for incomplete package installations.

```bash
dpkg-deb --info PACKAGE.deb
```

Inspect `.deb` package metadata.

```bash
dpkg-deb --field PACKAGE.deb FIELD
```

Display selected metadata fields.

```bash
dpkg-deb --contents PACKAGE.deb
```

List archive contents.

```bash
apt-get check
```

Check dependency consistency.

```bash
apt-get install --fix-broken
```

Ask APT to repair broken dependencies.

```bash
ldd EXECUTABLE
```

Show runtime shared-library dependencies.

```bash
readlink -f PATH
```

Resolve a canonical filesystem path.

```bash
hash -r
```

Clear Bash’s command-path cache.

### Important vocabulary

- package — пакет
- package manager — менеджер пакетів
- package archive — архів пакета
- repository — репозиторій
- package index — індекс пакетів
- dependency — залежність
- reverse dependency — зворотна залежність
- installed version — встановлена версія
- candidate version — запропонована версія
- available version — доступна версія
- upgrade — оновлення
- deferred upgrade — відкладене оновлення
- phased update — поетапне оновлення
- manually installed — встановлений вручну
- automatically installed — встановлений автоматично
- package metadata — метадані пакета
- configuration file — конфігураційний файл
- package cache — кеш пакетів
- obsolete archive — застарілий архів
- local package — локальний пакет
- shared library — спільна бібліотека
- dynamically linked — динамічно скомпонований
- dynamic loader — динамічний завантажувач
- executable — виконуваний файл
- package state — стан пакета
- held package — утримуваний пакет
- package signature — підпис пакета
- third-party repository — сторонній репозиторій
- remove — видалити пакет
- purge — повністю видалити пакет і конфігурацію
- simulate — симулювати
- inspect — перевіряти
- verify — підтверджувати
- package ownership — належність файлу пакету
- broken dependency — пошкоджена залежність
- firmware — мікропрограма
- transitional package — перехідний пакет
- cleanup — очищення
- command cache — кеш команд

### My sentence

I learned how APT and dpkg manage Ubuntu packages, how to inspect repositories and dependencies, and how to simulate, verify, install, remove, and troubleshoot packages safely.
## Lesson 17 — Linux services with systemd and journalctl

Today I learned how Linux starts, stops, supervises, and records the activity of services with systemd and `journalctl`.

I practised:

- inspecting PID 1 and the systemd version;
- checking the overall system state;
- listing running and failed services;
- inspecting real system services;
- reading unit files and systemd properties;
- understanding dependencies and targets;
- filtering structured journal entries;
- investigating time synchronization;
- inspecting socket activation;
- creating safe user services;
- starting, restarting, stopping, enabling, and disabling services;
- intentionally creating and clearing a failed unit;
- cleaning up all temporary lesson resources.

All practical service-management exercises used safe user units without `sudo`.

### Repository verification

Before beginning the lesson, I checked the repository:

```bash
cd ~/Projects/Learning-Journey
git status --short
git log -1 --oneline
```

My first attempt contained a typo:

```text
git status --short
```

Git suggested the correct command:

```text
git status
```

The corrected command produced no output, which meant that the working tree was clean.

The latest commit was:

```text
d806cef (HEAD -> main) Complete Linux package management lesson
```

This confirmed:

```text
Current branch: main
Working tree:   clean
Latest lesson:  Lesson 16
```

### Inspect PID 1

I inspected PID 1 with:

```bash
ps -p 1 -o pid,ppid,user,comm,args
```

The important output was:

```text
PID  PPID  USER  COMMAND  COMMAND
1    0     root  systemd  /sbin/init splash
```

PID 1 is the first userspace process started by the Linux kernel.

On my Ubuntu system, PID 1 is:

```text
systemd
```

`PPID 0` means that the process was started directly by the kernel.

Important distinction:

```text
Linux kernel → starts the first userspace process
systemd      → becomes PID 1 and manages system startup and services
```

### systemd version

I checked:

```bash
systemctl --version | head -n 3
```

The result included:

```text
systemd 255 (255.4-1ubuntu8.16)
```

The long feature line contained items beginning with `+` and `-`.

Their general meaning is:

```text
+FEATURE → included in this systemd build
-FEATURE → not included in this systemd build
```

### Overall system state

I ran:

```bash
systemctl is-system-running
printf 'Exit status: %s\n' "$?"
```

The result was:

```text
running
Exit status: 0
```

`running` means systemd considers the system fully operational.

Possible states include:

```text
running     → system is fully operational
degraded    → system works, but one or more units failed
starting    → system startup is still in progress
maintenance → system is in a maintenance state
```

### What is a unit?

A unit is an object or resource managed by systemd.

Common unit types include:

```text
.service   → service
.socket    → communication socket
.target    → grouped system state
.timer     → timer
.mount     → mount point
.automount → automatic mount
.path      → filesystem-path watcher
.device    → device
.scope     → externally created process group
.slice     → resource-management group
```

A service is only one type of systemd unit.

### What is a service?

A service unit starts, stops, or supervises a program.

Service unit names normally end with:

```text
.service
```

Examples from my system included:

```text
cron.service
NetworkManager.service
systemd-journald.service
systemd-timesyncd.service
```

### What is a daemon?

A daemon is a program that normally runs in the background and provides a system function.

Examples include:

```text
cron
systemd-journald
snapd
```

Important distinction:

```text
daemon  → background program or process
service → systemd unit that manages a program
```

Not every service remains running permanently.

A `oneshot` service can perform one action and exit.

### Loaded, active, running, and enabled

These words describe different properties:

```text
loaded  → systemd successfully read the unit definition
active  → the unit is currently activated
running → the service process is currently executing
enabled → the unit is configured for automatic activation
```

They are not interchangeable.

Examples:

```text
enabled + inactive → automatic activation configured, but stopped now
disabled + active  → started manually, but not configured for autostart
active (exited)    → logically active after its command finished
static + running   → running through dependencies or activation
```

### List running services

I listed running services with:

```bash
systemctl list-units \
    --type=service \
    --state=running \
    --no-pager
```

Examples included:

```text
cron.service
dbus.service
fwupd.service
NetworkManager.service
systemd-journald.service
systemd-logind.service
systemd-resolved.service
systemd-timesyncd.service
systemd-udevd.service
```

I counted running services with:

```bash
systemctl list-units \
    --type=service \
    --state=running \
    --no-legend \
    --no-pager |
wc -l
```

The result was:

```text
34
```

Therefore, 34 service units were running at that moment.

### Check failed system units

I ran:

```bash
systemctl --failed --no-pager
systemctl --failed --no-legend --no-pager | wc -l
```

The result was:

```text
0 loaded units listed.
0
```

There were no failed system-wide units.

### Inspect cron.service

I inspected a real running service:

```bash
systemctl status cron.service --no-pager
```

Important fields included:

```text
Loaded: loaded
Active: active (running)
Main PID: 973 (cron)
```

The service description was:

```text
Regular background program processing daemon
```

The unit file was loaded from:

```text
/usr/lib/systemd/system/cron.service
```

The service was:

```text
enabled
```

Its vendor preset was also:

```text
enabled
```

### Check active and enabled states

I ran:

```bash
systemctl is-active cron.service
printf 'is-active exit status: %s\n' "$?"

systemctl is-enabled cron.service
printf 'is-enabled exit status: %s\n' "$?"
```

The result was:

```text
active
is-active exit status: 0

enabled
is-enabled exit status: 0
```

This confirmed two independent facts:

```text
active  → cron was running at that moment
enabled → cron was configured for automatic activation
```

### Main PID

The status output showed:

```text
Main PID: 973 (cron)
```

Systemd considered PID 973 the main process of the service.

The process command was:

```text
/usr/sbin/cron -f -P
```

The `-f` option keeps cron in the foreground so systemd can supervise it directly.

### Tasks, memory, and CPU

The status output included information such as:

```text
Tasks: 1
Memory: 468.0K
CPU: 187ms
```

These values describe the resources used by the service.

### Control groups

The service belonged to:

```text
/system.slice/cron.service
```

A control group, or cgroup, lets Linux and systemd:

- group related processes;
- track resource usage;
- apply limits;
- stop all related processes when necessary.

### Inspect the cron unit file

I ran:

```bash
systemctl cat cron.service
```

The unit contained three main sections:

```ini
[Unit]
[Service]
[Install]
```

### The [Unit] section

The unit included:

```ini
[Unit]
Description=Regular background program processing daemon
Documentation=man:cron(8)
After=remote-fs.target nss-user-lookup.target
```

Their meanings are:

```text
Description=   → human-readable description
Documentation= → documentation reference
After=         → startup-ordering relationship
```

`After=` controls ordering.

It does not automatically start the named unit.

### The [Service] section

The service section included:

```ini
[Service]
EnvironmentFile=-/etc/default/cron
ExecStart=/usr/sbin/cron -f -P $EXTRA_OPTS
IgnoreSIGPIPE=false
KillMode=process
Restart=on-failure
SyslogFacility=cron
```

Important meanings:

```text
EnvironmentFile=  → read environment variables from a file
ExecStart=         → command used to start the service
Restart=on-failure → restart after an unsuccessful termination
KillMode=process   → target the main process when stopping
SyslogFacility=    → traditional syslog category
```

The leading minus sign in:

```ini
EnvironmentFile=-/etc/default/cron
```

means:

> Continue even if the environment file is missing or cannot be read.

### The [Install] section

The unit contained:

```ini
[Install]
WantedBy=multi-user.target
```

This section is used when the service is enabled.

It tells systemd to connect the service to:

```text
multi-user.target
```

### Inspect machine-readable properties

I ran:

```bash
systemctl show cron.service \
    -p Id \
    -p Description \
    -p LoadState \
    -p ActiveState \
    -p SubState \
    -p UnitFileState \
    -p MainPID \
    -p FragmentPath
```

The output included:

```text
Id=cron.service
Description=Regular background program processing daemon
LoadState=loaded
ActiveState=active
SubState=running
UnitFileState=enabled
MainPID=973
FragmentPath=/usr/lib/systemd/system/cron.service
```

`systemctl show` is useful for scripts because it exposes machine-readable properties.

### systemctl status and recent logs

The bottom of `systemctl status` displayed recent journal entries.

Examples included:

```text
session opened for user root
(root) CMD (...)
session closed for user root
run-parts --report /etc/cron.hourly
```

This showed cron:

1. opening a temporary session;
2. executing a scheduled command;
3. closing the session.

### Inspect logs with journalctl

I ran:

```bash
journalctl -u cron.service \
    -n 15 \
    --no-pager \
    -o short-iso
```

Options:

```text
-u cron.service → select one unit
-n 15           → show the newest 15 entries
--no-pager      → print directly to the terminal
-o short-iso    → use ISO-style timestamps
```

I also filtered by time:

```bash
journalctl -u cron.service \
    --since "30 minutes ago" \
    --no-pager \
    -o short-iso
```

### Journal entry format

A typical entry looked like:

```text
2026-07-24T11:45:01+02:00 artem-A320M-H CRON[11315]: (root) CMD (...)
```

Its fields are:

```text
timestamp
hostname
program or identifier
process ID
message text
```

### Cron journal warning

The journal contained:

```text
cron.service: Referenced but unset environment variable evaluates to an empty string: EXTRA_OPTS
```

The unit file used:

```ini
ExecStart=/usr/sbin/cron -f -P $EXTRA_OPTS
```

I inspected:

```bash
sed -n '1,120p' /etc/default/cron
```

The file contained only comments and did not define:

```text
EXTRA_OPTS
```

Therefore, systemd evaluated it as an empty string.

The effective command was approximately:

```text
/usr/sbin/cron -f -P
```

The warning did not prevent the service from starting.

The service remained:

```text
ActiveState=active
SubState=running
```

No configuration change was made because the service was healthy.

### Deprecated configuration mechanism

`/etc/default/cron` stated that it was deprecated.

It recommended using:

```bash
systemctl edit cron.service
```

or:

```bash
systemctl edit --full cron.service
```

A deprecated mechanism is old and no longer recommended for new configuration.

### Filter logs by priority

I ran:

```bash
journalctl -u cron.service \
    -p warning \
    --since today \
    --no-pager \
    -o short-iso
```

`-p warning` includes warning-level and more serious messages.

Priority order:

```text
emerg
alert
crit
err
warning
notice
info
debug
```

### Search journal messages

I searched by message text:

```bash
journalctl -u cron.service \
    --since today \
    --grep='EXTRA_OPTS' \
    --no-pager \
    -o short-iso
```

The same warning appeared in both command outputs because two different filters selected the same journal entry.

### List recorded boots

I ran:

```bash
journalctl --list-boots --no-pager | tail -n 5
```

Boot indexes included:

```text
0  → current boot
-1 → previous boot
-2 → two boots ago
```

Each boot also had a unique boot ID.

### Filter logs by boot

I inspected current-boot cron entries with:

```bash
journalctl -u cron.service \
    -b 0 \
    -n 10 \
    --no-pager \
    -o short-iso
```

`-b 0` means:

```text
current boot
```

### Current kernel boot ID

I ran:

```bash
cat /proc/sys/kernel/random/boot_id
```

The result was:

```text
427a7ac8-366f-4e1d-96f8-99cc115ae12e
```

This matched the current boot ID displayed by `journalctl --list-boots`.

### Monotonic timestamps

I inspected:

```bash
journalctl -u cron.service \
    -b 0 \
    -n 12 \
    --no-pager \
    -o short-monotonic
```

The timestamps looked like:

```text
[ 7158.257134]
[ 7758.276197]
[ 8358.292027]
[ 8958.307741]
```

A monotonic timestamp counts elapsed time since boot.

It always moves forward and is not affected when the calendar clock changes.

The cron entries were approximately:

```text
600 seconds = 10 minutes
```

apart.

This confirmed normal chronological order.

### Wall clock and monotonic clock

```text
wall clock      → calendar time displayed to users
monotonic clock → elapsed time since boot
```

The wall clock can be corrected forward or backward.

The monotonic clock always moves forward during the boot.

### Inspect time synchronization

I ran:

```bash
timedatectl status
timedatectl timesync-status
```

Important output included:

```text
Time zone: Europe/Warsaw (CEST, +0200)
System clock synchronized: yes
NTP service: active
RTC in local TZ: no
```

The hardware clock used UTC, which is normal for Linux.

### Inspect systemd-timesyncd logs

I ran:

```bash
journalctl -u systemd-timesyncd.service \
    -b 0 \
    -n 20 \
    --no-pager \
    -o short-monotonic
```

The service contacted an Ubuntu NTP server.

The initial clock synchronization happened approximately 36 seconds after boot.

The wall clock was corrected backward by almost two hours.

### Journal rotation after the clock correction

`systemd-journald` recorded:

```text
Time jumped backwards, rotating.
```

This confirmed the clock correction.

Journal rotation means journald closes the current journal file and begins using another one.

The status command also showed:

```text
journal has been rotated since unit was started
```

This did not mean the journal service failed.

### Default target

I ran:

```bash
systemctl get-default
```

The result was:

```text
graphical.target
```

A target groups units to represent a system state.

A simplified relationship is:

```text
graphical.target
└─ multi-user.target
   └─ cron.service
```

### Inspect dependencies

I ran:

```bash
systemctl list-dependencies cron.service --no-pager
```

The output included units such as:

```text
system.slice
sysinit.target
systemd-journald.service
systemd-udevd.service
local-fs.target
```

The command is recursive by default.

It shows dependencies of dependencies.

### Reverse dependencies

I ran:

```bash
systemctl list-dependencies \
    --reverse \
    cron.service \
    --no-pager
```

The reverse tree showed:

```text
cron.service
└─ multi-user.target
   └─ graphical.target
```

A reverse dependency answers:

> Which units depend on or include this unit?

### Requires, Wants, After, and Before

I inspected:

```bash
systemctl show cron.service \
    -p Requires \
    -p Wants \
    -p After \
    -p Before
```

The output included:

```text
Requires=sysinit.target system.slice
Wants=
Before=shutdown.target multi-user.target
After=basic.target systemd-journald.socket sysinit.target remote-fs.target system.slice nss-user-lookup.target
```

Their meanings are:

```text
Requires= → strong requirement relationship
Wants=    → weaker requirement relationship
After=    → ordering: start after
Before=   → ordering: start before
```

Requirement dependencies and ordering dependencies are different.

`After=` does not automatically start another unit.

### WantedBy and RequiredBy

I inspected:

```bash
systemctl show cron.service \
    -p WantedBy \
    -p RequiredBy
```

The result included:

```text
WantedBy=multi-user.target
RequiredBy=
```

This means:

```text
multi-user.target wants cron.service
```

It does not mean that cron wants `multi-user.target`.

### Enablement symlink

I inspected:

```bash
ls -l \
    /etc/systemd/system/multi-user.target.wants/cron.service
```

The symlink pointed to:

```text
/usr/lib/systemd/system/cron.service
```

I confirmed the final path with:

```bash
readlink -f \
    /etc/systemd/system/multi-user.target.wants/cron.service
```

This symlink is the filesystem representation of the enablement relationship.

### Compare unit-file states

I ran:

```bash
systemctl list-unit-files \
    cron.service \
    systemd-journald.service \
    systemd-timesyncd.service \
    --no-pager
```

The states included:

```text
cron.service              enabled
systemd-journald.service  static
systemd-timesyncd.service enabled
```

### Static units

A static unit normally has no regular enablement instructions in an `[Install]` section.

It is activated through:

- dependencies;
- socket activation;
- timer activation;
- path activation;
- another unit.

Static does not mean:

```text
stopped
broken
failed
unusable
```

### Inspect systemd-journald

I ran:

```bash
systemctl status systemd-journald.service \
    --no-pager \
    -l
```

The service was:

```text
Loaded: loaded (...; static)
Active: active (running)
Main PID: 359
```

This demonstrated:

```text
static + active (running)
```

A static service can run normally.

### Journald triggers

I inspected:

```bash
systemctl show systemd-journald.service \
    -p TriggeredBy \
    -p WantedBy \
    -p RequiredBy
```

The triggers included:

```text
systemd-journald.socket
systemd-journald-audit.socket
systemd-journald-dev-log.socket
```

A trigger is a mechanism or event that can activate another unit.

### Socket activation

With socket activation, systemd can:

```text
1. Create and listen on a socket.
2. Wait for data or a connection.
3. Start the associated service when necessary.
4. Pass communication to the service.
```

The socket can exist before the service process starts.

### Journald socket states

The output showed:

```text
systemd-journald.socket         active
systemd-journald-dev-log.socket active
systemd-journald-audit.socket   inactive
```

The inactive audit socket was not a failure.

The journal stated:

```text
Collecting audit messages is disabled.
```

### Drop-in configuration

The journald status showed a package-provided drop-in:

```text
/usr/lib/systemd/system/systemd-journald.service.d/nice.conf
```

A drop-in is an additional configuration fragment.

Package-provided configuration commonly lives under:

```text
/usr/lib/systemd/system/
```

Local administrator overrides normally live under:

```text
/etc/systemd/system/
```

### Runtime and persistent journals

Journald reported:

```text
Runtime Journal (/run/log/journal/...)
System Journal  (/var/log/journal/...)
```

Their general roles are:

```text
/run/log/journal → runtime journal storage
/var/log/journal → persistent journal storage
```

Persistent logs can survive reboots.

### List journald sockets

I ran:

```bash
systemctl list-sockets --all --no-pager |
grep 'systemd-journald'
```

The output connected:

```text
listening endpoint
socket unit
activated service
```

Important paths included:

```text
/run/systemd/journal/dev-log
/run/systemd/journal/socket
/run/systemd/journal/stdout
```

### Inspect socket properties

I ran:

```bash
systemctl show \
    systemd-journald.socket \
    systemd-journald-dev-log.socket \
    systemd-journald-audit.socket \
    -p Id \
    -p LoadState \
    -p ActiveState \
    -p SubState \
    -p Triggers
```

The main sockets were:

```text
LoadState=loaded
ActiveState=active
SubState=running
Triggers=systemd-journald.service
```

The audit socket was:

```text
LoadState=loaded
ActiveState=inactive
SubState=dead
Triggers=systemd-journald.service
```

### Inspect socket unit files

I ran:

```bash
systemctl cat systemd-journald.socket
systemctl cat systemd-journald-dev-log.socket
```

Important directives included:

```ini
DefaultDependencies=no
Before=sockets.target
IgnoreOnIsolate=yes
```

These socket units must be available very early during startup.

### ListenDatagram and ListenStream

The main socket unit included:

```ini
ListenDatagram=/run/systemd/journal/socket
ListenStream=/run/systemd/journal/stdout
```

A datagram socket transfers separate messages.

A stream socket transfers a continuous byte stream.

### Process credentials and security information

The socket unit included:

```ini
PassCredentials=yes
PassSecurity=yes
```

This allows journald to receive sender information such as:

```text
PID
UID
GID
security context
```

### Socket buffers

The configuration included:

```ini
ReceiveBuffer=8M
SendBuffer=8M
```

A buffer is temporary kernel memory used while data waits to be processed.

### Associated service

The socket unit included:

```ini
Service=systemd-journald.service
```

This connects socket activity to the journald service.

### Socket permissions

The configuration included:

```ini
SocketMode=0666
```

The permission form is:

```text
rw-rw-rw-
```

For a socket, these permissions control access to the communication endpoint.

### Timestamp precision

The socket unit included:

```ini
Timestamping=us
```

`us` means microseconds.

```text
1 microsecond = 0.000001 second
```

### /dev/log compatibility

The dev-log unit contained:

```ini
ListenDatagram=/run/systemd/journal/dev-log
Symlinks=/dev/log
```

This provides compatibility with programs that send traditional syslog messages to:

```text
/dev/log
```

### Inspect actual socket files

I ran:

```bash
ls -l \
    /dev/log \
    /run/systemd/journal/dev-log \
    /run/systemd/journal/socket \
    /run/systemd/journal/stdout
```

The result showed:

```text
/dev/log -> /run/systemd/journal/dev-log
```

`/dev/log` was a symbolic link.

The actual socket entries began with:

```text
s
```

in the `ls -l` output.

### Resolve /dev/log

I ran:

```bash
readlink -f /dev/log
```

The result was:

```text
/run/systemd/journal/dev-log
```

### Inspect Unix-domain sockets

I ran:

```bash
ss -lx | grep '/run/systemd/journal'
```

The output included:

```text
u_dgr UNCONN
u_str LISTEN
```

Their meanings are:

```text
u_dgr  → Unix datagram socket
u_str  → Unix stream socket
UNCONN → connectionless datagram state
LISTEN → ready to accept stream connections
```

### Send a safe test journal message

I created a unique identifier:

```bash
lesson_tag="lesson17-artem-$(date +%s)"
```

Then I sent one harmless message:

```bash
logger --tag "$lesson_tag" \
    "Safe Lesson 17 test message through /dev/log"
```

I retrieved it with:

```bash
journalctl -t "$lesson_tag" \
    --no-pager \
    -o short-iso
```

The result contained:

```text
Safe Lesson 17 test message through /dev/log
```

No configuration or service was modified.

### Command substitution

The tag used:

```bash
$(date +%s)
```

This is command substitution.

It inserts the output of a command into another command or assignment.

`date +%s` returns seconds since the Unix epoch.

### Inspect verbose journal metadata

I ran:

```bash
journalctl -t "$lesson_tag" \
    -n 1 \
    --no-pager \
    -o verbose
```

Important fields included:

```text
_UID=1000
_GID=1000
_PID=12914
_COMM=logger
_TRANSPORT=syslog
SYSLOG_IDENTIFIER=lesson17-artem-...
PRIORITY=5
SYSLOG_FACILITY=1
MESSAGE=Safe Lesson 17 test message through /dev/log
_BOOT_ID=...
_MACHINE_ID=...
_HOSTNAME=artem-A320M-H
```

### Structured journal fields

Journald stores structured metadata in addition to message text.

This allows filtering by:

```text
unit
boot
process
user
priority
transport
identifier
message
```

### Confirm the syslog transport

The field:

```text
_TRANSPORT=syslog
```

confirmed that journald received the test message through the syslog-compatible path.

The path was:

```text
logger
→ /dev/log
→ systemd-journald-dev-log.socket
→ systemd-journald.service
→ journal entry
```

### Journal priorities

The test message had:

```text
PRIORITY=5
```

Priority 5 means:

```text
notice
```

Priority numbers:

```text
0 emerg
1 alert
2 crit
3 err
4 warning
5 notice
6 info
7 debug
```

### Exact structured-field filtering

I ran:

```bash
journalctl \
    SYSLOG_IDENTIFIER="$lesson_tag" \
    _TRANSPORT=syslog \
    -n 1 \
    --no-pager \
    -o short-iso
```

Different field conditions are combined with logical AND.

The journal entry had to match both conditions.

### Show only the message body

I ran:

```bash
journalctl \
    SYSLOG_IDENTIFIER="$lesson_tag" \
    -n 1 \
    --no-pager \
    -o cat
```

The output was only:

```text
Safe Lesson 17 test message through /dev/log
```

`-o cat` removes timestamps and displayed metadata.

### List transport values

I ran:

```bash
journalctl -b 0 \
    -F _TRANSPORT \
    --no-pager |
sort
```

The result included:

```text
driver
journal
kernel
stdout
syslog
```

Their meanings are:

```text
driver  → internal journald messages
journal → native journal protocol
kernel  → Linux kernel messages
stdout  → captured standard output or error
syslog  → traditional syslog-compatible messages
```

### Compare journal transports

I ran:

```bash
journalctl -b 0 _TRANSPORT=kernel -n 3 \
    --no-pager \
    -o short-iso

journalctl -b 0 _TRANSPORT=stdout -n 3 \
    --no-pager \
    -o short-iso

journalctl -b 0 _TRANSPORT=syslog -n 3 \
    --no-pager \
    -o short-iso
```

The transport field describes how a message reached journald.

It is separate from the message priority.

### Kernel transport example

Kernel messages included AppArmor audit denials for the Firefox Snap profile.

A security denial does not automatically mean the entire application or a systemd unit failed.

### Standard-output examples

Captured output included messages from:

```text
gnome-shell
gdm-session-worker
tracker-miner-fs-3
```

One known local warning referenced:

```text
/etc/modprobe.d/blacklist-aic8800.conf
```

I intentionally skipped further inspection because I already knew that the file was related to an old Wi-Fi adapter.

### Syslog transport examples

Syslog entries included messages from:

```text
CRON
PackageKit
```

Words such as `ERROR`, `warning`, or `daemon quit` inside message text do not automatically prove that a unit failed.

The actual unit state should be checked with:

```bash
systemctl status UNIT
systemctl is-active UNIT
systemctl is-failed UNIT
systemctl --failed
```

### System and user service managers

There are two important service-manager contexts:

```text
systemctl        → system-wide manager, PID 1
systemctl --user → current user’s service manager
```

System units commonly live under:

```text
/usr/lib/systemd/system/
/etc/systemd/system/
```

User units commonly live under:

```text
~/.config/systemd/user/
```

### Create a transient user service

I created a safe transient user service:

```bash
demo_unit="lesson17-demo"

systemd-run --user \
    --unit="$demo_unit" \
    --description="Lesson 17 temporary demo service" \
    --collect \
    /bin/bash -c \
    'echo "Lesson 17 demo service started"; sleep 120'
```

The unit name was:

```text
lesson17-demo.service
```

### Transient unit

The status output showed:

```text
Transient: yes
```

The temporary definition was stored under:

```text
/run/user/1000/systemd/transient/
```

A transient unit is created at runtime instead of being stored as a permanent configuration file.

### Transient service state

The service became:

```text
active (running)
```

Its main process was:

```text
sleep 120
```

The `echo` output was captured in the user journal.

### User-service cgroup

The service appeared under:

```text
/user.slice/user-1000.slice/user@1000.service/app.slice/
```

This confirmed that it belonged to my user systemd manager.

### Transient-unit cleanup

After the process completed, `--collect` allowed systemd to remove the temporary unit definition.

Later checks showed:

```text
inactive
Unit lesson17-demo.service could not be found.
```

The historical journal entries were still available.

### Create a file-based user service

I created:

```text
~/.config/systemd/user/lesson17-practice.service
```

The unit contained:

```ini
[Unit]
Description=Lesson 17 safe practice service

[Service]
Type=simple
ExecStart=/usr/bin/sleep 600
```

### Type=simple

For a `simple` service, systemd considers startup successful when it starts the process from:

```ini
ExecStart=
```

It does not wait for an additional readiness notification.

### Verify the unit file

I ran:

```bash
systemd-analyze --user verify "$practice_file"
```

The result was:

```text
verify exit status: 0
```

The unit definition was valid.

### Reload unit definitions

I ran:

```bash
systemctl --user daemon-reload
```

`daemon-reload` makes the service manager reread unit files.

It does not restart running services.

### Loaded but inactive

Before starting, the service was:

```text
Loaded: loaded
Active: inactive (dead)
```

Its unit-file state was:

```text
static
```

because it had no `[Install]` section.

It could still be started manually.

### Start the practice service

I ran:

```bash
systemctl --user start lesson17-practice.service
```

The result was:

```text
start exit status: 0
active
is-active exit status: 0
```

The service became:

```text
active (running)
```

Its main process was:

```text
/usr/bin/sleep 600
```

### Restart the service

I saved the original PID, restarted the service, and checked the new PID.

The results were:

```text
Old PID: 13971
New PID: 14005
```

This proved that restart performed a real stop-and-start operation.

### Stop the service

I ran:

```bash
systemctl --user stop lesson17-practice.service
```

The result was:

```text
stop exit status: 0
inactive
is-active exit status: 3
```

A `ps` lookup of the old PID found no process.

The final properties included:

```text
Result=success
ExecMainCode=0
ExecMainStatus=0
ActiveState=inactive
SubState=dead
```

### Service lifecycle in the journal

The user journal showed:

```text
Started lesson17-practice.service
Stopping lesson17-practice.service
Stopped lesson17-practice.service
Started lesson17-practice.service
Stopping lesson17-practice.service
Stopped lesson17-practice.service
```

The restart appeared as:

```text
stop → stopped → start
```

### Create an intentional failure

I created:

```text
~/.config/systemd/user/lesson17-failure.service
```

The unit contained:

```ini
[Unit]
Description=Lesson 17 intentional failure demo

[Service]
Type=oneshot
ExecStart=/usr/bin/false
```

`/usr/bin/false` does nothing harmful and returns exit status `1`.

### Valid configuration with a failing command

The verification result was:

```text
verify exit status: 0
```

This demonstrated:

```text
valid unit syntax ≠ successful runtime execution
```

The unit file was valid, but its command was intentionally unsuccessful.

### Failed service state

Starting the unit returned:

```text
start exit status: 1
```

The status showed:

```text
Active: failed
Result: exit-code
status=1/FAILURE
```

The journal sequence included:

```text
Starting ...
Main process exited, code=exited, status=1/FAILURE
Failed with result 'exit-code'.
Failed to start ...
```

### Inspect failed user units

I ran:

```bash
systemctl --user --failed --no-pager
```

The output listed:

```text
lesson17-failure.service
```

I checked:

```bash
systemctl --user is-failed lesson17-failure.service
```

The result was:

```text
failed
is-failed exit status: 0
```

For `is-failed`, exit status `0` means the unit is currently recorded as failed.

### Failure properties

I inspected:

```bash
systemctl --user show lesson17-failure.service \
    -p ActiveState \
    -p SubState \
    -p Result \
    -p ExecMainCode \
    -p ExecMainStatus
```

The result included:

```text
Result=exit-code
ExecMainCode=1
ExecMainStatus=1
ActiveState=failed
SubState=failed
```

`ExecMainStatus=1` was the exit status returned by `/usr/bin/false`.

### Clear the failed state

I ran:

```bash
systemctl --user reset-failed lesson17-failure.service
```

The result was:

```text
reset-failed exit status: 0
```

The unit returned to:

```text
inactive (dead)
```

Historical failure messages remained in the journal.

### Repair the oneshot service

I changed:

```ini
ExecStart=/usr/bin/false
```

to:

```ini
ExecStart=/usr/bin/true
```

The repaired unit started successfully:

```text
start exit status: 0
```

The journal showed:

```text
Starting lesson17-failure.service
Finished lesson17-failure.service
```

### Successful oneshot without RemainAfterExit

The repaired service used:

```ini
Type=oneshot
ExecStart=/usr/bin/true
```

It did not contain:

```ini
RemainAfterExit=yes
```

Therefore, after completing successfully, it returned to:

```text
inactive (dead)
```

Its final properties included:

```text
Result=success
ExecMainCode=0
ExecMainStatus=0
ActiveState=inactive
SubState=dead
```

An inactive oneshot service can still have a successful result.

### Clean up the practice units

I removed:

```text
~/.config/systemd/user/lesson17-practice.service
~/.config/systemd/user/lesson17-failure.service
```

Then I ran:

```bash
systemctl --user daemon-reload
systemctl --user reset-failed
```

Verification showed:

```text
0 matching unit files
0 loaded lesson units
0 failed user units
```

### Create an enablement practice service

I created:

```text
~/.config/systemd/user/lesson17-enable-demo.service
```

The definition was:

```ini
[Unit]
Description=Lesson 17 enablement practice service

[Service]
Type=oneshot
ExecStart=/usr/bin/true
RemainAfterExit=yes

[Install]
WantedBy=default.target
```

### RemainAfterExit=yes

`RemainAfterExit=yes` means:

> Keep the unit logically active after `ExecStart` finishes successfully.

The expected state is:

```text
active (exited)
```

No main process remains running, but systemd remembers the unit as active.

### User default.target

The unit contained:

```ini
WantedBy=default.target
```

For the user systemd manager, `default.target` represents its normal startup target.

### Initial state

Before enabling or starting, the unit was:

```text
disabled + inactive
```

The status also showed:

```text
preset: enabled
```

A preset is a recommendation.

It is not the same as the current state.

### Enable without starting

I ran:

```bash
systemctl --user enable lesson17-enable-demo.service
```

Systemd created:

```text
~/.config/systemd/user/default.target.wants/lesson17-enable-demo.service
```

The symlink pointed to the original unit file.

The resulting state was:

```text
enabled + inactive
```

This proved that enabling did not start the service.

### Start the enabled service

I ran:

```bash
systemctl --user start lesson17-enable-demo.service
```

The resulting state was:

```text
enabled + active (exited)
```

The command finished successfully, and `RemainAfterExit=yes` kept the unit logically active.

### Stop without disabling

I ran:

```bash
systemctl --user stop lesson17-enable-demo.service
```

The resulting state was:

```text
enabled + inactive
```

The automatic-activation symlink still existed.

This proved that stopping does not disable a service.

### Disable the service

I ran:

```bash
systemctl --user disable lesson17-enable-demo.service
```

Systemd removed the symlink under:

```text
default.target.wants/
```

The resulting state was:

```text
disabled + inactive
```

The original unit file still existed.

### Start without enabling

I started the disabled service manually:

```bash
systemctl --user start lesson17-enable-demo.service
```

The result was:

```text
disabled + active (exited)
```

This proved that a disabled service can be started manually.

### Important enablement combinations

I observed:

```text
disabled + inactive
enabled  + inactive
enabled  + active
disabled + active
```

Their meanings are:

```text
disabled + inactive → not automatic and not active now
enabled + inactive  → automatic later, but stopped now
enabled + active    → automatic later and active now
disabled + active   → manually active now, not automatic later
```

### enable --now

Systemd can enable and start a unit in one command:

```bash
systemctl --user enable --now UNIT
```

I intentionally performed `enable` and `start` separately so I could observe the difference.

### Final cleanup

I stopped the enablement demo service, removed its unit file, reloaded the user manager, and reset failure state.

Final verification showed:

```text
0 lesson17 unit files
0 loaded lesson17 units
0 failed user units
```

### Final system health

I ran:

```bash
systemctl is-system-running
printf 'system state exit status: %s\n' "$?"

systemctl --failed --no-pager
systemctl --user --failed --no-pager
```

The results were:

```text
running
system state exit status: 0
0 failed system units
0 failed user units
```

The system remained healthy after all exercises.

### Final Git verification

I ran:

```bash
git status --short
```

The command produced no output.

This confirmed:

- all temporary lesson resources were removed;
- no unintended repository files were created;
- the working tree was clean before adding Lesson 17 notes.

### Important command summary

```bash
ps -p 1 -o pid,ppid,user,comm,args
```

Inspect PID 1.

```bash
systemctl --version
```

Show the systemd version and compiled features.

```bash
systemctl is-system-running
```

Show the overall systemd state.

```bash
systemctl list-units --type=service --state=running
```

List running services.

```bash
systemctl --failed
```

List failed system-wide units.

```bash
systemctl --user --failed
```

List failed user units.

```bash
systemctl status UNIT
```

Show a human-readable unit status.

```bash
systemctl show UNIT -p PROPERTY
```

Show selected machine-readable properties.

```bash
systemctl cat UNIT
```

Display a unit definition and its drop-ins.

```bash
systemctl is-active UNIT
```

Check the current activation state.

```bash
systemctl is-enabled UNIT
```

Check the automatic-activation configuration.

```bash
systemctl is-failed UNIT
```

Check whether a unit is recorded as failed.

```bash
systemctl start UNIT
```

Start a unit now.

```bash
systemctl stop UNIT
```

Stop a unit now.

```bash
systemctl restart UNIT
```

Stop and start a unit.

```bash
systemctl enable UNIT
```

Configure automatic activation.

```bash
systemctl disable UNIT
```

Remove automatic-activation links.

```bash
systemctl enable --now UNIT
```

Enable and start a unit in one command.

```bash
systemctl daemon-reload
```

Make the system manager reread unit definitions.

```bash
systemctl --user daemon-reload
```

Make the user manager reread user unit definitions.

```bash
systemctl reset-failed UNIT
```

Clear a recorded failed state.

```bash
systemctl list-unit-files
```

List unit files and enablement states.

```bash
systemctl list-dependencies UNIT
```

Show dependency relationships below a unit.

```bash
systemctl list-dependencies --reverse UNIT
```

Show units that depend on the selected unit.

```bash
systemctl get-default
```

Show the default system target.

```bash
journalctl -u UNIT
```

Show journal entries for one unit.

```bash
journalctl -u UNIT -n NUMBER
```

Show the newest matching entries.

```bash
journalctl -u UNIT --since "TIME"
```

Filter a unit’s journal by time.

```bash
journalctl -b 0
```

Show entries from the current boot.

```bash
journalctl --list-boots
```

List recorded boots.

```bash
journalctl -p warning
```

Show warning-level and more serious entries.

```bash
journalctl --grep='PATTERN'
```

Search journal message text.

```bash
journalctl -o short-iso
```

Display ISO-style timestamps.

```bash
journalctl -o short-monotonic
```

Display elapsed time since boot.

```bash
journalctl -o verbose
```

Display structured journal metadata.

```bash
journalctl -o cat
```

Display only message bodies.

```bash
journalctl FIELD=value
```

Filter by an exact journal-field value.

```bash
journalctl -F FIELD
```

List values present in a journal field.

```bash
journalctl --user-unit=UNIT
```

Show journal entries for a user unit.

```bash
timedatectl status
```

Show time, timezone, and synchronization state.

```bash
timedatectl timesync-status
```

Show detailed NTP synchronization information.

```bash
systemctl list-sockets --all
```

List socket units and listening endpoints.

```bash
ss -lx
```

List listening Unix-domain sockets.

```bash
logger --tag TAG "MESSAGE"
```

Send a syslog-compatible message to the local journal.

```bash
systemd-run --user --unit=NAME --collect COMMAND
```

Create and run a transient user service.

```bash
systemd-analyze --user verify FILE
```

Verify a user unit file.

```bash
readlink -f PATH
```

Resolve a symbolic link to its final path.

### Important vocabulary

- systemd — менеджер системи та служб
- init system — система ініціалізації
- PID 1 — перший userspace-процес
- unit — юніт, об’єкт systemd
- service — служба
- daemon — фоновий системний процес
- unit file — файл визначення юніта
- unit-file state — стан файла юніта
- loaded — завантажений
- active — активний
- inactive — неактивний
- running — виконується
- exited — процес завершився
- dead — процес юніта не виконується
- failed — стан помилки
- enabled — увімкнений для автоматичної активації
- disabled — вимкнений для автоматичної активації
- static unit — статичний юніт
- preset — типовий рекомендований стан
- vendor preset — рекомендований стан від дистрибутива
- target — цільовий юніт
- default target — типова ціль
- graphical target — ціль графічного режиму
- multi-user target — ціль багатокористувацького режиму
- dependency — залежність
- reverse dependency — зворотна залежність
- requirement dependency — залежність необхідності
- ordering dependency — залежність порядку
- Requires — сильна залежність
- Wants — слабша залежність
- After — запускати після
- Before — запускати перед
- WantedBy — залучається цільовим юнітом
- RequiredBy — сильно вимагається іншим юнітом
- pull in a unit — залучити юніт
- implicit dependency — неявна залежність
- recursive dependency tree — рекурсивне дерево залежностей
- symbolic link — символічне посилання
- enablement symlink — посилання автоматичної активації
- canonical path — канонічний шлях
- runtime state — поточний стан виконання
- automatic activation — автоматична активація
- activation — активація
- deactivation — деактивація
- service lifecycle — життєвий цикл служби
- main process — основний процес
- main PID — PID основного процесу
- control process — керувальний процес
- control group — контрольна група
- cgroup — контрольна група
- slice — група керування ресурсами
- scope unit — юніт області процесів
- transient unit — тимчасовий юніт
- persistent unit — постійний юніт
- user service manager — користувацький менеджер служб
- system service manager — системний менеджер служб
- daemon-reload — повторне читання визначень юнітів
- restart policy — політика перезапуску
- restart on failure — перезапуск після помилки
- oneshot service — одноразова служба
- simple service — проста служба
- RemainAfterExit — залишатися активним після завершення
- active (running) — активний із процесом, що виконується
- active (exited) — логічно активний після завершення процесу
- socket — сокет
- socket unit — socket-юніт
- socket activation — активація через сокет
- listening socket — сокет, що очікує дані або з’єднання
- Unix-domain socket — локальний Unix-сокет
- datagram socket — дейтаграмний сокет
- stream socket — потоковий сокет
- communication endpoint — кінцева точка обміну даними
- receive buffer — буфер приймання
- send buffer — буфер надсилання
- connection backlog — черга очікування з’єднань
- sender credentials — дані процесу-відправника
- security context — контекст безпеки
- journal — системний журнал
- journal entry — запис журналу
- journal metadata — метадані журналу
- structured fields — структуровані поля
- message body — текст повідомлення
- transport — канал надходження повідомлення
- syslog transport — syslog-сумісний канал
- kernel transport — повідомлення ядра
- stdout transport — перехоплене стандартне виведення
- priority — рівень серйозності
- facility — категорія повідомлення
- log identifier — ідентифікатор журналу
- boot ID — ідентифікатор завантаження
- machine ID — ідентифікатор системи
- wall clock — календарний системний час
- monotonic clock — монотонний час від завантаження
- time synchronization — синхронізація часу
- NTP — протокол мережевого часу
- clock correction — коригування часу
- journal rotation — ротація журналу
- runtime journal — журнал поточного запуску
- persistent journal — постійний журнал
- drop-in — додатковий фрагмент конфігурації
- metadata — метадані
- exact field match — точна відповідність полю
- logical AND — логічне «І»
- exit status — код завершення
- non-zero exit status — ненульовий код завершення
- successful completion — успішне завершення
- intentional failure — навмисна помилка
- runtime failure — помилка під час виконання
- configuration error — помилка конфігурації
- reset failure state — скинути стан помилки
- historical journal entry — історичний запис журналу
- garbage collection — автоматичне видалення непотрібного об’єкта
- cleanup — очищення
- health check — перевірка справності

### My sentence

I learned how systemd manages system and user services, how unit dependencies and enablement work, and how to inspect service states, failures, sockets, time synchronization, and structured logs safely with `systemctl` and `journalctl`.

## Lesson 18 — Linux storage, filesystems, mounts, and disk investigation

### Why this topic matters in DevOps

Storage problems can stop applications even when CPU, memory, and networking are healthy.

Common incidents include:

- a filesystem becomes full;
- all available inodes are consumed;
- logs, caches, databases, or container data grow unexpectedly;
- an expected filesystem is not mounted;
- a service keeps a deleted file open;
- a directory is writable when it should be read-only;
- an incorrect `/etc/fstab` entry causes mounting or boot problems.

A useful investigation workflow is:

```text
check filesystem capacity
→ identify the largest directory
→ identify the application that owns the data
→ inspect mounts and configuration
→ use the application's supported cleanup method
```

A large directory is not automatically safe to delete.

### Linux storage model

A simplified Linux storage stack is:

```text
physical disk
→ partition
→ filesystem
→ mount point
→ files and directories
```

Example from this system:

```text
/dev/nvme0n1
├─ /dev/nvme0n1p2
│  └─ vfat mounted at /boot/efi
└─ /dev/nvme0n1p3
   └─ ext4 mounted at /
```

Important distinction:

```text
block device → a disk, partition, or virtual storage device
filesystem   → a structure that organizes files and directories
mount point  → a directory where a filesystem becomes accessible
```

### Inspect block devices with `lsblk`

```bash
lsblk
```

Show disks, partitions, loop devices, filesystem types, and mount points as a tree.

```bash
lsblk -e 7
```

Exclude loop devices.

Loop devices are often used for mounted Snap package images and can make the output very long.

```bash
lsblk -d -e 7 \
  -o NAME,PATH,SIZE,MODEL,TRAN,ROTA,RO,TYPE
```

Show only physical disks.

Important columns:

```text
NAME  → device name
PATH  → full device path
SIZE  → device capacity
MODEL → device model
TRAN  → transport type, such as sata or nvme
ROTA  → 1 for rotating disk, 0 for SSD
RO    → read-only state
TYPE  → disk, partition, loop, and other device types
```

```bash
lsblk -e 7 \
  -o NAME,PATH,PKNAME,SIZE,TYPE,FSTYPE,FSVER,LABEL,UUID,MOUNTPOINTS
```

Show disks, partitions, filesystem information, identifiers, and active mount points.

Important columns:

```text
PKNAME      → parent block-device name
FSTYPE      → filesystem type
FSVER       → filesystem version
LABEL       → optional human-readable filesystem label
UUID        → unique filesystem identifier
MOUNTPOINTS → directories where the filesystem is mounted
```

Inspect partition-table information:

```bash
lsblk -e 7 \
  -o NAME,PATH,PKNAME,PTTYPE,PARTTYPE,PARTUUID,FSTYPE,UUID,MOUNTPOINTS
```

Common partition-table types:

```text
gpt → GUID Partition Table
dos → legacy MBR partition table
```

### Inspect active mounts with `findmnt`

```bash
findmnt
```

Show the current mount hierarchy.

Example structure:

```text
/
├─ /proc
├─ /sys
├─ /dev
├─ /run
└─ /boot/efi
```

```bash
findmnt -T PATH
```

Find the filesystem that contains a selected path.

Example:

```bash
findmnt -T "$HOME/Projects/Learning-Journey"
```

Show selected fields without headings:

```bash
findmnt -T PATH \
  -no TARGET,SOURCE,FSTYPE,OPTIONS
```

Important fields:

```text
TARGET  → mount point
SOURCE  → mounted device or source
FSTYPE  → filesystem type
OPTIONS → effective mount options
```

Example from this system:

```text
/ /dev/nvme0n1p3 ext4 rw,relatime
```

Check one exact mount point:

```bash
findmnt --mountpoint /boot/efi
```

`findmnt` generally returns exit status `1` when it cannot find a matching mount.

### Check whether a path is a mount point

```bash
mountpoint PATH
```

On this system:

```text
exit 0  → the path is a mount point
exit 32 → the path exists but is not a mount point
```

Example:

```bash
mountpoint /
printf 'exit status: %s\n' "$?"
```

### Disk-backed and virtual filesystems

Linux mounts both physical storage and special virtual filesystems.

Disk-backed filesystems from this lesson:

```text
/          → ext4 on /dev/nvme0n1p3
/boot/efi  → vfat on /dev/nvme0n1p2
```

Important virtual filesystems:

```text
/proc → process and kernel information
/sys  → devices, drivers, and kernel subsystems
/dev  → device nodes
/run  → current-boot runtime data
```

Inspect them:

```bash
for target in / /boot/efi /proc /sys /dev /run; do
  printf '\nTarget: %s\n' "$target"
  findmnt -no TARGET,SOURCE,FSTYPE,OPTIONS "$target"
done
```

`/proc` provides information such as:

```text
/proc/cpuinfo
/proc/meminfo
/proc/<PID>/
```

`/sys` exposes information about:

```text
block devices
network interfaces
drivers
power management
hardware classes
```

`/dev` contains device nodes such as:

```text
/dev/null
/dev/zero
/dev/random
/dev/nvme0n1
/dev/tty
```

`/run` stores temporary runtime information for the current boot:

```text
PID files
service sockets
runtime locks
systemd state
user-session data
```

### `tmpfs`

`tmpfs` is a memory-backed filesystem.

It can use RAM and swap, but its configured size is a maximum limit, not memory reserved immediately.

Inspect runtime filesystems:

```bash
df -h \
  --output=source,fstype,size,used,avail,pcent,target \
  /run /dev/shm /run/user/1000
```

Example concept:

```text
/dev/shm size: 7.8G
/dev/shm used: 16M
```

This does not mean that 7.8 GiB of RAM is permanently occupied.

Important tmpfs locations:

```text
/run            → system runtime state
/dev/shm        → shared memory
/run/user/1000  → runtime data for UID 1000
```

### Common mount options

```text
rw       → read and write
ro       → read-only
relatime → reduce access-time updates
nosuid   → ignore setuid and setgid privilege elevation
nodev    → do not interpret files as device nodes
noexec   → block direct execution from the mount
```

Ukrainian:

```text
read-only mount       → монтування лише для читання
read-write mount      → монтування для читання та запису
mount restriction     → обмеження монтування
effective mount option → фактичний параметр монтування
```

`noexec` blocks direct execution:

```bash
/path/on/noexec/script.sh
```

but an interpreter can still read the script as data:

```bash
bash /path/on/noexec/script.sh
```

Therefore, `noexec` reduces risk but is not a complete security boundary.

### Persistent mount configuration: `/etc/fstab`

`/etc/fstab` describes filesystems and swap areas that should be prepared during startup.

Show active non-comment entries:

```bash
grep -vE '^[[:space:]]*(#|$)' /etc/fstab
```

An `fstab` entry contains six fields:

```text
source  target  filesystem-type  options  dump  pass
```

Example:

```text
UUID=...  /  ext4  defaults  0  1
```

Show evaluated entries:

```bash
findmnt --fstab --evaluate \
  -o TARGET,SOURCE,FSTYPE,OPTIONS
```

`--evaluate` resolves identifiers such as UUIDs.

Validate the current configuration:

```bash
sudo findmnt --verify --verbose
```

A successful validation should report:

```text
0 parse errors
0 errors
exit status 0
```

A swap file can produce a warning because it is a regular file rather than a block-device partition. This is not necessarily an error when its filesystem type is correctly detected as `swap`.

Important distinction:

```text
configured state → what /etc/fstab requests
active state     → what is actually mounted or enabled now
```

Compare configured and active state:

```bash
findmnt --fstab --evaluate \
  -o TARGET,SOURCE,FSTYPE,OPTIONS

findmnt -no TARGET,SOURCE,FSTYPE,OPTIONS /
findmnt -no TARGET,SOURCE,FSTYPE,OPTIONS /boot/efi

swapon --show=NAME,TYPE,SIZE,USED,PRIO
```

Using UUIDs is usually safer than relying only on names such as `/dev/sdb1`, because device names can change.

Never edit `/etc/fstab` without verifying:

```text
source device
mount target
filesystem type
mount options
```

### Mounts as systemd units

Systemd represents mounts as `.mount` units.

Examples:

```text
/         → -.mount
/boot/efi → boot-efi.mount
```

Convert a path into a mount-unit name:

```bash
systemd-escape --path --suffix=mount /
systemd-escape --path --suffix=mount /boot/efi
systemd-escape --path --suffix=mount /var/lib/docker
```

Inspect mount-unit status:

```bash
systemctl status --no-pager -l -- -.mount
systemctl status --no-pager -l boot-efi.mount
```

For mount units:

```text
active (mounted) → the filesystem is mounted
What             → mount source
Where            → mount target
Type             → filesystem type
```

Inspect machine-readable properties:

```bash
systemctl show \
  -p Id \
  -p LoadState \
  -p ActiveState \
  -p SubState \
  -p What \
  -p Where \
  -p Type \
  -p Options \
  -- \
  -.mount \
  boot-efi.mount
```

`/etc/fstab` entries are converted into systemd units by:

```text
systemd-fstab-generator
```

Generated units can appear under:

```text
/run/systemd/generator/
```

Inspect their origin:

```bash
systemctl show \
  -p Id \
  -p FragmentPath \
  -p SourcePath \
  -- \
  -.mount \
  boot-efi.mount
```

Example relationship:

```text
/etc/fstab
→ systemd-fstab-generator
→ /run/systemd/generator/*.mount
→ systemd mounts the filesystem
```

Do not edit generated files under `/run/systemd/generator`. Modify the original configuration source instead.

### Filesystem capacity with `df`

```bash
df -hT
```

Show mounted filesystem usage.

Options:

```text
-h → human-readable values
-T → show filesystem type
```

Inspect the filesystem containing one path:

```bash
df -hT PATH
```

Example:

```bash
df -hT "$HOME/Projects/Learning-Journey"
```

Important columns:

```text
Size  → total filesystem capacity
Used  → currently allocated storage
Avail → storage available to ordinary users
Use%  → percentage used
```

Check inode usage:

```bash
df -i PATH
```

Important columns:

```text
Inodes → total inode count
IUsed  → used inodes
IFree  → free inodes
IUse%  → inode usage percentage
```

A filesystem can run out of:

```text
data blocks
or
inodes
```

Many small files can exhaust inodes even while `df -h` still reports free disk space.

### Directory usage with `du`

```bash
du -sh PATH
```

Show the allocated size of a directory.

```bash
du -h --max-depth=1 PATH |
sort -h
```

Show first-level usage and sort human-readable sizes.

Stay inside one filesystem:

```bash
sudo du \
  --one-file-system \
  --human-readable \
  --max-depth=1 \
  / |
sort -h
```

Equivalent shorter options:

```bash
sudo du -xhd1 / |
sort -h
```

Important options:

```text
-x, --one-file-system → do not cross filesystem boundaries
-h, --human-readable  → use K, M, and G units
-d1, --max-depth=1    → show only the first level
```

Important distinction:

```text
df → filesystem-wide allocation
du → allocated files reachable through directory paths
```

A standard DevOps investigation:

```bash
df -h /
sudo du -xhd1 / | sort -h
sudo du -xhd1 /var | sort -h
sudo du -xhd1 /var/lib | sort -h
```

Continue deeper only into the largest directory.

Example result from this lesson:

```text
/usr → installed programs and libraries
/home → user and application data
/var → logs, caches, and persistent service data
```

### Important Linux directories

```text
/usr       → installed programs, libraries, and shared resources
/home      → user data and user application state
/var       → changing application and service data
/var/lib   → persistent service and application state
/var/log   → logs and persistent journal data
/var/cache → recreatable cached data
/etc       → system-wide configuration
/boot      → kernel and boot files
/tmp       → temporary files
```

A large directory is not automatically unnecessary.

Examples:

```text
/var/lib/dpkg  → critical dpkg package database
/var/lib/apt   → persistent APT state
/var/cache/apt → recreatable APT cache
/var/log       → system and application logs
```

### Investigate logs and journal storage

Inspect `/var/log`:

```bash
sudo du -xhd1 /var/log |
sort -h
```

Show total journal usage:

```bash
sudo journalctl --disk-usage
```

Find the largest individual log files:

```bash
sudo find /var/log \
  -xdev \
  -type f \
  -printf '%s %p\n' |
sort -k1,1n |
tail -n 15 |
numfmt --field=1 --to=iec
```

Persistent systemd journal files are commonly stored under:

```text
/var/log/journal/
```

Journal rotation divides logs into multiple segment files instead of allowing one file to grow forever.

Important terms:

```text
persistent journal → постійний журнал
journal segment    → сегмент журналу
log rotation       → ротація журналів
archived log       → архівований журнал
```

Do not manually delete active journal files. Use supported `journalctl` maintenance commands only when cleanup is justified.

### Investigate APT cache

Inspect APT cache directories:

```bash
sudo du -xhd2 /var/cache/apt |
sort -h
```

Find large cache files:

```bash
sudo find /var/cache/apt \
  -xdev \
  -type f \
  -printf '%s %p\n' |
sort -k1,1n |
tail -n 15 |
numfmt --field=1 --to=iec
```

Count cached `.deb` packages:

```bash
sudo find /var/cache/apt/archives \
  -maxdepth 1 \
  -type f \
  -name '*.deb' |
wc -l
```

Important distinction:

```text
/var/lib/apt   → package-manager state
/var/cache/apt → cached and recreatable data
```

Use APT commands for cleanup rather than deleting package-manager files manually.

### Allocated size and apparent size

```bash
du -sh PATH
```

Show allocated storage.

```bash
du -sh --apparent-size PATH
```

Show the logical length of file contents.

Example from the repository:

```text
allocated size → 1.9M
apparent size  → 709K
```

Allocated size may be larger because filesystems allocate complete blocks.

Example:

```text
100-byte file
→ apparent size: about 100 bytes
→ allocated size: commonly at least 4 KiB
```

Inspect filesystem block information:

```bash
stat -f --printf='Filesystem type: %T\nBlock size: %S bytes\n' PATH
```

Inspect file allocation:

```bash
stat --printf='Apparent size: %s bytes\nAllocated blocks: %b\nBlock unit: %B bytes\n' FILE
```

For GNU `stat`:

```text
%s → apparent size in bytes
%b → allocated block count
%B → bytes in each reported block unit
```

The block unit reported by `%B` is commonly `512` bytes.

This is not necessarily the same as the ext4 allocation block size, which was `4096` bytes on this system.

Example calculation:

```text
8 stat blocks × 512 bytes = 4096 bytes
```

### Sparse files

A sparse file can have a large logical size without using the same amount of physical storage.

Create a sparse file:

```bash
truncate -s 1G sparse-demo.img
```

Inspect it:

```bash
ls -lh sparse-demo.img
du -h sparse-demo.img
du -h --apparent-size sparse-demo.img
stat sparse-demo.img
```

Expected concept:

```text
logical size:   1 GiB
allocated size: almost 0
```

A sparse region is called a file hole.

Reading an unwritten hole returns zero bytes even though physical data blocks were not allocated.

Write one 4 KiB block without reducing the file length:

```bash
dd if=/dev/zero \
  of=sparse-demo.img \
  bs=4096 \
  count=1 \
  conv=notrunc \
  status=none
```

`conv=notrunc` means:

```text
do not shorten the existing file
```

After the write:

```text
logical size:   1 GiB
allocated size: approximately 4 KiB
```

Copy while preserving sparse regions:

```bash
cp --sparse=always \
  sparse-demo.img \
  sparse-copy.img
```

Compare content:

```bash
cmp --silent sparse-demo.img sparse-copy.img
printf 'cmp exit status: %s\n' "$?"
```

`cmp` exit statuses:

```text
0 → files are identical
1 → files differ
2 → comparison error
```

Sparse files are used for:

```text
virtual-machine disk images
database files
container storage
backup images
preallocated application files
```

Important terms:

```text
sparse file       → розріджений файл
file hole         → розріджена область файла
logical size      → логічний розмір
allocated size    → фактично виділене місце
preserve sparseness → зберігати розріджену структуру
```

### Hard links and disk accounting

A hard link is another directory entry for the same inode.

```text
two pathnames
→ same filesystem
→ same inode
→ same physical data
```

Inspect inode numbers:

```bash
ls -li FILE1 FILE2
```

Inspect metadata:

```bash
stat FILE
```

Find all paths referring to the same file:

```bash
find PATHS \
  -xdev \
  -samefile FILE \
  -printf 'inode=%i links=%n size=%s path=%p\n'
```

Important fields:

```text
%i → inode number
%n → hard-link count
%s → file size
%p → pathname
```

Hard links cannot normally cross filesystem boundaries.

Normal `du` avoids counting the same hard-linked inode more than once during one scan.

Count every hard-link entry:

```bash
du -sh --count-links PATHS
```

The result from `--count-links` should not be added as unique physical usage because the same disk blocks may be counted multiple times.

Important distinction:

```text
hard link     → another name for the same inode
symbolic link → a separate file that contains a pathname
bind mount    → another mounted view of a directory tree
```

Important terms:

```text
hard link        → жорстке посилання
directory entry  → запис каталогу
same inode       → той самий inode
double-counting  → подвійний підрахунок
unique disk data → унікальні фізичні дані
```

### Deleted-but-open files

A process can keep a file open after its pathname has been deleted.

In this situation:

```text
du cannot find the deleted pathname
df still counts the allocated blocks
```

A simplified lifecycle:

```text
create file
→ process opens file
→ pathname is deleted
→ file remains allocated
→ process closes descriptor
→ storage is released
```

Inspect a process file descriptor:

```bash
ls -l /proc/PID/fd/FD
```

A deleted open file can appear as:

```text
/path/to/file.log (deleted)
```

Search system-wide for deleted-but-open files:

```bash
sudo lsof +L1
```

`+L1` searches for open files whose hard-link count is below one.

This problem often happens during log rotation when a service does not reopen its log file.

The normal repair is to make the owning process close or reopen the file, often through a service reload or restart.

Deleting additional files does not release storage held by an open descriptor.

Important terms:

```text
file descriptor       → файловий дескриптор
deleted pathname      → видалене ім’я файла
deleted-but-open file → видалений, але відкритий файл
release storage       → звільнити місце
```

### Temporary tmpfs mount

Create a temporary mount point:

```bash
mount_dir=$(mktemp -d /tmp/example-mount-XXXXXX)
```

Mount a small tmpfs:

```bash
sudo mount \
  -t tmpfs \
  -o size=32M,mode=700,nosuid,nodev,noexec \
  tmpfs \
  "$mount_dir"
```

Verify it:

```bash
mountpoint "$mount_dir"

findmnt \
  --mountpoint "$mount_dir" \
  -o TARGET,SOURCE,FSTYPE,SIZE,USED,AVAIL,USE%,OPTIONS
```

Unmount it:

```bash
sudo umount "$mount_dir"
```

Verify it is gone:

```bash
mountpoint "$mount_dir"
findmnt --mountpoint "$mount_dir"
```

After unmounting, the original underlying directory becomes visible again.

Remove the empty directory:

```bash
rmdir "$mount_dir"
```

Never delete a mount-point directory before confirming that it has been unmounted.

### Bind mounts

A bind mount makes an existing directory tree available at another path.

```text
source directory
→ bind mount
→ target path
```

Create a bind mount:

```bash
sudo mount \
  --bind \
  SOURCE_DIRECTORY \
  TARGET_DIRECTORY
```

Verify it:

```bash
findmnt \
  --mountpoint TARGET_DIRECTORY \
  -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Files accessed through source and target have:

```text
same device
same inode
same underlying data
```

A bind mount does not copy data and does not increase each file’s hard-link count.

Changes made through either path affect the same files.

Unmount the target:

```bash
sudo umount TARGET_DIRECTORY
```

Unmounting removes the alternate view but does not delete source data.

Bind mounts are used in:

```text
Docker bind mounts
container configuration
chroot environments
service isolation
Kubernetes hostPath volumes
```

### Read-only bind mounts

Create a normal bind mount:

```bash
sudo mount \
  --bind \
  SOURCE_DIRECTORY \
  TARGET_DIRECTORY
```

Remount only the target view as read-only:

```bash
sudo mount \
  -o remount,bind,ro \
  TARGET_DIRECTORY
```

Verify the target options:

```bash
findmnt \
  --mountpoint TARGET_DIRECTORY \
  -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Expected:

```text
source path → rw
target path → ro
```

Writing through the target produces:

```text
Read-only file system
```

Writing through the original source can still succeed.

The target immediately shows source changes because both paths expose the same underlying data.

Important distinction:

```text
Permission denied
→ access blocked by ownership or Unix permission bits

Read-only file system
→ access blocked by the mount itself
```

### Swap

Show active swap:

```bash
swapon --show
```

Select columns:

```bash
swapon --show=NAME,TYPE,SIZE,USED,PRIO
```

Show memory and swap totals:

```bash
free -h
```

Read kernel memory values:

```bash
grep -E \
  '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' \
  /proc/meminfo
```

Example from this system:

```text
/swap.img
type: file
size: 4G
used: 0B
```

A swap file is not mounted at a directory. Its target field in `/etc/fstab` is commonly `none`.

Important terms:

```text
swap file      → файл підкачки
swap area      → область підкачки
memory pressure → нестача або високий тиск на оперативну пам’ять
```

### ext4 filesystem metadata

Identify the root device:

```bash
root_dev=$(findmnt -no SOURCE /)
```

Read ext4 metadata:

```bash
sudo tune2fs -l "$root_dev"
```

Use only `-l` for a read-only listing. Other `tune2fs` options can modify filesystem settings.

Useful fields:

```text
Filesystem UUID
Filesystem features
Filesystem state
Errors behavior
Block count
Reserved block count
Free blocks
Block size
Mount count
Maximum mount count
Last checked
Check interval
```

Example values from this system:

```text
filesystem state:      clean
block size:            4096 bytes
reserved percentage:   5%
errors behavior:       Continue
```

`Filesystem state: clean` means the filesystem is not currently marked as unclean.

It does not mean that a full filesystem scan was performed.

Important ext4 features:

```text
has_journal   → filesystem journal is enabled
extent        → files use efficient block-range descriptions
64bit         → supports large filesystem structures
dir_index     → indexed directory lookup
metadata_csum → metadata checksums
```

`needs_recovery` can appear for an actively mounted read-write filesystem because journal recovery information is available if required after an improper shutdown.

Never run `e2fsck` against an actively mounted root filesystem.

### Reserved ext4 blocks

Ext4 can reserve part of the filesystem for privileged use.

Calculate reserved capacity:

```bash
sudo tune2fs -l "$root_dev" |
awk -F: '
  /^Block count:/ {
    gsub(/[[:space:]]/, "", $2)
    total = $2
  }
  /^Reserved block count:/ {
    gsub(/[[:space:]]/, "", $2)
    reserved = $2
  }
  /^Block size:/ {
    gsub(/[[:space:]]/, "", $2)
    block_size = $2
  }
  END {
    printf "Reserved blocks: %d\n", reserved
    printf "Reserved capacity: %.2f GiB\n",
           reserved * block_size / 1024 / 1024 / 1024
    printf "Reserved percentage: %.2f%%\n",
           reserved * 100 / total
  }
'
```

Example from this system:

```text
reserved capacity:   approximately 23.69 GiB
reserved percentage: 5%
```

Reserved blocks are free but normally unavailable to ordinary users.

They can help:

```text
root services continue writing essential information
administrators perform emergency cleanup
reduce filesystem fragmentation near full capacity
```

Important distinction:

```text
free blocks
→ all currently unallocated blocks

available blocks
→ blocks available to ordinary users

reserved blocks
→ free blocks withheld from ordinary-user allocation
```

The reserve is an allocation policy, not a hidden file.

Do not change the reserved-block percentage without a clear operational reason.

### Safe cleanup pattern

Before removing a temporary lesson directory, verify that the path matches the expected prefix.

Example:

```bash
case "$temporary_directory" in
  /tmp/expected-prefix-*)
    rm -rf -- "$temporary_directory"
    cleanup_status=$?
    ;;
  *)
    printf 'Refusing unexpected cleanup path: %s\n' \
      "$temporary_directory" >&2
    cleanup_status=1
    ;;
esac
```

Important safety practices:

```text
quote path variables
use -- before path arguments
verify mount state before deletion
unmount before removing a mount point
use application-supported cleanup tools
avoid manual deletion from /var/lib
```

### Common DevOps storage investigation

Check the filesystem:

```bash
df -hT /
df -i /
```

Identify large top-level directories:

```bash
sudo du -xhd1 / |
sort -h
```

Continue into the largest directory:

```bash
sudo du -xhd1 /var |
sort -h

sudo du -xhd1 /var/lib |
sort -h
```

Inspect logs:

```bash
sudo journalctl --disk-usage
sudo du -xhd1 /var/log |
sort -h
```

Check deleted-but-open files:

```bash
sudo lsof +L1
```

Inspect mounts:

```bash
findmnt
findmnt -T PATH
```

Validate persistent mount configuration:

```bash
sudo findmnt --verify --verbose
```

Check systemd mount units:

```bash
systemctl status --no-pager -l -- UNIT.mount
```

### Important command reference

```bash
lsblk
```

List block devices, partitions, filesystems, and mount points.

```bash
findmnt
```

Show active mounts and their hierarchy.

```bash
findmnt -T PATH
```

Find the filesystem containing a path.

```bash
mountpoint PATH
```

Check whether a path is an active mount point.

```bash
df -hT PATH
```

Show filesystem capacity, usage, and type.

```bash
df -i PATH
```

Show inode usage.

```bash
du -sh PATH
```

Show allocated directory size.

```bash
du -sh --apparent-size PATH
```

Show logical directory size.

```bash
sudo du -xhd1 PATH | sort -h
```

Find large first-level directories without crossing filesystem boundaries.

```bash
stat FILE
```

Inspect file metadata, inode, size, and allocation.

```bash
stat -f PATH
```

Inspect filesystem-level information.

```bash
swapon --show
```

Show active swap areas.

```bash
sudo journalctl --disk-usage
```

Show systemd journal storage usage.

```bash
sudo lsof +L1
```

Find deleted-but-open files.

```bash
sudo mount --bind SOURCE TARGET
```

Create a bind mount.

```bash
sudo mount -o remount,bind,ro TARGET
```

Make a bind-mounted target read-only.

```bash
sudo umount TARGET
```

Unmount a filesystem or bind mount.

```bash
sudo findmnt --verify --verbose
```

Validate `/etc/fstab`.

```bash
sudo tune2fs -l DEVICE
```

Read ext4 filesystem metadata.

### Important vocabulary

- storage — сховище
- storage capacity — місткість сховища
- storage usage — використання сховища
- block device — блоковий пристрій
- physical disk — фізичний диск
- partition — розділ диска
- partition table — таблиця розділів
- filesystem — файлова система
- filesystem type — тип файлової системи
- mount — монтування
- mount point — точка монтування
- mount source — джерело монтування
- mount target — ціль монтування
- mount hierarchy — ієрархія монтувань
- mount option — параметр монтування
- filesystem boundary — межа файлової системи
- disk-backed filesystem — файлова система на накопичувачі
- virtual filesystem — віртуальна файлова система
- pseudo-filesystem — псевдофайлова система
- memory-backed filesystem — файлова система в оперативній пам’яті
- runtime data — дані поточного запуску
- persistent data — постійні дані
- volatile data — тимчасові дані
- shared memory — спільна пам’ять
- device node — файл-представник пристрою
- UUID — унікальний ідентифікатор
- filesystem label — мітка файлової системи
- configured state — налаштований стан
- active state — активний стан
- generated unit — автоматично створений юніт
- mount unit — юніт монтування
- allocation — виділення місця
- allocated size — фактично виділене місце
- apparent size — логічний розмір
- filesystem block — блок файлової системи
- block size — розмір блока
- free blocks — вільні блоки
- available blocks — доступні блоки
- reserved blocks — зарезервовані блоки
- reserved capacity — зарезервована місткість
- inode — структура метаданих файла
- inode usage — використання inode
- inode exhaustion — вичерпання inode
- sparse file — розріджений файл
- file hole — розріджена область файла
- preserve sparseness — зберігати розріджену структуру
- hard link — жорстке посилання
- symbolic link — символічне посилання
- directory entry — запис каталогу
- hard-link count — кількість жорстких посилань
- same inode — той самий inode
- double-counting — подвійний підрахунок
- file descriptor — файловий дескриптор
- deleted pathname — видалене ім’я файла
- deleted-but-open file — видалений, але відкритий файл
- release storage — звільнити місце
- bind mount — прив’язане монтування
- alternate view — альтернативне представлення
- read-only mount — монтування лише для читання
- read-write mount — монтування для читання та запису
- write protection — захист від запису
- mount restriction — обмеження монтування
- underlying directory — початковий каталог під точкою монтування
- underlying file — базовий файловий об’єкт
- unmount — розмонтувати
- persistent journal — постійний журнал
- journal segment — сегмент журналу
- log rotation — ротація журналів
- cache — кеш
- recreatable data — дані, які можна створити повторно
- package archive — архів пакета
- filesystem metadata — метадані файлової системи
- filesystem state — стан файлової системи
- filesystem feature — можливість файлової системи
- filesystem check — перевірка файлової системи
- metadata checksum — контрольна сума метаданих
- extent — діапазон послідовних блоків
- allocation policy — політика виділення місця
- storage investigation — дослідження використання сховища
- disk-space incident — інцидент із заповненням диска
- storage owner — застосунок або служба, якій належать дані
- guarded cleanup — очищення із захисною перевіркою

### My sentence

I learned how Linux organizes disks, partitions, filesystems, mount points, and swap; how to investigate storage with `lsblk`, `findmnt`, `df`, `du`, and `stat`; and how to work safely with sparse files, hard links, systemd mount units, temporary filesystems, bind mounts, read-only views, ext4 metadata, and storage-related incidents.
## Lesson 19 — Linux archives, compression, and backup verification

### Why this topic matters in DevOps

DevOps engineers regularly archive, compress, transfer, verify, and restore files.

Common uses include:

- creating release packages;
- saving configuration before a deployment;
- transferring application files between servers;
- storing CI/CD artifacts;
- collecting logs during incidents;
- verifying downloaded software;
- restoring deleted or damaged files;
- creating backups before risky changes.

Important principle:

```text
A backup is not proven until it has been restored successfully.
```

Ukrainian:

```text
Резервна копія не є перевіреною, доки з неї не було успішно відновлено дані.
```

### Archive versus compression

An archive combines multiple files and directories into one file.

Compression reduces the storage required by data.

```text
archive     → combines files into one container
compression → reduces the amount of storage used
```

Common formats:

```text
.tar     → uncompressed tar archive
.tar.gz  → tar archive compressed with gzip
.tgz     → shorter extension for .tar.gz
.tar.xz  → tar archive compressed with xz
.txz     → shorter extension for .tar.xz
.zip     → archive and compression in one cross-platform format
```

Important terms:

```text
archive             → архів
compression         → стиснення
archive member      → об’єкт усередині архіву
compressed archive  → стиснений архів
archive container   → файл-контейнер архіву
```

### Prepare clean archive paths

Archive relative paths rather than complete absolute paths.

Recommended pattern:

```bash
tar \
  --create \
  --file=backup.tar \
  --directory=PARENT_DIRECTORY \
  DIRECTORY
```

Example:

```bash
tar \
  --create \
  --file=source-backup.tar \
  --directory=/tmp/example \
  source
```

The archive stores:

```text
source/
source/config/
source/config/app.conf
```

It does not store:

```text
/tmp/example/source/config/app.conf
```

This makes the archive cleaner, safer, and easier to extract elsewhere.

Important option:

```text
--directory, -C → change directory before processing files
```

### Create an uncompressed tar archive

```bash
tar \
  --create \
  --verbose \
  --file=source-backup.tar \
  --directory=/tmp/example \
  source
```

Short form:

```bash
tar -cvf source-backup.tar \
  -C /tmp/example \
  source
```

Options:

```text
--create, -c  → create a new archive
--verbose, -v → display processed members
--file, -f    → specify the archive filename
```

Important rule:

```text
-f must be followed by the archive filename
```

List archive contents without extracting:

```bash
tar \
  --list \
  --verbose \
  --file=source-backup.tar
```

Short form:

```bash
tar -tvf source-backup.tar
```

Options:

```text
--list, -t → list archive members
```

Verbose listing can show:

```text
file type and permissions
owner and group
file size
modification time
stored path
symbolic-link target
```

### Create a gzip-compressed tar archive

```bash
tar \
  --create \
  --gzip \
  --verbose \
  --file=source-backup.tar.gz \
  --directory=/tmp/example \
  source
```

Short form:

```bash
tar -czvf source-backup.tar.gz \
  -C /tmp/example \
  source
```

New option:

```text
--gzip, -z → use gzip compression
```

Conceptual process:

```text
files and directories
→ tar creates one archive stream
→ gzip compresses the stream
→ .tar.gz file
```

Test the gzip stream:

```bash
gzip --test source-backup.tar.gz
printf 'exit status: %s\n' "$?"
```

Exit status:

```text
0        → gzip stream is structurally valid
non-zero → gzip detected an error
```

List without extracting:

```bash
tar -tzvf source-backup.tar.gz
```

### Create an xz-compressed tar archive

```bash
tar \
  --create \
  --xz \
  --verbose \
  --file=source-backup.tar.xz \
  --directory=/tmp/example \
  source
```

Short form:

```bash
tar -cJvf source-backup.tar.xz \
  -C /tmp/example \
  source
```

New option:

```text
--xz, -J → use xz compression
```

Test the xz stream:

```bash
xz --test source-backup.tar.xz
printf 'exit status: %s\n' "$?"
```

General comparison:

```text
gzip → usually faster and widely supported
xz   → often stronger compression but slower and more CPU-intensive
```

A stronger algorithm does not guarantee a smaller result for every archive.

For very small files, format metadata and compression overhead may be larger than the saved space.

Important terms:

```text
compression algorithm → алгоритм стиснення
compression overhead  → службові витрати формату стиснення
compression ratio     → коефіцієнт стиснення
trade-off             → компроміс між перевагами та витратами
CPU-intensive         → ресурсомісткий для процесора
```

### Create a ZIP archive

ZIP combines archiving and compression in one format.

```bash
(
  cd /tmp/example || exit 1

  zip \
    --recurse-paths \
    source-backup.zip \
    source
)
```

Short form:

```bash
zip -r source-backup.zip source
```

Option:

```text
--recurse-paths, -r → recursively include directories
```

The parentheses create a subshell.

```text
subshell → дочірнє середовище оболонки
```

Changing directory inside the subshell does not change the main shell’s directory.

Test a ZIP archive:

```bash
unzip -t source-backup.zip
```

List ZIP contents:

```bash
unzip -l source-backup.zip
```

ZIP output may show:

```text
deflated → file was compressed
stored   → file was stored without compression
```

Very small files may be stored without compression because compression would not save useful space.

Practical format choice:

```text
.tar.gz → common for Linux backups, releases, and source packages
.tar.xz → useful when smaller size is more important than speed
.zip    → convenient across Linux, Windows, and macOS
```

### Logical size versus allocated size

```bash
ls -lh ARCHIVE
```

Shows the archive’s logical file size.

```bash
du -h ARCHIVE
```

Shows allocated filesystem space.

Example:

```text
logical size:   336 bytes
allocated size: 4 KiB
```

The filesystem allocates complete blocks, so a small archive commonly occupies at least one block.

### Inspect before extracting

Always inspect an unfamiliar archive before extraction.

For tar:

```bash
tar -tf backup.tar
tar -tzf backup.tar.gz
tar -tJf backup.tar.xz
```

For ZIP:

```bash
unzip -l backup.zip
```

Look for suspicious member names such as:

```text
/etc/example.conf
../../important-file
```

Dangerous patterns:

```text
absolute path → begins with /
path traversal → uses .. to leave the intended directory
```

Important vocabulary:

```text
unsafe path        → небезпечний шлях
absolute path      → абсолютний шлях
relative path      → відносний шлях
parent directory   → батьківський каталог
path traversal     → вихід за межі дозволеного каталогу
malicious archive  → шкідливий архів
```

### Basic tar path-safety check

Count suspicious archive members:

```bash
unsafe_member_count=$(
  tar \
    --list \
    --gzip \
    --file=backup.tar.gz |
  awk '
    /^\// {
      unsafe++
    }

    /(^|\/)\.\.(\/|$)/ {
      unsafe++
    }

    END {
      print unsafe + 0
    }
  '
)
```

Extract only when the result is zero:

```bash
if [ "$unsafe_member_count" -eq 0 ]; then
  tar \
    --extract \
    --gzip \
    --file=backup.tar.gz \
    --directory=RESTORE_DIRECTORY
else
  printf '%s\n' \
    'Refusing extraction because unsafe paths were detected.' >&2
fi
```

Translation:

```text
Refusing extraction because unsafe paths were detected.
→ Відмова від розпакування, тому що були виявлені небезпечні шляхи.
```

This simple check is useful for learning, but unfamiliar archives should still be handled in an isolated location.

### Extract tar archives

Create a separate restore directory:

```bash
mkdir restore-directory
```

Extract an uncompressed archive:

```bash
tar \
  --extract \
  --verbose \
  --file=backup.tar \
  --directory=restore-directory
```

Extract gzip:

```bash
tar \
  --extract \
  --gzip \
  --verbose \
  --file=backup.tar.gz \
  --directory=restore-directory
```

Short form:

```bash
tar -xzvf backup.tar.gz \
  -C restore-directory
```

Extract xz:

```bash
tar -xJvf backup.tar.xz \
  -C restore-directory
```

Options:

```text
--extract, -x   → extract archive members
--directory, -C → extract relative to a selected directory
```

Recommended restoration workflow:

```text
inspect archive
→ create a new empty restore directory
→ extract the archive
→ inspect restored files
→ compare them with the original
→ only then use them
```

Important terms:

```text
extract               → розпакувати, витягнути з архіву
extraction            → розпакування
restore               → відновити
restored data         → відновлені дані
dedicated directory   → окремий спеціально призначений каталог
restoration workflow  → процес відновлення
```

### Compare original and restored data

Compare complete directory trees:

```bash
diff \
  --recursive \
  --no-dereference \
  ORIGINAL_DIRECTORY \
  RESTORED_DIRECTORY
```

Options:

```text
--recursive, -r      → include nested directories
--no-dereference     → compare symbolic links themselves
```

`diff` exit statuses:

```text
0 → no differences
1 → differences found
2 → comparison error
```

A successful archive creation is not enough.

A useful backup must also pass a restoration test.

### Timestamps and permissions

Inspect metadata:

```bash
stat \
  --printf='%A %a %s bytes %y %n\n' \
  ORIGINAL_FILE \
  RESTORED_FILE
```

Useful output:

```text
%A → symbolic permissions
%a → numeric permission mode
%s → size in bytes
%y → modification timestamp
%n → filename
```

A tar archive normally preserves:

```text
directory structure
file permissions
modification timestamps
symbolic links
```

Timestamp precision may differ.

For example, the same whole second may be preserved while fractional nanoseconds are not.

Terms:

```text
timestamp precision  → точність часової мітки
fractional seconds   → дробова частина секунди
nanosecond precision → точність до наносекунд
```

### SHA-256 checksums

A checksum is a value calculated from file contents.

```text
same bytes    → same SHA-256 hash
changed bytes → different SHA-256 hash
```

Calculate one checksum:

```bash
sha256sum backup.tar.gz
```

Create a checksum manifest:

```bash
sha256sum \
  backup.tar \
  backup.tar.gz \
  backup.tar.xz \
  backup.zip \
  > archive-checksums.sha256
```

Verify it:

```bash
sha256sum --check archive-checksums.sha256
```

Expected output:

```text
backup.tar: OK
backup.tar.gz: OK
backup.tar.xz: OK
backup.zip: OK
```

Exit status:

```text
0        → all listed files matched
non-zero → one or more checks failed
```

Important vocabulary:

```text
checksum               → контрольна сума
cryptographic hash     → криптографічний хеш
checksum manifest      → файл-перелік контрольних сум
verify integrity       → перевірити цілісність
exact byte match       → точна відповідність байтів
hash mismatch          → невідповідність хешу
data corruption        → пошкодження даних
unexpected modification → неочікувана зміна
```

### Create a manifest for directory files

Create stable checksums for every regular file:

```bash
(
  cd SOURCE_DIRECTORY || exit 1

  find . \
    -type f \
    -print0 |
  sort -z |
  xargs -0 sha256sum \
    > /tmp/source-files.sha256
)
```

Important options:

```text
-print0 → separate filenames with null bytes
sort -z → sort null-separated names
xargs -0 → read null-separated names
```

This safely handles filenames containing spaces or unusual characters.

Verify files in a restored directory:

```bash
(
  cd RESTORED_DIRECTORY || exit 1
  sha256sum --check /tmp/source-files.sha256
)
```

This confirms the restored contents match the original files exactly.

### Archive tests versus checksums

```text
gzip --test
xz --test
unzip -t
```

Check whether the compressed structure is readable.

```text
sha256sum --check
```

Checks whether the current bytes match an earlier recorded value.

Important distinction:

```text
archive integrity test
→ checks internal archive or compression structure

checksum verification
→ confirms exact byte-for-byte identity
```

A checksum does not prove who created a file.

For publisher identity and authenticity, a digital signature is needed.

```text
authenticity      → автентичність
digital signature → цифровий підпис
publisher         → видавець або автор релізу
```

### Detect a modified restored file

Modify a restored copy:

```bash
printf 'Unexpected modification\n' \
  >> restored/documents/notes.txt
```

Verify against the original manifest:

```bash
(
  cd restored || exit 1
  sha256sum --check /tmp/source-files.sha256
)
```

Expected:

```text
./documents/notes.txt: FAILED
```

Exit status:

```text
1 → at least one checksum did not match
```

This detects accidental or unexpected changes.

### Restore only one selected file

List the exact member name first:

```bash
tar -tzf backup.tar.gz
```

Extract only one member:

```bash
tar \
  --extract \
  --gzip \
  --verbose \
  --overwrite \
  --file=backup.tar.gz \
  --directory=restore-directory \
  source/documents/notes.txt
```

Short form:

```bash
tar -xzvf backup.tar.gz \
  -C restore-directory \
  source/documents/notes.txt
```

Option:

```text
--overwrite → replace an existing file
```

This is called:

```text
selective restoration → вибіркове відновлення
```

It is useful when only one configuration file, script, certificate, or document must be recovered.

Recommended process:

```text
detect checksum failure
→ identify the affected file
→ restore only that member
→ verify checksums again
```

Vocabulary:

```text
affected file         → змінений або пошкоджений файл
selective extraction  → вибіркове розпакування
selective restoration → вибіркове відновлення
recover               → відновити
overwrite             → перезаписати
```

### Detect archive corruption

Never intentionally damage the original backup.

Create a disposable copy:

```bash
cp -- \
  backup.tar.gz \
  backup-corrupt.tar.gz
```

Remove its final byte:

```bash
truncate \
  --size=-1 \
  backup-corrupt.tar.gz
```

`--size=-1` means:

```text
reduce the current file size by one byte
```

Compare hashes:

```bash
sha256sum \
  backup.tar.gz \
  backup-corrupt.tar.gz
```

Compare bytes directly:

```bash
cmp \
  --silent \
  backup.tar.gz \
  backup-corrupt.tar.gz

printf 'cmp exit status: %s\n' "$?"
```

`cmp` exit statuses:

```text
0 → files are identical
1 → files differ
2 → comparison error
```

Test the damaged copy:

```bash
gzip --test backup-corrupt.tar.gz
```

Possible message:

```text
unexpected end of file
```

Translation:

```text
unexpected end of file → неочікуваний кінець файла
```

Trying to list it with tar can produce:

```text
Child returned status 1
Error is not recoverable: exiting now
```

Translations:

```text
child process       → дочірній процес
not recoverable     → неможливо надійно продовжити
truncated file      → обрізаний або неповний файл
incomplete stream   → неповний потік даних
disposable copy     → тимчасова копія, яку можна безпечно пошкодити
```

### Preserve executable files

Create a script:

```bash
mkdir -p source/bin

printf '%s\n' \
  '#!/usr/bin/env bash' \
  'printf "Script executed successfully\n"' \
  > source/bin/run.sh

chmod 755 source/bin/run.sh
```

Permission mode `755`:

```text
owner → read, write, execute
group → read, execute
other → read, execute
```

After archiving and restoring, verify:

```bash
test -x restored/source/bin/run.sh
printf 'executable status: %s\n' "$?"
```

Execute it:

```bash
restored/source/bin/run.sh
```

Successful status:

```text
0 → restored script is executable and completed successfully
```

### Preserve symbolic links

Create a symbolic link:

```bash
ln -s \
  config/app.conf \
  source/current.conf
```

Inspect it:

```bash
ls -l source/current.conf
readlink source/current.conf
```

Expected:

```text
current.conf -> config/app.conf
```

By default, tar normally stores the symbolic link itself instead of copying the target file as another regular file.

After restoration:

```bash
test -L restored/source/current.conf
printf 'symbolic-link status: %s\n' "$?"

readlink restored/source/current.conf
```

Read through the link:

```bash
cat restored/source/current.conf
```

Important terms:

```text
symbolic link          → символічне посилання
link target            → ціль посилання
executable permission  → право на виконання
preserve metadata      → зберігати метадані
object type            → тип файлового об’єкта
regular file           → звичайний файл
follow a link          → перейти за посиланням
```

### Pipeline exit statuses

Bash stores pipeline command statuses in:

```bash
"${PIPESTATUS[@]}"
```

Example:

```bash
tar -tzvf backup.tar.gz |
grep 'run\.sh'

printf 'tar status: %s\n' "${PIPESTATUS[0]}"
printf 'grep status: %s\n' "${PIPESTATUS[1]}"
```

Meaning:

```text
PIPESTATUS[0] → first command in the pipeline
PIPESTATUS[1] → second command in the pipeline
```

This is useful because `$?` after a normal pipeline usually reports only the final command’s status.

### Practical DevOps workflows

#### Backup configuration before a change

```bash
backup_file="service-config-$(date +%F-%H%M%S).tar.gz"

sudo tar \
  -czf "$backup_file" \
  /etc/example-service

sha256sum "$backup_file" \
  > "$backup_file.sha256"

sha256sum \
  --check "$backup_file.sha256"
```

Then:

```text
modify configuration
→ validate it
→ reload or restart the service
→ check service health
→ restore the backup if necessary
```

#### Create a CI/CD artifact

```bash
tar -czf release.tar.gz build/
sha256sum release.tar.gz > release.tar.gz.sha256
```

A later pipeline stage can run:

```bash
sha256sum --check release.tar.gz.sha256
tar -xzf release.tar.gz
```

#### Collect incident data

```bash
sudo tar \
  -czf incident-report.tar.gz \
  /var/log/example-service \
  /etc/example-service
```

Be careful because configuration archives may contain:

```text
passwords
API tokens
private keys
certificates
secret environment variables
```

#### Transfer an application

```bash
tar \
  -czf website-backup.tar.gz \
  /var/www/example
```

Before using the transferred copy:

```text
verify checksum
→ inspect archive members
→ restore into a separate directory
→ test the application
```

### Reliable backup workflow

A file existing with a `.tar.gz` extension does not automatically mean the backup is usable.

Recommended workflow:

```text
create archive
→ test archive structure
→ calculate checksum
→ copy archive to another storage location
→ verify checksum of the copied file
→ perform a test restoration
→ compare restored files
```

Keeping a backup on the same disk as the original data does not protect against complete disk failure.

Important terms:

```text
backup verification   → перевірка резервної копії
test restoration      → тестове відновлення
off-site backup       → резервна копія в іншому фізичному місці
separate storage      → окреме сховище
disaster recovery     → аварійне відновлення
rollback              → повернення до попередньої робочої версії
```

### Safety rules

- Inspect unfamiliar archives before extraction.
- Extract into a new, empty directory first.
- Prefer relative archive paths.
- Watch for absolute paths and `..` components.
- Do not damage or modify the only backup copy.
- Store checksum manifests with backups.
- Verify checksums after transferring files.
- Test restoration periodically.
- Protect archives containing secrets.
- Do not assume successful archive creation means successful recovery.
- Quote all path variables.
- Use `--` before path arguments when supported.

### Important command reference

```bash
tar -cvf archive.tar -C PARENT DIRECTORY
```

Create an uncompressed tar archive.

```bash
tar -czvf archive.tar.gz -C PARENT DIRECTORY
```

Create a gzip-compressed tar archive.

```bash
tar -cJvf archive.tar.xz -C PARENT DIRECTORY
```

Create an xz-compressed tar archive.

```bash
tar -tvf archive.tar
```

List an uncompressed tar archive.

```bash
tar -tzvf archive.tar.gz
```

List a gzip tar archive.

```bash
tar -tJvf archive.tar.xz
```

List an xz tar archive.

```bash
tar -xzvf archive.tar.gz -C RESTORE_DIRECTORY
```

Extract a gzip tar archive.

```bash
tar -xzvf archive.tar.gz -C RESTORE_DIRECTORY MEMBER
```

Extract one selected member.

```bash
gzip --test archive.tar.gz
```

Test a gzip stream.

```bash
xz --test archive.tar.xz
```

Test an xz stream.

```bash
zip -r archive.zip DIRECTORY
```

Create a ZIP archive recursively.

```bash
unzip -l archive.zip
```

List ZIP contents.

```bash
unzip -t archive.zip
```

Test ZIP integrity.

```bash
sha256sum FILE
```

Calculate a SHA-256 checksum.

```bash
sha256sum FILES > checksums.sha256
```

Create a checksum manifest.

```bash
sha256sum --check checksums.sha256
```

Verify files against a checksum manifest.

```bash
diff -r --no-dereference ORIGINAL RESTORED
```

Compare original and restored directory trees.

```bash
cmp --silent FILE1 FILE2
```

Compare two files byte by byte.

```bash
stat FILE
```

Inspect permissions, size, timestamps, and metadata.

```bash
readlink SYMBOLIC_LINK
```

Show a symbolic link’s target.

### Important vocabulary

- archive — архів
- archive member — об’єкт усередині архіву
- archive container — файл-контейнер архіву
- archive listing — перегляд вмісту архіву
- compression — стиснення
- compressed archive — стиснений архів
- compression algorithm — алгоритм стиснення
- compression ratio — коефіцієнт стиснення
- compression overhead — службові витрати формату стиснення
- data stream — потік даних
- integrity test — перевірка цілісності
- checksum — контрольна сума
- checksum manifest — файл-перелік контрольних сум
- cryptographic hash — криптографічний хеш
- hash mismatch — невідповідність хешу
- exact byte match — точна відповідність байтів
- data corruption — пошкодження даних
- corrupted archive — пошкоджений архів
- unexpected modification — неочікувана зміна
- truncated file — обрізаний або неповний файл
- disposable copy — тимчасова копія для безпечного тесту
- extract — розпакувати
- extraction — розпакування
- restore — відновити
- restored data — відновлені дані
- test restoration — тестове відновлення
- selective extraction — вибіркове розпакування
- selective restoration — вибіркове відновлення
- overwrite — перезаписати
- affected file — змінений або пошкоджений файл
- dedicated directory — окремий спеціально призначений каталог
- absolute path — абсолютний шлях
- relative path — відносний шлях
- parent directory — батьківський каталог
- path traversal — вихід за межі дозволеного каталогу
- unsafe path — небезпечний шлях
- recursive — рекурсивний
- symbolic link — символічне посилання
- link target — ціль посилання
- executable permission — право на виконання
- metadata preservation — збереження метаданих
- timestamp precision — точність часової мітки
- fractional seconds — дробова частина секунди
- subshell — дочірнє середовище оболонки
- cross-platform — сумісний із різними операційними системами
- deployment package — пакет для розгортання
- build artifact — артефакт збірки
- release archive — архів релізу
- pipeline stage — етап CI/CD-конвеєра
- configuration backup — резервна копія конфігурації
- rollback — повернення до попередньої робочої версії
- incident investigation — розслідування інциденту
- support bundle — пакет діагностичних даних
- server migration — перенесення на інший сервер
- authenticity — автентичність
- digital signature — цифровий підпис
- disaster recovery — аварійне відновлення
- reliable backup — надійна резервна копія

### My sentence

I learned how to create and inspect `tar`, `gzip`, `xz`, and ZIP archives; how to extract files safely; how to preserve permissions and symbolic links; and how to verify, test, corrupt, detect, and restore backups using `diff`, `cmp`, and SHA-256 checksums.
---

## Checkpoint 02 — Lessons 11–19 and Linux Phase 1 completion

Date: 2026-08-04

Checkpoint 02 completed the second major part of my Linux foundation.

The checkpoint covered Lessons 11–19 and tested practical troubleshooting, Bash scripting, process control, permissions, package management, systemd, storage, archives, checksums, and backup restoration.

---

### Lesson 11 — DNS and HTTP connectivity

I practiced:

```bash
nslookup example.com
dig example.com
dig +short example.com
curl https://example.com
curl -I https://example.com
curl -v https://example.com
curl -L URL
wget --spider URL
```

Important concepts:

```text
DNS
→ converts a domain name into an IP address

HTTP
→ communication between a client and web server

HTTP headers
→ metadata about the response

HTTP body
→ actual response content, for example HTML
```

#### NXDOMAIN vs HTTP 404

```text
NXDOMAIN
→ DNS cannot find the domain
→ the domain does not exist

HTTP 404
→ DNS worked
→ connection worked
→ server responded
→ requested resource was not found
```

This is an important troubleshooting difference.

#### curl headers

```bash
curl -I https://example.com
```

`-I` shows HTTP response headers without downloading the normal response body.

Example:

```text
HTTP/2 200
content-type: text/html
server: ...
```

#### Redirects

```bash
curl -I http://github.com
```

can return:

```text
301 Moved Permanently
Location: https://github.com/
```

Follow the redirect:

```bash
curl -IL http://github.com
```

Important option:

```text
-L → follow HTTP redirects
```

#### HTTP status vs curl exit status

These are different.

```text
HTTP status
→ response from the web server

curl exit status
→ result of the curl command itself
```

Example:

```bash
curl \
  --silent \
  --show-error \
  --output /dev/null \
  --write-out '%{http_code}\n' \
  https://example.com/not-existing-page
```

The server may return:

```text
404
```

while curl still returns:

```text
exit status 0
```

because DNS, TCP/TLS, and HTTP communication succeeded.

Using:

```bash
curl --fail ...
```

makes HTTP 4xx/5xx responses count as curl failures.

Example:

```text
HTTP 404
curl exit status 22
```

Important curl exit codes:

```text
0  → success
6  → could not resolve hostname
7  → could not connect to host
22 → HTTP error when --fail is used
28 → timeout
```

---

### Lesson 12 — Bash scripting fundamentals

Important shebang:

```bash
#!/usr/bin/env bash
```

The shebang tells the operating system which interpreter should run the script.

Run explicitly with Bash:

```bash
bash script.sh
```

Run directly:

```bash
chmod +x script.sh
./script.sh
```

Direct execution requires executable permission.

#### Variables

```bash
name="Artem"
echo "$name"
```

No spaces around `=`:

```bash
name="Artem"
```

not:

```bash
name = "Artem"
```

#### Quoting

Normally quote variable expansions:

```bash
echo "$variable"
```

This protects values containing spaces or special characters.

#### Positional arguments

```text
$0 → script name
$1 → first argument
$2 → second argument
$# → number of arguments
$@ → all arguments
```

Example with default value:

```bash
url="${1:-https://example.com}"
```

Meaning:

```text
use $1 if provided
otherwise use https://example.com
```

#### Command substitution

```bash
directory="$(pwd)"
```

`$(...)` executes a command and stores its output.

Example:

```bash
current_date="$(date +%F)"
```

#### Conditions

String empty:

```bash
if [[ -z "$name" ]]; then
  echo "Empty"
fi
```

String not empty:

```bash
if [[ -n "$name" ]]; then
  echo "Not empty"
fi
```

Numeric comparisons:

```text
-eq → equal
-ne → not equal
-gt → greater than
-ge → greater than or equal
-lt → less than
-le → less than or equal
```

Example:

```bash
if [[ "$status" -ge 200 && "$status" -lt 300 ]]; then
  echo "Healthy"
fi
```

#### File tests

```text
-f → regular file
-d → directory
-e → filesystem object exists
-x → executable
-r → readable
-w → writable
-L → symbolic link
```

#### Exit codes

```text
0        → success
non-zero → failure or special condition
```

Check the previous command:

```bash
echo "$?"
```

Save it immediately when needed:

```bash
command
command_status=$?
```

The next command changes `$?`.

---

### Lesson 13 — Bash loops, arrays, and functions

#### Arrays

```bash
urls=(
  "https://example.com"
  "https://example.com/not-existing-page"
  "https://does-not-exist.invalid"
)
```

Important difference:

```text
"${urls[0]}" → first element only
"${urls[@]}" → all elements
```

#### for loop

```bash
for url in "${urls[@]}"; do
  echo "Checking: $url"
done
```

A `for` loop is useful when iterating through a known list.

#### while loop

```bash
counter=1

while [[ "$counter" -le 3 ]]; do
  echo "$counter"
  counter=$((counter + 1))
done
```

A `while` loop continues while its condition remains true.

#### Functions

```bash
check_url() {
  local url="$1"

  echo "Checking: $url"
}
```

`local` keeps the variable inside the function.

#### return vs exit

```text
return → leaves the current function
exit   → terminates the entire script
```

Example:

```bash
check_url() {
  local url="$1"

  if [[ "$url" == "https://example.com" ]]; then
    return 0
  else
    return 1
  fi
}
```

Save function status:

```bash
check_url "$url"
function_status=$?
```

#### Counters

```bash
healthy_count=0
unhealthy_count=0
failed_count=0
```

Increment:

```bash
((healthy_count++))
```

or:

```bash
healthy_count=$((healthy_count + 1))
```

#### Multi-URL health-check logic

The final checkpoint script classified results as:

```text
function status 0
→ Healthy

function status 1
→ Unhealthy HTTP response

other non-zero status
→ DNS/network failure
```

Final result:

```text
Healthy: 1
Unhealthy: 1
Failed: 1
Script exit status: 2
```

The script combined:

```text
arrays
for loops
functions
local variables
curl
command substitution
return values
exit codes
numeric conditions
counters
overall script status
```

#### Bash checkpoint assessment

Bash scripting is currently the main area that needs continued practice.

I understand the logic of:

```text
variables
conditions
arrays
loops
functions
return / exit
exit codes
counters
```

but combining everything into a complete script without examples still requires repetition.

Recommended workflow:

```text
read an example
→ write it manually
→ bash -n script.sh
→ shellcheck script.sh
→ run it
→ read the error
→ fix it
→ repeat without notes
```

Useful syntax check:

```bash
bash -n script.sh
```

Static analysis:

```bash
shellcheck script.sh
```

---

### Bash file creation methods

#### Using Nano

```bash
nano script.sh
```

Useful for manually writing and editing scripts.

#### Using vi / vim

```bash
vi script.sh
```

Basic workflow:

```text
i
→ enter insert mode

Esc
→ leave insert mode

:wq
→ save and quit

:q!
→ quit without saving
```

#### Using cat and a here-document

```bash
cat > script.sh <<'EOF'
#!/usr/bin/env bash

echo "Hello"
EOF
```

Important:

```text
>  → create/overwrite file
>> → append to file
```

`<<'EOF'` starts a here-document.

The final:

```text
EOF
```

must be on its own line.

Using quoted:

```bash
<<'EOF'
```

prevents variables and command substitutions from being expanded while the file is being created.

#### Simple rule

```text
Nano / VS Code
→ good for manually writing and editing scripts

cat <<'EOF'
→ good for quickly creating a file from a ready block of text
```

---

### Lesson 14 — Processes and job control

Start a background process:

```bash
sleep 300 &
```

The shell returns a job number and PID.

Get the PID of the most recently started background process:

```bash
checkpoint_sleep_pid=$!
```

Important:

```text
$! → PID of the latest background process
```

Show shell jobs:

```bash
jobs
jobs -l
```

Inspect a process:

```bash
ps -p "$checkpoint_sleep_pid" \
  -o pid,ppid,state,cmd
```

Difference:

```text
jobs
→ jobs managed by the current shell

ps
→ operating-system processes
```

#### Process signals

Stop/pause:

```bash
kill -STOP "$checkpoint_sleep_pid"
```

Observed state:

```text
T → stopped
```

Continue:

```bash
kill -CONT "$checkpoint_sleep_pid"
```

Observed state:

```text
S → sleeping
```

Terminate:

```bash
kill "$checkpoint_sleep_pid"
```

Wait for process completion:

```bash
wait "$checkpoint_sleep_pid"
```

Observed exit status:

```text
143
```

Because:

```text
143 = 128 + 15
15 = SIGTERM
```

Important signals:

```text
SIGSTOP → pause process
SIGCONT → continue process
SIGTERM → request termination
```

Common process states:

```text
R → running
S → sleeping
T → stopped
Z → zombie
```

Other useful tools:

```bash
pgrep PROCESS
pgrep -a PROCESS
top
htop
```

---

### Lesson 15 — Users, groups, and permissions

Check identity:

```bash
id
groups
id -gn
```

`id` shows:

```text
UID
primary GID
supplementary groups
```

#### Permission structure

Example:

```text
-rwxr-x---
```

Split:

```text
-    → regular file
rwx  → owner
r-x  → group
---  → others
```

Permission values:

```text
r → 4
w → 2
x → 1
```

Examples:

```text
700 → rwx------
640 → rw-r-----
644 → rw-r--r--
750 → rwxr-x---
755 → rwxr-xr-x
```

Checkpoint targets:

```text
config.txt → 640 → -rw-r-----
run.sh     → 750 → -rwxr-x---
```

Meaning of `640`:

```text
owner  → rw-
group  → r--
others → ---
```

Meaning of `750`:

```text
owner  → rwx
group  → r-x
others → ---
```

#### chmod

Change permissions:

```bash
chmod 640 config.txt
chmod 750 run.sh
```

Symbolic example:

```bash
chmod g-w config.txt
```

Meaning:

```text
remove write permission from group
```

#### chown and chgrp

```text
chmod → change permissions
chown → change owner and/or group
chgrp → change group ownership
```

Examples:

```bash
chown user file
chown user:group file
chgrp group file
```

#### umask

Check:

```bash
umask
```

Typical base modes:

```text
files       → 666
directories → 777
```

Example:

```text
umask 027

file      → approximately 640
directory → approximately 750
```

Technically, umask masks permission bits.

#### setgid directory

```bash
chmod 2770 shared-dir
```

New files/directories inside normally inherit the directory's group.

#### Sticky bit

```bash
chmod 1777 shared-dir
```

Used for shared writable directories such as `/tmp`.

It prevents users from normally deleting or renaming files owned by other users.

---

### Lesson 16 — APT package management

Important package-management layers:

```text
APT
→ high-level Debian/Ubuntu package management

dpkg
→ lower-level Debian package database and package tool
```

Refresh package metadata:

```bash
sudo apt update
```

Important:

```text
apt update
→ refresh package information
→ does NOT install upgrades
```

Upgrade packages:

```bash
sudo apt upgrade
```

Full upgrade:

```bash
sudo apt full-upgrade
```

`full-upgrade` may install or remove packages to resolve dependency changes.

#### Package information

```bash
apt-cache policy curl
```

Checkpoint result:

```text
Installed: 8.5.0-2ubuntu10.11
Candidate: 8.5.0-2ubuntu10.11
```

Meaning:

```text
Installed
→ version currently installed

Candidate
→ version APT would currently choose for installation or upgrade
```

Check installed package:

```bash
dpkg -l curl
```

or:

```bash
dpkg-query -W curl
```

Other useful commands:

```bash
apt search PACKAGE
apt show PACKAGE
apt list --installed
dpkg -l
```

#### Remove vs purge

```bash
sudo apt remove PACKAGE
```

normally removes the package while keeping configuration files.

```bash
sudo apt purge PACKAGE
```

removes the package and its configuration files.

#### autoremove

Preview first:

```bash
sudo apt autoremove --dry-run
```

Then, only after reviewing:

```bash
sudo apt autoremove
```

Important safe workflow:

```text
apt update
→ inspect packages
→ simulate risky operations when possible
→ perform change
→ verify system/services afterward
```

---

### Lesson 17 — systemd and journalctl

systemd manages services and other units.

#### Service status

```bash
systemctl status NetworkManager
```

Checkpoint result:

```text
Loaded: loaded ... enabled
Active: active (running)
```

Important difference:

```text
active
→ service is running now

enabled
→ service is configured to start automatically at boot
```

Possible combinations:

```text
active + enabled
→ running now and starts automatically at boot

active + disabled
→ running now but not configured to start automatically

inactive + enabled
→ not running now but configured to start automatically

inactive + disabled
→ not running now and not configured to start automatically
```

#### Failed units

```bash
systemctl --failed
```

Checkpoint result:

```text
0 loaded units listed
```

Meaning:

```text
systemd currently reports no failed units
```

#### Other service commands

```bash
sudo systemctl start SERVICE
sudo systemctl stop SERVICE
sudo systemctl restart SERVICE
sudo systemctl reload SERVICE
sudo systemctl enable SERVICE
sudo systemctl disable SERVICE
```

Difference:

```text
restart
→ stop and start again

reload
→ reload configuration without a complete restart, when supported
```

#### journalctl

Current boot:

```bash
journalctl -b
```

One service:

```bash
journalctl -u SERVICE
```

One service from current boot:

```bash
journalctl -b -u SERVICE
```

Without pager:

```bash
journalctl -b -u SERVICE --no-pager
```

Recent messages:

```bash
journalctl -u SERVICE -n 50
```

Follow new logs:

```bash
journalctl -u SERVICE -f
```

Warnings:

```bash
journalctl -p warning
```

Checkpoint command:

```bash
journalctl -b -u NetworkManager --no-pager
```

During the checkpoint I found a Netplan warning saying that:

```text
/etc/netplan/01-network-manager-all.yaml
```

had permissions that were too open.

The checkpoint remained read-only and did not modify networking configuration.

#### Troubleshooting workflow

```text
systemctl status SERVICE
→ inspect service state
→ inspect journalctl logs
→ identify useful error
→ inspect configuration
→ make controlled change
→ restart/reload if necessary
→ verify again
```

---

### Lesson 18 — Storage, filesystems, and mounts

Important storage structure:

```text
disk
→ partition
→ filesystem
→ mount point
→ files/directories
```

Example from my Ubuntu system:

```text
disk       → /dev/nvme0n1
partition  → /dev/nvme0n1p3
filesystem → ext4
mount point → /
```

#### lsblk

```bash
lsblk
```

Show filesystem information:

```bash
lsblk -f
```

Useful columns:

```text
NAME
FSTYPE
UUID
FSAVAIL
FSUSE%
MOUNTPOINTS
```

#### df

```bash
df -h
df -hT
```

Shows filesystem-level disk usage.

Checkpoint root filesystem:

```text
/dev/nvme0n1p3
ext4
mounted at /
```

#### du

```bash
du -sh DIRECTORY
```

Shows space used by a specific directory.

Checkpoint temporary laboratory:

```text
12K
```

Important difference:

```text
df
→ mounted filesystem usage

du
→ size used by specific files/directories
```

#### findmnt

```bash
findmnt
findmnt /
findmnt -T /dev/shm
```

Shows mounted filesystems and their mount points/options.

#### /dev/shm

Checkpoint result:

```text
/dev/shm
→ tmpfs
```

`tmpfs` is a temporary memory-backed filesystem.

It is commonly used for shared memory and temporary data.

#### Important terms

```text
disk
→ storage device

partition
→ section of a disk

filesystem
→ structure used to organize files/directories and metadata

mount point
→ directory where a filesystem becomes accessible
```

#### Storage safety

Before disk operations:

```text
identify device
→ inspect size
→ inspect filesystem
→ inspect mount points
→ verify target again
```

Dangerous commands include:

```text
mkfs
fdisk write operations
parted changes
wipefs
dd
```

Never use destructive commands against an unidentified disk.

---

### Lesson 19 — Archives, compression, and backups

#### Archive vs compression

```text
archive
→ combines files/directories into one container

compression
→ reduces the number of bytes required to store data
```

Formats:

```text
.tar     → tar archive without gzip compression
.tar.gz  → tar archive compressed with gzip
.tar.xz  → tar archive compressed with xz
.zip     → archive format with built-in compression support
```

#### Create gzip-compressed tar archive

Checkpoint command:

```bash
tar -czvf "$archive_file" \
  -C "$archive_dir" \
  source
```

Important options:

```text
-c → create
-z → gzip compression
-v → verbose
-f → archive filename
-C → change directory before processing files
```

Other tar options:

```text
-x → extract
-t → list archive contents
-J → xz compression
```

#### Relative archive paths

The checkpoint archive contained:

```text
source/
source/config/
source/config/app.conf
source/documents/
source/documents/notes.txt
```

It did not contain a full absolute path like:

```text
/tmp/linux-phase1-checkpoint-.../archive-lab/source/...
```

Relative paths are better because they are:

```text
safer
more portable
easier to restore to a chosen location
```

#### List contents without extraction

```bash
tar -tzvf "$archive_file"
```

#### gzip integrity test

```bash
gzip --test "$archive_file"
```

Checkpoint result:

```text
gzip test status: 0
```

Meaning:

```text
gzip stream is structurally valid
```

#### SHA-256

Calculate checksum:

```bash
sha256sum "$archive_file"
```

Create checksum file:

```bash
sha256sum "$archive_file" \
  > source-backup.sha256
```

Verify:

```bash
sha256sum --check source-backup.sha256
```

Checkpoint result:

```text
source-backup.tar.gz: OK
```

A SHA-256 checksum helps verify:

```text
integrity
→ whether the file bytes still match the previously recorded hash
```

It can help detect:

```text
corruption
unexpected modification
incomplete transfer
wrong file
```

Important:

```text
checksum verifies integrity
≠
checksum proves authenticity
```

#### Restore backup

Restore to a separate directory:

```bash
tar -xzvf "$archive_file" \
  -C "$restore_dir"
```

Check restored files:

```bash
find "$restore_dir" -type f
```

Compare original and restored directories:

```bash
diff \
  --recursive \
  --no-dereference \
  "$source_dir" \
  "$restore_dir/source"
```

Checkpoint result:

```text
Diff exit status: 0
```

Meaning:

```text
original data
=
restored data
```

Important `diff` statuses:

```text
0 → no differences
1 → differences found
2 → comparison error
```

#### Backup principle

> A backup is not proven until it has been successfully restored and verified.

Reliable backup workflow:

```text
create archive
→ inspect archive
→ test archive
→ calculate checksum
→ copy backup
→ verify checksum
→ restore to separate location
→ compare restored data
```

---

## Checkpoint 02 practical results

Checkpoint 02 tested Lessons 11–19.

Completed practical tasks:

- DNS resolution with `nslookup`
- NXDOMAIN investigation with `dig`
- HTTP headers with `curl -I`
- HTTP redirects with `curl -L`
- HTTP `200` and `404`
- curl exit status `0`
- curl `--fail` exit status `22`
- Bash single-URL health-check
- arrays
- `for` loops
- functions
- `local` variables
- `return`
- exit-status handling
- counters
- multi-URL health-check
- background processes
- `$!`
- `jobs`
- `ps`
- `SIGSTOP`
- `SIGCONT`
- `SIGTERM`
- exit status `143`
- user/group investigation
- symbolic and numeric permissions
- `640`
- `750`
- executable script verification
- APT package inspection
- installed vs candidate version
- systemd failed-unit inspection
- NetworkManager status
- journalctl current-boot logs
- `lsblk`
- `lsblk -f`
- `df`
- `du`
- `findmnt`
- `/dev/shm`
- tar.gz archive creation
- relative archive paths
- gzip integrity test
- SHA-256 checksum
- SHA-256 verification
- backup restoration
- recursive `diff`
- safe cleanup

---

## Checkpoint 02 assessment

### Strong areas

I demonstrated good understanding of:

```text
DNS vs HTTP problems
HTTP status codes
curl troubleshooting
process and job control
Linux permissions
APT package investigation
systemd service investigation
journalctl
storage concepts
archive and restore workflow
safe Linux investigation
```

### Main area to improve

Bash scripting requires continued practice.

I understand individual concepts, but I still need repetition when combining:

```text
variables
conditions
arrays
loops
functions
return values
exit codes
counters
curl output
```

into one complete script.

This is a practice requirement, not a failed checkpoint.

---

## Important Phase 1 troubleshooting workflow

When something does not work:

```text
1. Read the complete error.
2. Identify which layer may be failing.
3. Inspect the current state before changing anything.
4. Gather evidence.
5. Test one hypothesis.
6. Make one controlled change.
7. Verify the result.
8. Clean up temporary resources.
```

For a website/service:

```text
service/process
→ logs
→ listening ports
→ DNS
→ connectivity
→ HTTP
→ permissions/configuration
→ disk space/packages
```

Useful commands:

```bash
systemctl status SERVICE
journalctl -b -u SERVICE
ss -lntp
dig DOMAIN
nslookup DOMAIN
curl -I URL
id
ls -l FILE
df -h
du -sh DIRECTORY
apt-cache policy PACKAGE
```

---

## Important exit codes from Phase 1

```text
0   → success
1   → general failure / negative result
2   → command processing or usage error
6   → curl could not resolve hostname
7   → curl could not connect
22  → curl HTTP error with --fail
28  → curl timeout
126 → command found but could not execute
127 → command not found
130 → interrupted with Ctrl+C
143 → terminated by SIGTERM
```

Exit-code meanings depend on the command, so documentation should be checked when necessary.

---

## Important vocabulary

```text
resolve hostname       → визначити IP-адресу домену
request                → запит
response               → відповідь
response header        → заголовок відповіді
response body          → тіло відповіді
redirect               → перенаправлення
exit status            → код завершення
argument               → аргумент
condition              → умова
array                   → масив
loop                    → цикл
function                → функція
local variable          → локальна змінна
counter                 → лічильник
background process      → фоновий процес
foreground process      → процес на передньому плані
permission              → право доступу
ownership               → власність
dependency              → залежність
candidate version       → версія, яку APT вибере для встановлення
service                 → сервіс
failed unit             → systemd unit у стані failure
filesystem              → файлова система
mount point             → точка монтування
block device            → блочний пристрій
archive                 → архів
compression             → стиснення
checksum                → контрольна сума
integrity               → цілісність
authenticity            → автентичність / підтвердження походження
restore                 → відновлення
corruption              → пошкодження даних
relative path           → відносний шлях
absolute path           → абсолютний шлях
troubleshooting         → пошук і усунення проблем
```

---

## Linux Phase 1 completion

Linux Phase 1 is completed.

Completed:

```text
Lessons 01–19
Checkpoint 01
Checkpoint 02
```

I now have a practical Linux foundation covering:

```text
navigation and files
Git fundamentals
system information
processes
services
logs
networking
DNS and HTTP
Bash scripting
loops and functions
job control
users and permissions
APT package management
systemd troubleshooting
storage and filesystems
archives and backups
```

The Linux foundation is strong enough to continue with real projects and later DevOps topics.

Bash scripting will continue to be practised alongside future work, especially:

```text
writing scripts without copying examples
combining multiple Bash concepts
reading errors
using bash -n
using ShellCheck
understanding exit codes
building small automation scripts
```

The checkpoint temporary environment was safely removed.
