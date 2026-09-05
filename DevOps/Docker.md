# Docker Notes — Artem

## Purpose

This file contains my Docker notes.

The goal is to learn Docker step by step, practise real commands, and explain container concepts in clear English.

---

## Lesson 01 — Docker concepts and first containers

Date: `2026-08-24`

In this lesson, I learned the main Docker concepts and practised the basic container workflow.

### Main Docker concepts

#### Docker CLI

The Docker CLI is the `docker` command that I use in the terminal. It sends requests such as run, stop, list, and remove to the Docker daemon.

CLI means command-line interface — інтерфейс командного рядка.

#### Docker daemon (`dockerd`)

The Docker daemon is the background service that manages Docker objects. It receives commands from the Docker CLI and manages images, containers, networks, and volumes.

Daemon means a program that works in the background — фонова системна програма.

#### `containerd`

`containerd` is a lower-level container runtime used by Docker. Docker delegates container lifecycle tasks to it, including starting and stopping containers.

Ukrainian explanation:

> Docker керує зручним користувацьким процесом, а `containerd` виконує нижчорівневу роботу з життєвим циклом контейнерів.

#### Image

An image is a read-only template that contains an application, its files, and the dependencies needed to run it.

An image is like a prepared blueprint — образ є підготовленим шаблоном.

#### Container

A container is a running or stopped instance created from an image. Multiple containers can be created from the same image.

Containers have isolated filesystems and processes. However, they are not complete virtual machines: Linux containers share the host Linux kernel.

Ukrainian explanation:

> Контейнери мають ізольовані файлові системи та процеси, але використовують спільне ядро Linux хост-системи.

#### Docker Hub and registry

A registry stores and distributes container images. Docker Hub is a public registry used by Docker by default.

When an image is not available locally, Docker can pull it from a registry.

#### Tag

A tag is a readable image version or variant label, such as `latest` or `alpine`.

Example:

```text
nginx:alpine
```

Here, `nginx` is the repository name and `alpine` is the tag. A tag can be moved to point to a newer image, so it is not an immutable identifier.

#### Digest

A digest is a content-based, immutable identifier for an exact image, usually beginning with `sha256:`. If image content changes, its digest changes.

Ukrainian explanation:

> Тег — це зручна назва версії, яка може змінити своє посилання. Digest — незмінний ідентифікатор точного вмісту образу.

#### Port mapping

Port mapping connects a port on the host to a port inside a container.

The format is:

```text
HOST_PORT:CONTAINER_PORT
```

This allows a service inside an isolated container to be reached from the host.

### First container: `hello-world`

I successfully ran:

```bash
docker run hello-world
```

Docker performed these steps:

1. It did not find the image locally.
2. It pulled `hello-world:latest` from Docker Hub.
3. It created a new container from the image.
4. It started the container.
5. The container printed the Docker welcome message.
6. The container exited successfully with exit code `0`.

Exit code `0` means that the container's main process completed successfully. The container stopped because its task was finished, not because Docker failed.

The automatically generated container name was `peaceful_shirley`.

### Listing images and containers

I practised:

```bash
docker image ls
docker ps
docker ps -a
```

`docker image ls` lists images stored locally.

`docker ps` shows only running containers.

`docker ps -a` shows all containers, including running and stopped containers.

This explains why the completed `hello-world` container appeared in `docker ps -a` but not in `docker ps`.

### Running Nginx

I ran an Nginx web server with:

```bash
docker run -d --name lesson01-nginx -p 8080:80 nginx:alpine
```

Command explanation:

- `docker run` creates and starts a new container.
- `-d` runs the container in detached mode, in the background.
- `--name lesson01-nginx` gives the container a clear custom name.
- `-p 8080:80` maps host port `8080` to container port `80`.
- `nginx:alpine` selects the Nginx image with the lightweight `alpine` tag.

The request path was:

```text
browser or curl
→ localhost:8080 on the host
→ port 80 inside lesson01-nginx
→ Nginx
```

### Nginx verification

I opened this address successfully:

```text
http://localhost:8080
```

The command `curl -I http://localhost:8080` returned headers including:

```text
HTTP/1.1 200 OK
Server: nginx/1.31.4
Content-Type: text/html
```

`200 OK` confirmed that Nginx received the request and returned a successful HTTP response.

`ss -lnt` confirmed that port `8080` was listening through both IPv4 and IPv6.

The container logs from:

```bash
docker logs lesson01-nginx
```

showed:

- `HEAD / HTTP/1.1` with status `200` from `curl -I`
- `GET / HTTP/1.1` with status `200` from Firefox
- `GET /favicon.ico` with status `404` from Firefox

The favicon `404` was harmless. Firefox requested a small website icon, but the file did not exist. The main page still returned `200` and worked correctly.

### Stopping and removing containers

I stopped the Nginx container:

```bash
docker stop lesson01-nginx
```

After it stopped, `curl` returned exit code `7` because nothing was listening on host port `8080`.

This was expected and confirmed that the stopped container was no longer serving the website.

I removed these stopped containers:

- `lesson01-nginx`
- `peaceful_shirley`

Removing a container removes that container instance, but it does not automatically remove the image used to create it.

I verified that these images remained available locally:

- `hello-world:latest`
- `nginx:alpine`

### English–Ukrainian vocabulary

| English | Ukrainian |
|---|---|
| image | образ контейнера |
| container | контейнер |
| registry | реєстр образів |
| tag | тег / мітка версії |
| digest | незмінний ідентифікатор вмісту |
| daemon | фонова системна програма |
| pull an image | завантажити образ із реєстру |
| port mapping | перенаправлення / зіставлення портів |
| detached mode | фоновий режим |
| isolated | ізольований |
| host | хост / основна система |

### Key takeaways

- Docker uses images as templates and containers as runnable instances.
- Containers isolate filesystems and processes but share the host Linux kernel.
- The Docker CLI communicates with the Docker daemon, which uses `containerd` for lower-level container operations.
- `docker ps` shows running containers; `docker ps -a` also shows stopped containers.
- Port mapping makes a container service accessible through a host port.
- HTTP headers, listening ports, and container logs provide different evidence during verification.
- Stopping or removing a container does not automatically remove its image.

## Next step

The next lesson is:

**Docker Lesson 02 — Images and Containers**

---

## Lesson 02 — Images and Containers

**Date:** 2026-08-26

In this lesson, I learned how Docker images, tags, and containers are related. I also practised the container lifecycle, investigated several exit codes, and cleaned up resources safely.

### Starting state

Before the lesson:

- the Docker service was `active`;
- the local images were `hello-world:latest` and `nginx:alpine`;
- no containers existed;
- Git contained only the pre-existing untracked `source-backup.tar.gz`;
- the latest existing commit was `722eb21 Refocus Docker notes on learning concepts`.

### Image and container fundamentals

An image is an immutable package or template containing the files and dependencies needed to run an application. Immutable means that the existing image content does not change — незмінний.

A container is an instance created from an image. One image can create multiple independent containers, and each container has its own name, ID, process state, and writable changes.

A registry stores and distributes images. A repository groups related images under one name. A tag is a readable, mutable reference to image content, while an image digest identifies exact content cryptographically.

Ukrainian explanation:

> Registry зберігає images, repository об'єднує пов'язані images, tag є змінюваним посиланням, а digest точно визначає вміст.

Important command comparison:

```text
docker pull    → downloads an image only
docker run     → creates and starts a new container
docker start   → starts an existing stopped container
docker restart → stops and starts an existing container
```

### Pulling an explicit tag

I pulled a specific Alpine tag:

```bash
docker pull alpine:3.24
```

I verified it with:

```bash
docker image ls alpine
```

The result was:

- image: `alpine:3.24`;
- image ID: `28bd5fe8b56d`;
- content size: approximately `3.93 MB`.

`docker pull` downloaded the image but did not create a container.

The full image reference is:

```text
docker.io/library/alpine:3.24
```

Its parts are:

```text
docker.io → registry
library   → official-images namespace
alpine    → repository
3.24      → tag
```

### Short-lived container

I ran:

```bash
docker run --name alpine-once alpine:3.24 echo "Hello from Alpine"
```

Docker created the container and ran `echo "Hello from Alpine"` inside it. The command printed its output and finished, so the container stopped immediately.

I verified the state with:

```bash
docker ps
docker ps -a
```

The container did not appear in `docker ps` because it was no longer running, but it appeared in `docker ps -a`:

- container ID: `8dd18b168391`;
- name: `alpine-once`;
- status: `Exited (0)`.

A container remains running only while its main process is running. This was a short-lived container — короткочасний container.

### Starting an existing container

I started the stopped container again:

```bash
docker start -a alpine-once
```

The `-a` option attached the terminal to the container output. The original `echo` command ran again because a container keeps the command configured when it is created.

The container retained ID `8dd18b168391`. `docker start` reused it and did not create a new container.

In container listings:

- `CREATED` is the original container creation time;
- `STATUS` describes the latest state of the container process.

### Name conflict and exit code 125

I attempted to create another container with the same name:

```bash
docker run --name alpine-once alpine:3.24 echo "Second container"
```

Docker rejected the request because container names must be unique. The result was:

```text
exit status 125
```

Exit code `125` means Docker could not start the requested container. The application inside the new container did not run because Docker failed before that stage.

### Renaming and multiple containers

I renamed the first container:

```bash
docker rename alpine-once alpine-first
```

Then I created a second container using the now-available name:

```bash
docker run --name alpine-once alpine:3.24 echo "Second container"
```

The results were:

- `alpine-first`: ID `8dd18b168391`;
- new `alpine-once`: ID `382817dcc879`;
- both containers used `alpine:3.24`;
- both exited with code `0`.

Renaming changed only the first container's name, not its ID. Docker reused the existing local image for the second container and did not download it again. This demonstrated that one image can create multiple independent containers.

### Incorrect command arguments

My first attempt to create a long-running container was:

```bash
docker run -d --name alpine-sleeper alpine:3.24 sleep 300 echo "sleepy"
```

Everything after the image name was treated as one executable and its arguments:

```text
Executable: sleep
Arguments: 300, echo, sleepy
```

I diagnosed the failure with:

```bash
docker ps -a --filter name=alpine-sleeper
docker logs alpine-sleeper
```

The results were:

```text
Exited (1)
sleep: invalid number 'echo'
```

Exit code `1` meant that the process inside the container started but returned an error. Docker passed `echo` to `sleep` as an argument; it did not interpret it as a second command.

Multiple shell commands require an explicit shell, for example `sh -c`, although that method was not practised during this lesson.

### Correct long-running container

I removed the failed container and recreated it correctly:

```bash
docker rm alpine-sleeper
docker run -d --name alpine-sleeper alpine:3.24 sleep 300
```

The result was:

- container ID: `4d369b5753fa`;
- command: `sleep 300`;
- status: `Up`;
- name: `alpine-sleeper`.

The `-d` option means detached mode, so the container ran in the background — фоновий режим. This was a long-running container because its main process continued to run.

### Stop behavior and exit code 137

I stopped the container:

```bash
docker stop alpine-sleeper
```

Its result was:

```text
Exited (137)
```

I inspected the reason:

```bash
docker inspect --format 'Exit={{.State.ExitCode}} OOMKilled={{.State.OOMKilled}}' alpine-sleeper
```

The output was:

```text
Exit=137 OOMKilled=false
```

The calculation `137 = 128 + 9` shows that the process was terminated by signal 9, `SIGKILL`. Docker first attempted a graceful termination. The `sleep` process did not stop within the timeout, so Docker forcibly terminated it.

`OOMKilled=false` proved that insufficient memory was not the cause.

### Start versus restart

I started the same stopped container:

```bash
docker start alpine-sleeper
```

Then I restarted the running container:

```bash
docker restart alpine-sleeper
```

Verification showed that:

- the container retained ID `4d369b5753fa`;
- its original `CREATED` time remained;
- its `Up` time reset;
- `start` reused the stopped container;
- `restart` stopped and started the same container;
- neither command created a new container.

The `sleep 300` process later completed naturally, resulting in `Exited (0)`.

### Tags pointing to the same image

I pulled another Alpine tag:

```bash
docker pull alpine:latest
```

Both references displayed the same image ID:

```text
alpine:3.24   28bd5fe8b56d
alpine:latest 28bd5fe8b56d
```

I inspected the tags with:

```bash
docker image inspect alpine:3.24 --format '{{json .RepoTags}}'
```

The result was:

```text
["alpine:3.24","alpine:latest"]
```

Both tags pointed to the same underlying image, so Docker stored the image layers only once. `latest` is a mutable tag and can point to another image in the future. Local images do not update automatically; another pull is required.

### Untagging versus deleting

I removed the `latest` reference:

```bash
docker image rm alpine:latest
```

Docker reported:

```text
Untagged: alpine:latest
```

The `alpine:3.24` reference and image ID `28bd5fe8b56d` remained. This proved that Docker removed only the tag, not the shared underlying image data.

### Image dependency conflict

I attempted to remove the remaining reference:

```bash
docker image rm alpine:3.24
```

Docker refused because existing containers still referenced the image, including stopped container `8dd18b168391`. The result was:

```text
exit status 1
```

Both running and stopped containers can prevent image removal. Forced removal is not the normal solution because it bypasses the safe dependency workflow.

The safe order is:

```text
stop running containers → remove containers → remove unused image
```

### Safe cleanup

I listed the containers that depended on the image:

```bash
docker ps -a --filter ancestor=alpine:3.24
```

Then I cleaned up in dependency order:

```bash
docker stop alpine-sleeper
docker rm alpine-first alpine-once alpine-sleeper
docker image rm alpine:3.24
```

The final image removal produced:

```text
Untagged: alpine:3.24
Deleted: sha256:28bd5fe8...
```

`Untagged` removed the final reference. `Deleted` removed the now-unused underlying image data.

The final Docker state was:

- no containers;
- retained images: `hello-world:latest` and `nginx:alpine`;
- the Alpine image and all Lesson 02 containers were removed.

### Exit-code summary

| Exit code | Meaning in this lesson                         |
| --------: | ---------------------------------------------- |
|       `0` | Container process completed successfully       |
|       `1` | Process inside the container returned an error |
|     `125` | Docker could not start the requested container |
|     `137` | Container process was terminated with `SIGKILL` |

### Commands practised

| Command | Purpose |
|---|---|
| `docker pull` | Download an image from a registry without creating a container. |
| `docker image ls` | List local images. |
| `docker image inspect` | Show detailed image information. |
| `docker image rm` | Remove an image tag or unused image data. |
| `docker run` | Create and start a new container. |
| `docker ps` | List running containers. |
| `docker ps -a` | List all containers, including stopped containers. |
| `docker start` | Start an existing stopped container. |
| `docker start -a` | Start an existing container and attach to its output. |
| `docker restart` | Stop and start the same existing container. |
| `docker stop` | Request a graceful stop, then force termination after the timeout if necessary. |
| `docker rename` | Change a container name without changing its ID. |
| `docker rm` | Remove a stopped container. |
| `docker logs` | Show output written by a container process. |
| `docker inspect` | Show detailed Docker object information and state. |

### English–Ukrainian vocabulary

| English | Ukrainian |
|---|---|
| underlying image | базовий вміст image |
| mutable tag | змінюваний tag |
| reference | посилання |
| image digest | точний криптографічний ідентифікатор image |
| short-lived container | короткочасний container |
| long-running container | довготривалий container |
| name conflict | конфлікт назв |
| graceful stop | штатна зупинка |
| forced termination | примусове завершення |
| dependency | залежність |
| lifecycle | життєвий цикл |

### Key takeaways

- Images and containers are separate Docker objects.
- Pulling an image does not create a container.
- `docker run` creates a new container, while `docker start` and `docker restart` reuse an existing one.
- A container's lifetime follows its main process.
- Multiple tags can share the same image ID and layers.
- Stopped containers still reference their images.
- Docker resources should be cleaned in dependency order.
- Logs, status, inspect output, and exit codes provide evidence for troubleshooting.

## Next step

The next lesson is:

**Docker Lesson 03 — Ports and Web Containers**

---

## Docker Lesson 03 — Ports and Web Containers

**Date:** 2026-08-27

In this lesson, I learned how Docker connects host ports to ports inside containers. I practised publishing Nginx on different host addresses and ports, investigated a port conflict, compared exposed and published ports, and verified each configuration with Docker, Linux networking, and HTTP tools.

### Port mapping fundamentals

Containers have isolated network environments. Nginx listens on port `80` inside each Nginx container, but that internal port is not automatically available through a port on the host.

The publishing syntax is:

```text
-p HOST_PORT:CONTAINER_PORT
```

For example, `-p 8080:80` forwards traffic from host port `8080` to port `80` inside the container.

Multiple containers can use the same internal port `80` because each container has its own isolated network environment. However, two containers cannot simultaneously publish the same host IP, host port, and protocol. Different host ports can map to the same container port without a conflict.

### First published container

I first checked whether host port `8080` was free:

```bash
ss -lnt | grep ':8080'
```

Then I created a detached Nginx container:

```bash
docker run -d --name web-all -p 8080:80 nginx:alpine
```

I verified the container, its Docker mapping, the host listener, and the HTTP response with:

```bash
docker ps --filter name=web-all
docker port web-all
ss -lnt | grep ':8080'
curl -I http://127.0.0.1:8080
```

The observed mappings were:

```text
0.0.0.0:8080->80/tcp
[::]:8080->80/tcp
```

The HTTP response included:

```text
HTTP/1.1 200 OK
Server: nginx/1.31.4
```

When `-p` does not include a specific host address, Docker binds the published port to all host interfaces by default. Here, `0.0.0.0` represents all IPv4 host interfaces, and `[::]` represents all IPv6 host interfaces.

### Host-port conflict

I attempted to create another container using the same host port:

```bash
docker run -d --name web-conflict -p 8080:80 nginx:alpine
```

Docker returned:

```text
Bind for 0.0.0.0:8080 failed: port is already allocated
```

The command returned exit code `125`. This meant that Docker could not start the requested container because host port `8080` was already in use by `web-all`.

I inspected the failed container with:

```bash
docker ps -a --filter name=web-conflict
```

It appeared in the `Created` state. Docker had created the container object, but it could not finish the networking setup or start Nginx. I then removed the failed container.

### Two containers using internal port 80

I created a second working Nginx container:

```bash
docker run -d --name web-second -p 8081:80 nginx:alpine
```

Both containers ran simultaneously:

- `web-all`: host `8080` → container `80`;
- `web-second`: host `8081` → container `80`.

Both returned `HTTP/1.1 200 OK`.

There was no conflict because the host ports were different. Each container could listen on its own internal port `80`, while Docker published those ports through separate host ports.

### Localhost-only publishing

I created another container and bound its published port only to the IPv4 loopback address:

```bash
docker run -d --name web-local -p 127.0.0.1:8082:80 nginx:alpine
```

Verification showed:

- `docker port web-local` returned `80/tcp -> 127.0.0.1:8082`;
- `ss` showed the local listening address `127.0.0.1:8082`;
- `curl -I http://127.0.0.1:8082` returned `HTTP/1.1 200 OK`.

The computer's LAN information was:

- interface: `wlp6s0`;
- LAN address: `192.168.0.193`;
- gateway: `192.168.0.1`.

I tested the difference between all-interface and localhost-only publishing:

- `http://192.168.0.193:8080` returned `200 OK` because port `8080` was published on all interfaces;
- `http://192.168.0.193:8082` failed with curl exit code `7` because port `8082` was bound only to `127.0.0.1`.

The binding difference is:

- `0.0.0.0:8080` — accessible through all IPv4 host interfaces, subject to firewall and network rules;
- `127.0.0.1:8082` — accessible only from the local computer.

In `ss` output, the local-address column determines where the socket is bound. A peer column such as `0.0.0.0:*` does not mean that the service listens on every local interface; it describes the possible remote peer for a listening socket.

### Exposed versus published ports

I inspected the Nginx image metadata:

```bash
docker image inspect nginx:alpine --format '{{json .Config.ExposedPorts}}'
```

The result was:

```json
{"80/tcp":{}}
```

Then I created a container without `-p`:

```bash
docker run -d --name web-hidden nginx:alpine
```

The results were:

- the container was running;
- `docker ps` displayed `80/tcp`;
- `docker port web-hidden` returned no mapping.

`EXPOSE 80` is image metadata that describes the expected internal port. It does not publish a host port. A container port becomes accessible through a host port only when it is published with `-p` or `-P`.

### Automatically selected host port

I created a container with uppercase `-P`:

```bash
docker run -d --name web-random -P nginx:alpine
```

For this run, Docker automatically selected host port `32768`:

```text
0.0.0.0:32768->80/tcp
[::]:32768->80/tcp
```

The request:

```bash
curl -I http://127.0.0.1:32768
```

returned `HTTP/1.1 200 OK`.

Uppercase `-P` publishes all ports declared by the image and lets Docker select available host ports. Port `32768` was the result of this run, but Docker is not guaranteed to select the same host port in future runs.

### Recreating a container to change its port mapping

The original `web-hidden` container had no published port. I correctly stopped and removed it, then recreated it with a localhost-only mapping:

```bash
docker run -d --name web-hidden -p 127.0.0.1:8083:80 nginx:alpine
```

Verification showed:

- `127.0.0.1:8083->80/tcp`;
- `docker port web-hidden` returned `80/tcp -> 127.0.0.1:8083`;
- `curl -I http://127.0.0.1:8083` returned `HTTP/1.1 200 OK`.

`docker start` only starts an existing stopped container with its original configuration. It cannot add or change a port mapping. To change the mapping, the container must be removed and recreated with a new `docker run` configuration.

### Useful commands

| Command | Purpose |
|---|---|
| `docker run -p HOST_PORT:CONTAINER_PORT IMAGE` | Create a container and publish a specific host port. |
| `docker run -P IMAGE` | Publish all exposed image ports on automatically selected host ports. |
| `docker port CONTAINER` | Show the published port mappings for a container. |
| `docker ps` | List running containers and their port information. |
| `ss -lnt` | Show listening TCP sockets using numeric addresses and ports. |
| `curl -I URL` | Send an HTTP HEAD request and display response headers. |
| `ip route get ADDRESS` | Show the route, interface, and source address used to reach a destination. |
| `docker stop CONTAINER` | Stop a running container. |
| `docker rm CONTAINER` | Remove a stopped container. |

### Troubleshooting model

When a published web container is unavailable, I can investigate it in this order:

1. Confirm that the container is running with `docker ps`.
2. Inspect its mapping with `docker port`.
3. Check the host listener with `ss -lnt`.
4. Test HTTP locally with `curl -I`.
5. Compare the requested host port with the actual Docker mapping.
6. Check whether the port is bound to all interfaces or only `127.0.0.1`.
7. If the mapping is incorrect or missing, recreate the container.

This order checks the container, Docker configuration, host networking, and application response separately.

### Cleanup

I stopped and removed these containers:

- `web-all`;
- `web-second`;
- `web-local`;
- `web-hidden`;
- `web-random`.

Final verification showed:

- `docker ps -a` contained no containers;
- ports `8080`, `8081`, `8082`, `8083`, and the automatically selected port `32768` were no longer listening;
- images `hello-world:latest` and `nginx:alpine` were intentionally retained.

### Key takeaways

- Container ports belong to isolated container network environments.
- `-p` publishes a chosen host port, while `-P` selects available host ports automatically for exposed image ports.
- Different host ports can map to the same internal container port.
- A host IP, port, and protocol combination can be published by only one container at a time.
- `EXPOSE` documents an internal port but does not publish it.
- The local-address column in `ss` shows whether a service is bound to all interfaces or only localhost.
- Port mappings are part of a container's creation configuration, so changing them requires recreating the container.
- `docker port`, `ss`, and `curl` provide complementary evidence during troubleshooting.

## Next step

The next lesson is:

**Docker Lesson 04 — Container Investigation**

---

# Docker Lesson 04 — Container Investigation

**Date:** 2026-08-28

In this lesson, I investigated a running Nginx container through its logs, processes, filesystem, configuration, runtime state, and resource usage. I also diagnosed an intentionally broken container by comparing its logs, exit code, and inspect data.

### Initial state

Before the lesson:

- the previous commit was `c892cb9 Complete Docker Lesson 03`;
- the Docker service was active;
- no containers existed;
- `nginx:alpine` was available locally;
- `source-backup.tar.gz` remained intentionally untracked.

### Image reference mistake

The first attempt used the incorrect image reference:

```text
nginx-alpine
```

Docker interpreted this as a different repository named `nginx-alpine:latest` and returned a pull-access or repository error.

The correct reference was:

```text
nginx:alpine
```

Here, `nginx` is the image repository or name, and `alpine` is the tag. A colon (`:`) separates the image name from its tag.

### Investigation container

I created the working container with:

```bash
docker run -d --name lesson04-nginx -p 127.0.0.1:8080:80 nginx:alpine
```

Verification showed:

- the container status was `Up`;
- the mapping was `127.0.0.1:8080->80/tcp`;
- `ss` showed a listener on `127.0.0.1:8080`;
- `curl -I http://127.0.0.1:8080` returned `HTTP/1.1 200 OK`;
- the Nginx version was `1.31.4`.

### Container logs

I practised:

```bash
docker logs lesson04-nginx
docker logs --tail 10 lesson04-nginx
docker logs --timestamps --tail 10 lesson04-nginx
docker logs --follow --tail 0 lesson04-nginx
```

I generated HTTP requests with `curl`. The logs showed:

- `GET / HTTP/1.1` returned `200`;
- `GET /missing HTTP/1.1` returned `404`;
- `GET /test-page HTTP/1.1` returned `404`;
- Nginx reported `No such file or directory` for missing files;
- access-log entries included methods such as `GET` and `HEAD`, the requested path, HTTP version, status code, response size, and user-agent `curl/8.5.0`;
- the source address appeared as `172.17.0.1` because traffic reached the container through Docker's bridge network.

Container logs normally contain application output written to standard output (`STDOUT`) and standard error (`STDERR`). `--tail` limits the number of displayed lines, `--timestamps` adds Docker timestamps, and `--follow` displays new log entries in real time. With `--tail 0`, Docker ignores old entries and waits only for new ones. Pressing `Ctrl+C` stops only the local log-following command; it does not stop the container.

### Non-interactive `docker exec`

I ran individual commands inside the running container:

```bash
docker exec lesson04-nginx pwd
docker exec lesson04-nginx whoami
docker exec lesson04-nginx cat /etc/os-release
docker exec lesson04-nginx ls -la /usr/share/nginx/html
```

The results showed:

- the default working directory was `/`;
- the command ran as `root`;
- the container userspace was Alpine Linux `3.24.1`;
- the host remained Ubuntu;
- the Nginx document directory contained `index.html` and `50x.html`;
- these files belonged to `root:root`.

A Linux container shares the host Linux kernel, but it can contain a different userspace, filesystem, libraries, and package manager. This is why an Alpine container can run on an Ubuntu host.

### Interactive `docker exec`

I opened an interactive shell with:

```bash
docker exec -it lesson04-nginx sh
```

The `-i` option keeps standard input open, and `-t` allocates a pseudo-terminal. Alpine normally provides `sh`, not Bash. `docker exec` starts an additional process inside an existing running container, and that process can exist only while the container's PID `1` is running.

Inside the container, I practised:

```bash
pwd
hostname
ps | head -n 10
grep -E 'listen|root|index' /etc/nginx/conf.d/default.conf
exit
```

The investigation verified:

- the hostname matched the short container ID `cc07c8d95cbc`;
- the Nginx master process had container PID `1`;
- worker processes ran as user `nginx`;
- the configuration contained `listen 80` and `listen [::]:80`;
- the document root was `/usr/share/nginx/html`;
- the configuration declared the index files;
- `exit` stopped only the exec shell, not the container.

The `grep` command also displayed commented PHP examples. `grep` searches text patterns; it does not understand Nginx configuration syntax. Lines beginning with `#` are comments and are not active configuration directives.

### PID namespace and `docker top`

I compared container and host process information with:

```bash
docker top lesson04-nginx
docker inspect --format 'HostPID={{.State.Pid}}' lesson04-nginx
ps -fp 6513
```

Inside the container, the Nginx master process was PID `1`, and worker PIDs began at `30`. On the host, the same master process was PID `6513`, its host parent PID was `6488`, and worker host PIDs began at `6607`. The workers had the Nginx master process as their parent.

Docker uses a PID namespace to give the container an isolated view of process numbers. Therefore, the same Nginx master process appeared as PID `1` inside the container and PID `6513` on the host. Host-side usernames can differ because the host resolves numeric UIDs through its own user database; inside the container, the worker UID was named `nginx`.

### Structured `docker inspect`

I used Go templates to extract individual fields from `docker inspect`:

- `.Name`;
- `.Config.Image`;
- `.State.Status`;
- `.State.Running`;
- `.State.Pid`;
- `.State.ExitCode`;
- `.NetworkSettings.Networks`;
- `.NetworkSettings.Ports`.

Verified values included:

- name `/lesson04-nginx`;
- image `nginx:alpine`;
- status `running`;
- `Running=true`;
- host PID `6513`;
- container IP `172.17.0.2`;
- host mapping `127.0.0.1:8080` to `80/tcp`.

`docker inspect` returns detailed, low-level JSON data about a Docker object. `--format` extracts selected fields using Go templates, while `{{json ...}}` presents nested values as JSON.

Configuration fields such as the image name are relatively static. Runtime fields such as PID, status, and IP address can change. An exit code becomes most meaningful after the container's main process stops.

### Resource monitoring

I practised:

```bash
docker stats lesson04-nginx
docker stats --no-stream lesson04-nginx
```

A Bash loop generated 100 local HTTP requests. The observed snapshot included:

- maximum noticed CPU usage: approximately `0.03%`;
- final CPU usage: `0.00%`;
- memory usage: approximately `20.6 MiB`;
- memory percentage: `0.13%`;
- network I/O: approximately `65.8kB / 152kB`;
- block I/O: approximately `8.01MB / 20.5kB`;
- PIDs: `17`.

The main columns mean:

| Column | Meaning |
|---|---|
| `CPU %` | The container's current CPU usage. |
| `MEM USAGE / LIMIT` | Memory currently used and the available limit. |
| `MEM %` | The percentage of the memory limit in use. |
| `NET I/O` | Network data received and sent. |
| `BLOCK I/O` | Data read from and written to block devices. |
| `PIDS` | The number of processes and threads counted for the container. |

Normal `docker stats` continuously streams live data. `docker stats --no-stream` returns one snapshot and exits. Pressing `Ctrl+C` stops monitoring without stopping the container.

A typo added `~` to the container name:

```text
lesson04-nginx~
```

Docker correctly returned `No such container` because `~` became a literal part of the requested name. The real container was unaffected, and the command succeeded after the correct name was used.

### Broken-container troubleshooting

I intentionally created a broken container:

```bash
docker run --name lesson04-broken nginx:alpine nginx -g 'invalid_directive;'
```

Docker created the container, but Nginx reported:

```text
unknown directive "invalid_directive" in command line
```

The command returned exit status `1`, and the container status became `Exited (1)`. `docker logs lesson04-broken` contained the application error. Inspection showed:

```text
Status=exited
ExitCode=1
Error=""
OOMKilled=false
```

Docker successfully created the container and started its process. The application itself then failed. Application errors appeared in `docker logs`, while `.State.Error` remained empty because there was no Docker runtime-level launch error. `OOMKilled=false` proved that memory exhaustion was not the cause.

My final diagnosis was:

> The container exited because Nginx received an invalid directive. `docker logs` showed the error, and the main process returned exit code 1.

### Commands available for stopped containers

I tried:

```bash
docker exec lesson04-broken sh
```

Docker reported that the container was not running, and the command returned exit status `1`.

- `docker logs` can inspect a stopped container.
- `docker inspect` can inspect a stopped container.
- `docker exec` requires a running container.

### Troubleshooting workflow

I can investigate a container in this order:

1. Check state with `docker ps -a`.
2. Read application output with `docker logs`.
3. Inspect `.State.Status`, `.State.ExitCode`, `.State.Error`, and `.State.OOMKilled`.
4. If running, inspect processes with `docker top`.
5. If running, execute diagnostic commands with `docker exec`.
6. Inspect configuration and networking with `docker inspect`.
7. Check resource usage with `docker stats`.
8. Identify whether the problem belongs to Docker, the application, configuration, resources, or networking.

### Command reference

| Command | Purpose |
|---|---|
| `docker logs CONTAINER` | Show the container's available application logs. |
| `docker logs --tail N CONTAINER` | Show only the last `N` log lines. |
| `docker logs --timestamps CONTAINER` | Add Docker timestamps to log entries. |
| `docker logs --follow CONTAINER` | Follow new log entries in real time. |
| `docker exec CONTAINER COMMAND` | Run one additional command in a running container. |
| `docker exec -it CONTAINER sh` | Open an interactive shell in a running container. |
| `docker top CONTAINER` | Show the container's processes from the host view. |
| `docker inspect --format TEMPLATE CONTAINER` | Extract selected low-level fields with a Go template. |
| `docker stats CONTAINER` | Stream live resource-usage information. |
| `docker stats --no-stream CONTAINER` | Display one resource-usage snapshot. |

### Cleanup

I stopped the running investigation container and then removed:

- `lesson04-nginx`;
- `lesson04-broken`.

Final verification showed:

- `docker ps -a` contained no containers;
- host port `8080` was no longer listening;
- `nginx:alpine` remained available locally;
- `source-backup.tar.gz` remained intentionally untracked and unchanged.

### Key takeaways

- Logs show application output from `STDOUT` and `STDERR`.
- `docker exec` runs an additional command only inside a running container.
- Containers share the host kernel but can use a different userspace and filesystem.
- PID namespaces give a process different container-side and host-side PIDs.
- `docker inspect --format` extracts useful configuration and runtime fields.
- `docker stats` shows live or snapshot resource usage.
- Logs, state, exit codes, processes, configuration, and resource data should be compared before choosing a fix.

## Next step

The next lesson is:

**Docker Lesson 05 — Container Lifecycle**

---

# Docker Lesson 05 — Container Lifecycle

**Date:** 2026-09-01
**Started:** 2026-08-29

In this lesson, I practised the complete container lifecycle and investigated how stopping, starting, removing, and recreating containers affect container identity and filesystem changes.

### Initial state

Before the lesson:

- the previous commit was `10f5a96 Complete Docker Lesson 04`;
- the Docker service was active;
- no containers existed;
- `nginx:alpine` was available locally;
- `source-backup.tar.gz` remained intentionally untracked.

### Creating the initial container

The intended command was:

```bash
docker run -d --name lesson05-web -p 127.0.0.1:8080:80 nginx:alpine
```

The first attempt incorrectly used:

```text
127.0.0.1:8080.80
```

Docker returned:

```text
invalid containerPort: 8080.80
```

In a port mapping, a colon separates the host port from the container port. A period cannot be used in its place.

The corrected container:

- was named `lesson05-web`;
- used `nginx:alpine`;
- had full ID `20af586c4b8e1c5a235b3c61dcb654bebff930eba2cd4fb42bbfebbe8644a014`;
- published `127.0.0.1:8080` to container port `80`.

The first `curl` request omitted `:8080`, so `curl` tried host port `80` and returned exit code `7`. The corrected request to `127.0.0.1:8080` returned HTTP `200`.

### Container writable layer

I created this marker file inside the container:

```text
/usr/share/nginx/html/marker.txt
```

Its content was:

```text
Created during Docker Lesson 05
```

The file was accessible over HTTP and belonged to `root:root`.

`docker diff lesson05-web` showed:

```text
A /usr/share/nginx/html/marker.txt
```

`A` means that the file was added. It existed in the container's writable layer and was not part of the original `nginx:alpine` image. Other runtime changes reported by `docker diff` came from normal Nginx startup activity.

### Stop and resume

I paused the lesson after running:

```bash
docker stop lesson05-web
```

Three days later:

- Docker was active;
- `lesson05-web` existed with status `Exited (0)`;
- its full container ID remained unchanged;
- `docker diff` still showed the marker file.

Stopping a container stops its main process, but it does not delete the container object or its writable layer.

### Start and restart

I started the existing container with:

```bash
docker start lesson05-web
```

Verification showed:

- the short ID remained `20af586c4b8e`;
- the original creation time remained unchanged;
- `StartedAt` changed;
- the marker file remained accessible.

I then restarted the same container:

```bash
docker restart lesson05-web
```

The full ID remained unchanged, `StartedAt` changed from approximately `22:28` to `22:35`, and `marker.txt` survived. Both `start` and `restart` preserve the existing container and its writable layer.

### Remove and recreate

I stopped and removed the container normally:

```bash
docker stop lesson05-web
docker rm lesson05-web
```

After removal:

- `docker ps -a` no longer showed the container;
- `curl` to port `8080` returned exit code `7`;
- the image remained available.

I created a new container with the same name, image, and port mapping. Verification showed:

- new full ID: `1eb1e3f6459eb696d03675df0adc67d446095d0fde4adefa29326af8417f77ca`;
- the new ID differed from the original ID;
- the image ID remained `db35bfc6b295`;
- `/marker.txt` returned HTTP `404`;
- `docker diff lesson05-web | grep marker` returned exit status `1` because no matching change existed.

Container names may be reused after removal, but a reused name does not mean that it is the same container. `docker rm` deleted the old writable layer. The unchanged image did not contain `marker.txt`, so recreation produced a new container ID and a clean writable layer.

Immediately after recreation, the first `curl` request returned exit code `56`, `Connection reset by peer`, and HTTP status `000`. A retry returned HTTP `404`. This was a startup race: a container can have status `running` before the application inside it is fully ready to accept requests.

### Removing running containers

Running this command while the container was active failed with exit status `1`:

```bash
docker rm lesson05-web
```

Docker reported that the container must first be stopped or force-removed, and the container remained running.

I then intentionally force-removed the disposable training container:

```bash
docker rm -f lesson05-web
```

Normal `docker rm` removes a stopped container. The safe normal sequence is `docker stop` followed by `docker rm`. `docker rm -f` force-removes a running container using `SIGKILL`, so it should be intentional: the application cannot perform a graceful shutdown.

After force removal, no `lesson05-web` container existed, port `8080` was unavailable, and `nginx:alpine` remained available.

### `docker create` versus `docker run`

I created a container without starting it:

```bash
docker create --name lesson05-created -p 127.0.0.1:8080:80 nginx:alpine
```

Verification showed:

- full ID: `44f5bd2e222393a30354839b39bcb84169711e02f536e50a5947764b0a4f1194`;
- status `Created`;
- `curl` exit code `7`;
- no application accepting connections on port `8080`.

I then started the existing container:

```bash
docker start lesson05-created
```

The ID was unchanged before and after `docker start`, the status changed from `created` to `running`, the saved port mapping became active, and Nginx returned HTTP `200`.

The lifecycle model is:

```text
docker run = docker create + docker start
```

`docker start` starts an existing created or stopped container. `docker run` creates and starts a new container from an image.

### Automatic removal with `--rm`

I ran a temporary container with:

```bash
docker run --rm --name lesson05-auto nginx:alpine nginx -v
```

The Nginx image entrypoint ran, Nginx printed version `1.31.4`, and the command returned exit status `0`. After the main process finished, `lesson05-auto` did not appear in `docker ps -a`.

The `--rm` option automatically removes a container after its main process exits. It does not delete the image.

### Independent final challenge

I independently:

1. created `lesson05-challenge` without starting it;
2. verified status `Created`;
3. started it with `docker start`;
4. received HTTP `200` from Nginx;
5. stopped it normally;
6. removed it normally;
7. verified that `docker ps -a` showed no containers;
8. verified that Docker images remained available.

The challenge container ID began with `92adec...`.

Two harmless command mistakes occurred during the challenge.

First, this filter was incomplete:

```bash
docker ps -a --filter=lesson05-challenge
```

Docker filters require `key=value`. The correct form is:

```bash
docker ps -a --filter name=lesson05-challenge
```

Second, this command accidentally passed `ss` to `curl` as another address:

```bash
curl ss --connect-timeout 3 http://127.0.0.1:8080/
```

`curl` returned exit code `6` for the unresolved host `ss`, then exit code `7` for the unavailable local port. The intended Linux command was:

```bash
ss -lnt | grep ':8080'
```

### Lifecycle command model

| Command | Purpose |
|---|---|
| `docker create` | Create a container without starting it. |
| `docker start` | Start an existing stopped or created container. |
| `docker run` | Create and start a new container from an image. |
| `docker stop` | Gracefully stop a running container. |
| `docker restart` | Stop and start the same container. |
| `docker rm` | Remove a stopped container. |
| `docker rm -f` | Force-remove a running container. |
| `docker run --rm` | Automatically remove the container after its process exits. |
| `docker diff` | Show filesystem changes in the writable layer. |

The important lifecycle rules are:

- stop, start, and restart preserve the same container and writable layer;
- remove and recreate produce a new ID and a clean writable layer;
- data stored only in the writable layer is temporary;
- persistent storage will be introduced with bind mounts and Docker volumes.

### Final state

Final verification showed:

- `docker ps -a` contained no containers;
- `curl` to `127.0.0.1:8080` returned exit code `7`;
- `hello-world:latest` and `nginx:alpine` remained available;
- no images were removed;
- no training container remained.

### Key takeaways

- A stopped container keeps its identity, configuration, and writable layer.
- Starting or restarting reuses the same container.
- Removing a container deletes its writable layer, while its image remains independent.
- Recreating with the same name creates a different container with a clean writable layer.
- A `running` state does not guarantee that the application is ready yet.
- Normal stop-and-remove is safer than force removal because it permits graceful shutdown.

## Next step

The next lesson is:

**Docker Lesson 06 — Bind Mounts**

---

# Docker Lesson 06 — Bind Mounts

**Date:** 2026-09-04
**Started:** 2026-09-02

In this lesson, I learned how bind mounts connect existing host files and directories to containers. I practised changes in both directions, read-only access, container recreation, missing-source behaviour, host permissions, and systematic troubleshooting.

### Bind-mount concept

A bind mount exposes an existing host file or directory at a path inside a container.

The host and container paths do not contain separate copies. While the mount is active, both paths provide access to the same underlying host data.

The explicit syntax is:

```text
--mount type=bind,source=<host-path>,target=<container-path>
```

Its parts mean:

- `type=bind` selects a bind mount;
- `source` identifies the real host path;
- `target` identifies where that path appears inside the container.

Changes can become visible immediately without restarting the container. The data lifecycle belongs to the host and is independent of the container lifecycle.

### Initial host content

The temporary host directory was:

```text
/tmp/docker-lesson06-site
```

It contained an `index.html` file created by the Ubuntu user. I created the first container with:

```bash
docker run -d --name lesson06-nginx -p 127.0.0.1:8080:80 --mount type=bind,source=/tmp/docker-lesson06-site,target=/usr/share/nginx/html nginx:alpine
```

Inspection verified:

- mount type `bind`;
- source `/tmp/docker-lesson06-site`;
- destination `/usr/share/nginx/html`;
- `RW=true`;
- port mapping `127.0.0.1:8080->80/tcp`.

Nginx successfully served the host's `index.html`.

### Recovery after the lesson pause

The container was stopped but not removed before the lesson paused. When the lesson resumed:

- the container still existed with status `Exited (0)`;
- its original short ID was `0693df042608`;
- its bind-mount configuration still referenced `/tmp/docker-lesson06-site`;
- the source directory had disappeared because it was stored under `/tmp`.

Docker preserved the container metadata, but it did not manage or back up the host bind source. Temporary directories may be cleaned during a reboot or system maintenance.

I recreated the host directory and file before starting the existing container. The first immediate `curl` after `docker start` returned a connection reset. A repeated request succeeded.

A running container is not necessarily an application that is ready to accept requests. Docker can report the container as running as soon as its main process starts, while Nginx still needs a short time to initialize and begin serving connections.

### Live host-to-container changes

I changed the host's `index.html` to contain:

- heading: `Updated from Ubuntu`;
- paragraph: `No container restart was needed.`

The new content appeared immediately:

- in the host file;
- through `curl`;
- through `docker exec` at `/usr/share/nginx/html/index.html`.

Docker did not copy the updated file. The container read the host file directly through the bind mount.

### Container-to-host changes

Because the mount had `RW=true`, I created a file through the container path:

```bash
docker exec lesson06-nginx sh -c 'printf "Created from inside the container\n" > /usr/share/nginx/html/from-container.txt'
```

The file immediately appeared on the host as:

```text
/tmp/docker-lesson06-site/from-container.txt
```

Nginx also served it successfully. This was one host file visible through both the host path and the container path.

The file created through `docker exec` belonged to `root:root`, while the original host-created file belonged to `artem:artem`. Bind mounts expose real Linux ownership and permissions, which are based on numeric UID and GID values. User names are how each system maps those numeric identifiers for display.

### Bind mounts and `docker diff`

This check produced no matching paths and `grep` exit status `1`:

```bash
docker diff lesson06-nginx | grep -E 'index.html|from-container.txt'
```

Bind-mounted changes are external to the container's writable layer. Therefore, `docker diff` does not report them as writable-layer file changes. Here, `grep` status `1` meant that it found no matching lines; it did not mean that the bind-mounted files were missing.

### Container removal and persistence

I stopped and removed the first container. After removal:

- `docker ps -a` no longer showed the container;
- both host files still existed;
- their contents remained unchanged.

I created a new container with the same name and bind source. Its new ID began with `c3465567d6fe`, but it immediately served the existing host files.

Removing and recreating a container produces a new container identity. Bind-mounted host data can remain available because its lifecycle belongs to the host, not to the removed container.

### Docker run ordering mistake

An attempted recreation omitted `--name` and placed Docker options after the first non-option argument. Docker interpreted `lesson06-nginx` as the image name and attempted to pull `lesson06-nginx:latest`.

The command structure is:

```text
docker run [DOCKER OPTIONS] IMAGE [CONTAINER COMMAND]
```

Options such as `-d`, `--name`, `-p`, and `--mount` must appear before the image reference. After the image, Docker treats the remaining arguments as the command and arguments for the container.

### Read-only bind mounts

I created a read-only container using:

```text
--mount type=bind,source=/tmp/docker-lesson06-site,target=/usr/share/nginx/html,readonly
```

Inspection showed:

```text
Type=bind RW=false
```

The container could read and serve the existing files. An attempted write through the mounted container path failed with:

```text
Read-only file system
```

The `docker exec` command returned exit status `1`, and host verification confirmed that `blocked.txt` did not exist.

The Ubuntu user could still change the host's `index.html`. The updated content immediately appeared through Nginx and inside the container.

The `readonly` option prevents writes through the container's mounted path. It does not prevent authorized host users from changing the source files directly.

### Missing source with `--mount`

I intentionally tested this missing source:

```text
/tmp/docker-lesson06-does-not-exist
```

Docker returned:

```text
invalid mount config for type "bind": bind source path does not exist
```

Verification showed:

- `docker run` returned exit status `125`;
- no container named `lesson06-missing` was created;
- the application inside the image never started.

Exit status `125` indicates that `docker run` failed before the containerized application could run.

### Difference between `--mount` and `-v`

I tested the short `-v` syntax with a missing host source:

```text
-v /tmp/docker-lesson06-v-created:/usr/share/nginx/html
```

Unlike `--mount`, `-v` automatically created the missing directory. Verification showed:

- the directory was created as `root:root`;
- mount type was `bind`;
- `RW=true`;
- Nginx returned HTTP `403`.

The newly created host directory was empty. Mounting it over `/usr/share/nginx/html` obscured the image's existing files at that path, including its normal `index.html`. The original image files were hidden by the mount, not deleted.

Nginx returned `403 Forbidden` because the mounted directory contained no index file and directory listing was disabled.

`--mount` is generally clearer and safer because a source-path typo produces an immediate error instead of silently creating an empty directory.

### Host permissions troubleshooting

The normal `artem` user initially could not create `index.html` in the directory automatically created by `-v`. The write returned:

- `Permission denied`;
- exit status `1`.

The directory belonged to `root:root` and had mode `755`. A non-root user could read and enter it but could not create files there.

I corrected ownership with:

```bash
sudo chown "$USER":"$(id -gn)" /tmp/docker-lesson06-v-created
```

Afterward:

- the directory belonged to `artem:artem`;
- creating `index.html` returned exit status `0`;
- the new file belonged to `artem:artem`;
- Nginx immediately changed from HTTP `403` to HTTP `200`;
- no container restart was required.

Bind-mount problems can come from ordinary host filesystem ownership and permissions, not only from Docker configuration.

### Final challenge

The independent challenge used:

- container name `lesson06-challenge`;
- host port `127.0.0.1:8081`;
- container port `80`;
- source `/tmp/docker-lesson06-site`;
- target `/usr/share/nginx/html`;
- read-only access;
- image `nginx:alpine`.

Verification showed:

- the container was running;
- `curl -I` returned `HTTP/1.1 200 OK`;
- inspect showed `Type=bind RW=false`;
- attempting to create `challenge-write.txt` failed with `Read-only file system`;
- `docker exec` returned exit status `1`;
- the file did not appear on the host;
- the host `ls` check returned exit status `2`.

I also tried:

```bash
docker ps lesson06-challenge
```

Docker rejected it because `docker ps` does not accept a container name as a positional argument. The correct name-specific form is:

```bash
docker ps --filter name=lesson06-challenge
```

### Practical troubleshooting model

I can troubleshoot a bind mount in this order:

1. Verify that the host source path exists.
2. Inspect its owner and permissions.
3. Check the container status and port mapping.
4. Inspect `.Mounts` to confirm type, source, destination, and `RW`.
5. Test the host file directly.
6. Test the mounted path with `docker exec`.
7. Test the application with `curl`.
8. Check whether the mount is intentionally read-only.
9. Remember that a mounted directory can hide existing image files.
10. Prefer `--mount` when strict missing-source validation is useful.

### Cleanup and final state

I removed these containers:

- `lesson06-nginx`;
- `lesson06-readonly`;
- `lesson06-v-created`;
- `lesson06-challenge`.

After verifying their exact paths, I removed these disposable host directories:

- `/tmp/docker-lesson06-site`;
- `/tmp/docker-lesson06-v-created`.

Final verification showed:

- `docker ps -a` contained no containers;
- ports `8080` and `8081` were not listening;
- both temporary directories no longer existed;
- `nginx:alpine` remained available locally;
- its image ID was `db35bfc6b295`;
- `git status --short` produced no output.

### Key takeaways

- A bind mount exposes real host data through a container path instead of copying it.
- Host and container writes can be visible immediately when the mount is read-write.
- Bind-mounted data survives container removal when it remains on the host.
- Linux ownership and permissions apply to bind-mounted files.
- Read-only access blocks writes through the container but not authorized host changes.
- Bind-mounted changes do not belong to the container writable layer.
- `--mount` rejects a missing source, while `-v` can create an empty host directory.
- A mounted directory hides the image content at the same container path while the mount is active.

## Next step

The next lesson is:

**Docker Lesson 07 — Docker Volumes**

---

# Docker Lesson 07 — Named Volumes

**Date:** 2026-09-05

In this lesson, I learned how Docker manages named volumes. I practised persistence after container removal, shared data, read-only attachments, automatic volume creation, and cleanup.

### Initial state

The verified starting state was:

- initial HEAD: `a18927f Add project state and refresh roadmap`;
- previous Docker lesson commit: `648f79e Complete Docker Lesson 06`;
- the Git working tree was clean;
- no containers existed;
- no Docker volumes existed.

The Microsoft Dev Containers and Container Tools extensions were installed in VS Code. I continued with Docker CLI commands to develop command-line understanding.

### Named-volume concept

A named volume is an independent Docker storage object. I supply a volume name instead of an ordinary host path, and Docker manages its physical storage location.

Containers and named volumes have separate lifecycles. Removing a container does not automatically remove its named volume. Named volumes are normally managed through Docker commands instead of manually editing their internal host directories.

### Creating and inspecting a volume

I practised:

```bash
docker volume create lesson07-data
docker volume ls
docker volume inspect lesson07-data
```

Inspection verified:

```text
Name: lesson07-data
Driver: local
Mountpoint: /var/lib/docker/volumes/lesson07-data/_data
Scope: local
Options: null
Labels: null
```

Creating the volume did not create a container. The volume existed independently and was initially empty.

### Attaching a named volume

I created the first Nginx container with:

```bash
docker run -d \
  --name lesson07-nginx \
  -p 127.0.0.1:8080:80 \
  --mount type=volume,source=lesson07-data,target=/usr/share/nginx/html \
  nginx:alpine
```

Here, `type=volume` selects a Docker volume, `source` is its name, and `target` is the path where it appears inside the container. The port mapping exposes Nginx on localhost port `8080`.

Inspection verified:

```text
Type=volume
Name=lesson07-data
Destination=/usr/share/nginx/html
RW=true
```

The first immediate `curl` attempt returned `Recv failure: Connection reset by peer`. The container was running before Nginx was fully ready. A retry returned `HTTP/1.1 200 OK`.

The image's target directory already contained `index.html` and `50x.html`. During the first attachment, Docker copied those existing files into the empty named volume.

This differed from Lesson 06: an empty bind-mounted host directory obscured the existing Nginx files and produced HTTP `403`. An empty named volume normally receives the target directory's initial contents instead.

### Writing data

Through the container, I replaced `/usr/share/nginx/html/index.html` with:

```html
<h1>Lesson 07 Named Volume</h1>
<p>This data lives in lesson07-data.</p>
```

`curl` immediately returned the custom page. The write command used a path inside the container, but the resulting data was stored in `lesson07-data` because that path was inside the mounted volume.

### Persistence after container removal

The original container ID began with `77505c9d085d`. I removed it with:

```bash
docker rm -f lesson07-nginx
```

Verification showed:

- `docker ps -a` no longer showed the container;
- `docker volume ls` still showed `lesson07-data`;
- `curl` could not connect to port `8080` and returned exit status `7` because no web container was running.

I created a new container named `lesson07-restored` with the same volume and host port `8080`. Its ID began with `cf8f060da71a`. Although this was a different container, `curl` returned the previously modified custom page.

The data survived because it belonged to the named volume, not to the deleted container. Because the existing volume was no longer empty, Docker did not overwrite its modified `index.html` with the image's default page.

### Sharing a volume

I created a second Nginx container named `lesson07-second` on host port `8081`, attached to the same `lesson07-data` volume with `RW=true`.

Verification showed:

- `lesson07-restored` served the page through port `8080`;
- `lesson07-second` served the same page through port `8081`;
- both containers mounted `lesson07-data`.

Through `lesson07-second`, I changed the index page to:

```html
<h1>Changed by the second container</h1>
<p>One volume, two containers.</p>
```

The new content immediately appeared through both ports `8081` and `8080`, and when I read the file with `docker exec` inside `lesson07-restored`.

Both container paths referred to the same underlying volume data. No restart or copy was required.

Sharing a volume does not guarantee that every application can safely perform concurrent writes. Applications such as databases require appropriate coordination and application support.

### Read-only named-volume attachment

I created a third container with:

```bash
docker run -d \
  --name lesson07-readonly \
  -p 127.0.0.1:8082:80 \
  --mount type=volume,source=lesson07-data,target=/usr/share/nginx/html,readonly \
  nginx:alpine
```

Inspection showed:

```text
Volume=lesson07-data
RW=false
```

The container could read and serve the shared page. During the write challenge, an attempt to create `blocked.txt` through the read-only attachment failed with:

```text
Read-only file system
```

`docker exec` returned exit status `1`. The file was not created, and checking for it inside the writable container also returned exit status `1`.

`readonly` applies to one particular volume attachment. Other containers mounting the same volume with `RW=true` can still modify its data.

### Protection against removing an in-use volume

I ran:

```bash
docker volume rm lesson07-data
```

Docker refused because three containers were using the volume. The command returned exit status `1` and listed their container IDs.

I identified all running containers using the volume with:

```bash
docker ps --filter volume=lesson07-data
```

Normal `docker volume rm` protects an attached volume from accidental deletion. A container reference prevents removal even if that container is stopped; stopping a container does not remove its attachment configuration.

### Automatic named-volume creation

I started a one-shot container with a previously nonexistent named volume:

```bash
docker run \
  --name lesson07-auto \
  --mount type=volume,source=lesson07-auto-data,target=/data \
  nginx:alpine \
  sh -c 'printf "Created in an automatically created volume\n" > /data/note.txt'
```

Verification showed:

- Docker automatically created `lesson07-auto-data`;
- the container wrote `note.txt` and exited with status `0`;
- both `lesson07-data` and `lesson07-auto-data` appeared in `docker volume ls`.

I read the file with a temporary container using the shorter syntax:

```bash
docker run --rm \
  -v lesson07-auto-data:/data:ro \
  nginx:alpine \
  cat /data/note.txt
```

The output was:

```text
Created in an automatically created volume
```

In `-v lesson07-auto-data:/data:ro`, the three parts are the volume name, container target path, and read-only mode.

`--rm` removed the temporary container after `cat` finished. It did not remove the named volume.

A missing named volume is automatically created. This differs from `--mount type=bind` with a missing host source, which normally returns an error.

### Cleanup

I explicitly removed these containers:

- `lesson07-restored`;
- `lesson07-second`;
- `lesson07-readonly`;
- `lesson07-auto`.

I then explicitly removed these named volumes:

- `lesson07-data`;
- `lesson07-auto-data`.

Final practical verification showed:

- no Lesson 07 containers remained;
- `docker volume ls` contained no volumes;
- ports `8080`, `8081`, and `8082` were no longer listening;
- the port `grep` command returned exit status `1`, meaning no matching listening ports were found;
- `git status --short` remained empty before documenting the lesson.

### Key takeaways

| Storage behaviour | Bind mount | Named volume |
|---|---|---|
| Storage location | The user selects a host path. | Docker manages the storage location. |
| Empty source mounted over a populated target | The image files are obscured. | Docker normally copies the target's initial contents into the volume. |

- Removing a container does not automatically remove its named volume.
- A named volume can be reused by replacement containers.
- Multiple containers can mount the same volume.
- `readonly` controls the access mode of a particular attachment.
- Docker refuses to remove a volume that is still referenced by a container.
- `--rm` removes the temporary container but does not remove a named volume.

## Next step

The next lesson follows environment variables after volumes in `ROADMAP.md`:

**Docker Lesson 08 — Environment Variables**
