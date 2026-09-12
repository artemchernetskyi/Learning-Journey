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

---

# Docker Lesson 08 — Environment Variables

**Date:** 2026-09-06

In this lesson, I learned how to pass runtime configuration into containers. I practised exported variables, environment files, overrides, required values, configurable Nginx startup, and troubleshooting missing configuration.

### Initial state

The verified starting state was:

- previous commit: `32aa57b Complete Docker Lesson 07`;
- local `main` and `origin/main` were synchronized;
- `git status --short` was empty;
- no containers existed;
- `docker image ls alpine` showed no local image whose repository was exactly `alpine`;
- `nginx:alpine` remained available locally.

### Bash variables and exported environment variables

I practised:

```bash
unset LESSON_MESSAGE
LESSON_MESSAGE="Hello from the host shell"
printf '%s\n' "$LESSON_MESSAGE"
bash -c 'printf "%s\n" "$LESSON_MESSAGE"'
export LESSON_MESSAGE
bash -c 'printf "%s\n" "$LESSON_MESSAGE"'
```

The current shell could read the normal Bash variable. Before export, the child Bash process printed an empty value. After export, a newly started child Bash process received `Hello from the host shell`.

A normal shell variable belongs to the current shell. `export` marks it for inheritance by newly started child processes; it does not automatically send it into Docker containers.

The single quotes around the `bash -c` command prevented the host shell from expanding `$LESSON_MESSAGE`. The child shell therefore read the value from its own environment.

### Passing host variables into containers

The `alpine:3.24` image was pulled for this lesson. I compared:

```bash
docker run --rm alpine:3.24 sh -c 'printf "%s\n" "$LESSON_MESSAGE"'
docker run --rm -e LESSON_MESSAGE alpine:3.24 sh -c 'printf "%s\n" "$LESSON_MESSAGE"'
```

Without `-e`, the container printed an empty value. With `-e LESSON_MESSAGE`, Docker copied the exported host value, and the container printed `Hello from the host shell`.

Docker does not automatically copy the complete host environment into a container. Variables must be passed explicitly. `--rm` removed each temporary container after its command finished.

### Explicit container variables

I created a long-running container with:

```bash
docker run -d --name lesson08-env -e APP_ENV=development -e APP_PORT=8080 -e WELCOME_MESSAGE="Hello from Lesson 08" alpine:3.24 sleep 3600
```

Verification showed:

- short container ID: `889d93a354ca`;
- status: `Up`;
- `APP_ENV=development`;
- `APP_PORT=8080`;
- `WELCOME_MESSAGE=Hello from Lesson 08`;
- `docker inspect` showed the custom variables in `.Config.Env`;
- `PATH` was also present because it came from the image;
- the `PORTS` column was empty.

`APP_PORT=8080` is only a string containing configuration data. It does not publish a port. Docker port publishing still requires `-p`, and the application must actually read and use the variable.

### Host and container environment separation

After the container had been created, I changed the host's `APP_ENV` to `production`.

Verification showed:

- the host printed `APP_ENV=production`;
- a normal `docker exec` still printed `development`;
- `docker exec -e APP_ENV=testing` printed `testing` for that process;
- the next normal `docker exec` returned to `development`;
- `docker inspect` still showed `APP_ENV=development`.

A container's configured environment is fixed when the container is created. Changing a host variable does not update an existing container. `docker exec -e` overrides a value only for that additional exec process. Permanently changing the configuration normally requires recreating the container.

### Environment files

The temporary host file `/tmp/docker-lesson08.env` contained:

```text
APP_ENV=staging
APP_PORT=9090
WELCOME_MESSAGE=Loaded from an environment file
FEATURE_FLAG=true
```

I used it with this command structure, followed by the container's checking command:

```text
docker run --rm --env-file /tmp/docker-lesson08.env alpine:3.24 ...
```

All four values were available inside the container. The value containing spaces remained intact, but the environment file itself did not exist inside the container.

Docker reads the host file and passes its values. It does not automatically copy or mount the file into the container.

Environment variable values are strings. The application decides whether a string such as `true` represents a Boolean option.

### Precedence and default values

I combined the environment file with these explicit options:

```text
-e APP_ENV=production -e APP_PORT=7070
```

Verification showed:

- `APP_ENV=production` replaced `staging` from the file;
- `APP_PORT=7070` replaced `9090` from the file;
- `WELCOME_MESSAGE` remained `Loaded from an environment file` because it was not overridden.

Explicit command-line `-e` values override matching `--env-file` values.

Default-value tests showed:

- an unset `OPTIONAL_SETTING` printed as empty;
- `${OPTIONAL_SETTING:-safe-default}` produced `safe-default`;
- after passing `-e OPTIONAL_SETTING=provided`, the expression used `provided`.

`${VAR:-default}` uses a fallback when the value is missing or empty.

### Required variables and fail-fast behaviour

The required-variable expression was:

```bash
${REQUIRED_SETTING:?REQUIRED_SETTING must be provided}
```

Without `REQUIRED_SETTING`, the shell reported the error and `docker run` returned exit status `2`. The following `printf` command did not execute.

With `-e REQUIRED_SETTING=ready`, the command printed `ready` and returned exit status `0`.

`${VAR:?error}` stops the shell when a required value is missing or empty. This fail-fast behaviour helps automation stop immediately with a useful configuration error instead of continuing with incomplete settings.

### Configurable Nginx service

I started a real Nginx container from `nginx:alpine` with:

- name: `lesson08-web`;
- port mapping: `127.0.0.1:8080:80`;
- `APP_ENV=production`;
- `PAGE_TITLE="Lesson 08 Environment Variables"`.

The startup shell:

1. Validated `APP_ENV` and `PAGE_TITLE` as required values.
2. Generated `/usr/share/nginx/html/index.html` from the variables.
3. Used `exec nginx -g "daemon off;"` to replace the shell with Nginx as the main container process.

Verification showed:

- short container ID: `30961e8591ec`;
- status: `Up`;
- `docker inspect` showed `APP_ENV`, `PAGE_TITLE`, and image-provided variables such as `PATH` and `NGINX_VERSION`.

`curl` returned:

```html
<h1>Lesson 08 Environment Variables</h1>
<p>Environment: production</p>
```

`-e` configures a process, while `-p` publishes a port. These settings are independent. `exec` made Nginx replace the startup shell and become the main container process.

### Recreating the same image with different configuration

The temporary file `/tmp/docker-lesson08-web.env` contained:

```text
APP_ENV=staging
PAGE_TITLE=Same Image, New Configuration
```

The first attempt to remove the production container accidentally used:

```text
docker rm -f lesson08-web\
```

The trailing backslash continued the command onto the next line, so the following `docker run -d` became part of `docker rm`. Docker returned:

```text
unknown shorthand flag: 'd' in -d
```

Removal failed: the old and new inspected IDs were identical, and the original production page remained available.

I corrected the removal command to:

```bash
docker rm -f lesson08-web
```

Removal succeeded with exit status `0`, and the filtered container list was empty. I then recreated the service from the same `nginx:alpine` image using the staging environment file.

The new short container ID was `511f5a0a1af0`. The old and new IDs were different, and `curl` returned:

```html
<h1>Same Image, New Configuration</h1>
<p>Environment: staging</p>
```

The same image can be reused for development, staging, and production by supplying different runtime configuration. Applying changed configuration through recreation creates a new container without requiring changes to the image.

A trailing backslash should be used only when intentionally continuing one command across multiple lines.

### Missing-variable troubleshooting challenge

The file `/tmp/docker-lesson08-broken.env` contained only:

```text
APP_ENV=testing
```

The intentionally broken container required both `APP_ENV` and `PAGE_TITLE`, but `PAGE_TITLE` was missing.

Verification showed:

- `docker run` returned exit status `2`;
- short container ID: `fc2a1e0e8ec1`;
- container status: `Exited (2)`;
- `.Config.Env` contained `APP_ENV=testing`.

`docker logs` contained:

```text
sh: PAGE_TITLE: PAGE_TITLE must be provided
```

Inspection showed:

```text
Status=exited
ExitCode=2
Error=""
```

Docker successfully created and started the process. The shell inside the container rejected the missing required configuration, so the useful error was in `docker logs`. `.State.Error` remained empty because Docker itself did not fail.

During the first investigation attempt, a trailing backslash after `docker ps` joined several separate commands. The host Bash then expanded the required-variable expression and printed its own `PAGE_TITLE` error. Running `docker ps`, `docker logs`, and `docker inspect` as separate commands produced the correct investigation results.

Final diagnosis:

> The container exited because the required PAGE_TITLE environment variable was missing, so the shell returned exit code 2. Docker successfully created and started the process, so .State.Error remained empty.

### Environment-variable security

- Normal environment variables are configuration, not secure secret storage.
- Users with Docker access can view configured values using `docker inspect`.
- Processes inside the container can access their environment.
- Environment files store values as plain text.
- Values written directly in commands may remain in shell history.
- Normal users without Docker permission cannot necessarily inspect containers.
- Real credentials should use an appropriate dedicated secret-management mechanism.

### Cleanup

I removed these containers:

- `lesson08-env`;
- `lesson08-web`;
- `lesson08-broken`.

I removed these temporary host files:

- `/tmp/docker-lesson08.env`;
- `/tmp/docker-lesson08-web.env`;
- `/tmp/docker-lesson08-broken.env`.

I also removed `alpine:3.24`, which had been downloaded specifically for this lesson, and unset `LESSON_MESSAGE`, `APP_ENV`, `OLD_ID`, and `NEW_ID`. `nginx:alpine` was intentionally left untouched.

Final practical verification showed:

- `docker ps -a --filter name=lesson08` displayed only headers;
- `docker image ls alpine` displayed only headers;
- host port `8080` was not listening;
- the port-check `grep` returned exit status `1`, meaning no match;
- `git status --short` was empty before documenting the lesson.

## Next step

The next topic after environment variables in `ROADMAP.md` is Docker Compose:

**Docker Lesson 09 — Docker Compose**

---

## Lesson 09 — Docker Compose

**Date:** 2026-09-10

I completed the basic Docker Compose workflow with one Nginx service. The initial practice was intentionally kept simple after an earlier attempt became too complicated. Later on the same day, I completed Compose logs and `exec` practice. Multiple services are reserved for Lesson 10, and deeper container networking and service discovery for Lesson 11.

### Purpose of Docker Compose

Instead of putting all container configuration into long `docker run` commands, I can describe it in `compose.yaml`.

For now, I treat a Compose service as the description of a container I want Docker to run. The file stores the desired service/container configuration.

### One Nginx service

The final `compose.yaml` in `/tmp/docker-lesson09` contained:

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8083:80"
```

- `web` is the service name.
- `nginx:alpine` is the image to use.
- `8083` is the host port, and `80` is the container port.

### Read and check the configuration

From the lesson directory, I ran:

```bash
docker compose config
```

This command reads, validates, and resolves `compose.yaml`. It shows how Compose understands the configuration. It does **not** inspect a running container.

In the resolved port configuration:

- `target: 80` means port `80` inside the container;
- `published` means the host port: `8081`, `8082`, or `8083` during this practice.

### Start and check the service

```bash
docker compose up -d
docker compose ps
```

`docker compose up -d` creates and starts the service in the background. Compose also created its default project network automatically.

`docker compose ps` shows containers belonging to the current Compose project. I verified:

- service: `web`;
- image: `nginx:alpine`;
- status: `Up`;
- port mapping: host `8083` to container `80` (`8083->80` in the mapping).

### Stop and remove the lesson resources

```bash
docker compose down
docker compose ps
```

`docker compose down` stopped and removed the Compose container and removed the automatically created default project network. Afterward, `docker compose ps` showed no containers.

### Repeated practice and independent command selection

I repeated the workflow with host ports `8081`, `8082`, and `8083`, keeping container port `80`. After changing `compose.yaml`, I checked the new configuration with `docker compose config`.

Later, I independently selected the commands for each step:

```bash
docker compose config
docker compose up -d
docker compose ps
docker compose down
```

### Temporary project for logs and exec

For the additional practice on 2026-09-10, I created `/tmp/docker-lesson09-logs` with a `compose.yaml` equivalent to:

```yaml
name: lesson09-logs

services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8083:80"
```

The port binding publishes container port `80` on host port `8083`, accessible through host loopback address `127.0.0.1`.

Compose manages services together as a project:

| Name | Meaning |
|---|---|
| `lesson09-logs` | Compose project name, set by `name` in the configuration. |
| `web` | Stable service name defined under `services` in `compose.yaml`. |
| `lesson09-logs-web-1` | Generated container name for this project's service instance. |

Commands such as `docker compose logs web` and `docker compose exec web ...` accept the service name. Compose resolves `web` to the appropriate container in the current project, so I do not need to type the generated full container name. The following Compose commands were run from the temporary project directory.

### Project and HTTP verification

```bash
docker compose config
docker compose up -d
docker compose ps
curl -I http://127.0.0.1:8083/
```

Verified results:

- `config` successfully validated and rendered the resolved configuration;
- `up -d` created `lesson09-logs_default` and started `lesson09-logs-web-1`;
- `ps` showed service `web` running with `127.0.0.1:8083->80/tcp`;
- the HEAD request returned `HTTP/1.1 200 OK`;
- the Nginx version was `1.31.4`;
- a request to `/missing` returned HTTP status `404`.

### Compose logs

```bash
docker compose logs --tail 10 web
docker compose logs --timestamps --tail 10 web
```

- `--tail 10` prints the last ten available log lines and then exits.
- `--timestamps` adds Docker/Compose timestamps to the displayed lines. Nginx messages can also contain their own application timestamps, so a line may show both.
- `web` limits the output to that service.

The logs showed `HEAD / HTTP/1.1` with status `200` and `GET /missing HTTP/1.1` with status `404`. Nginx also reported that `/usr/share/nginx/html/missing` did not exist. The source address appeared as `172.18.0.1` in this practice.

### Following live logs

In one terminal, I ran:

```bash
docker compose logs --follow --tail 0 web
```

`--follow` keeps the local command running and displays new log output in real time. `--tail 0` skips existing history and waits only for new entries.

From a second terminal, I generated a request to `/live-test`. The live output immediately showed the missing-file error and `GET /live-test HTTP/1.1` with status `404`.

**Correction:** Pressing `Ctrl+C` stopped only the local log-following command. It did not stop the `web` container or the Nginx process. A later `docker compose ps` confirmed that the service remained `Up`.

### Compose exec

```bash
docker compose exec web pwd
docker compose exec web nginx -v
docker compose ps
```

`pwd` returned `/`, and `nginx -v` reported `nginx/1.31.4`. The final `ps` check confirmed that `web` remained running.

`docker compose exec` starts an additional command inside the already-running container for the named service. It does not replace or restart the service's main process.

### Understanding check

- `compose.yaml` stores the desired service/container configuration.
- `config` shows the resolved Compose configuration.
- `up -d` creates and starts services in the background.
- `ps` shows the status of containers in the current Compose project.
- `down` stops and removes the Compose resources used in this lesson.
- In `"8083:80"`, `8083` is the host port and `80` is the container port.

### Cleanup

`docker compose down` completed successfully, and `/tmp/docker-lesson09` was removed. No lesson containers, default project network, or temporary lesson directory remained.

After the additional logs and `exec` practice, I ran:

```bash
docker compose down
docker compose ps -a
```

Verified cleanup results:

- `down` removed `lesson09-logs-web-1` and `lesson09-logs_default`;
- `ps -a` showed only the headers afterward;
- the filtered Docker network listing showed no remaining Lesson 09 network;
- `/tmp/docker-lesson09-logs` was removed, and the directory absence check returned exit status `0`;
- the port `8083` listening check returned exit status `1`, meaning nothing was listening there;
- the repository remained clean after the practical work, before this documentation update;
- the local `nginx:alpine` image was intentionally retained.

## Next step

**Docker Lesson 10 — Multiple Services**

Continue through Lessons 11–12 in `ROADMAP.md`, then complete one comprehensive Docker checkpoint and one practical Docker project before starting Python for DevOps.

---

## Lesson 10 — Multiple Services

**Date:** 2026-09-10

I completed a Compose project with two services: Nginx (`web`) and Redis (`cache`). I practised managing services separately and together, reading logs, applying configuration changes, recovering the project, and verifying cleanup.

### Two services in one project

The temporary project directory was `/tmp/docker-lesson10`, and the Compose project name was `lesson10`. The corrected initial `compose.yaml` was equivalent to:

```yaml
name: lesson10

services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  cache:
    image: redis:7-alpine
```

- `web` and `cache` are stable service names under `services`.
- Nginx container port `80` was initially published on host loopback address `127.0.0.1`, port `8080`.
- Redis container port `6379` was not published on the Ubuntu host.
- Compose created `lesson10-web-1`, `lesson10-cache-1`, and the default bridge network `lesson10_default`.

The following Compose commands were run from the temporary project directory.

### YAML indentation troubleshooting

An initial indentation error placed `cache` outside `services`. Running:

```bash
docker compose config
```

reported:

```text
additional properties 'cache' not allowed
```

A second attempt with inconsistent indentation produced a YAML parser error:

```text
did not find expected key
```

I corrected the indentation using spaces so that `web` and `cache` were at the same level inside `services`. `docker compose config` then successfully validated and resolved the configuration.

The resolved configuration showed both services attached to the default network. It also expanded the short port syntax into these fields:

| Field | Initial value | Meaning |
|---|---|---|
| `host_ip` | `127.0.0.1` | Host address used for the binding. |
| `published` | `8080` | Port on the Ubuntu host. |
| `target` | `80` | Port inside the web container. |
| `protocol` | `tcp` | Transport protocol. |

### Starting and verifying both services

```bash
docker compose up -d
docker compose ps
curl -I http://127.0.0.1:8080
docker compose exec cache redis-cli ping
```

Verified results:

- `up -d` pulled `redis:7-alpine`, created the default network, and started both services;
- `ps` showed both services `Up`;
- `web` showed `127.0.0.1:8080->80/tcp`;
- `cache` showed `6379/tcp`, indicating a container port with no published host mapping;
- the HTTP HEAD request returned `HTTP/1.1 200 OK` from Nginx `1.31.4`;
- `redis-cli ping` returned `PONG`.

`docker compose exec cache redis-cli ping` runs the Redis client inside the running cache container. Redis `PING` is an application command; Linux `ping` uses ICMP and is a different check.

### Managing one service by name

```bash
docker compose stop cache
docker compose ps -a
curl -I http://127.0.0.1:8080
docker compose exec cache redis-cli ping
```

Only Redis stopped. The web service remained running and continued returning HTTP `200 OK`.

The Redis check failed because `exec` requires a running service container. Compose reported:

```text
service "cache" is not running
```

The command returned exit status `1`.

```bash
docker compose start cache
docker compose ps
docker compose exec cache redis-cli ping
```

`start cache` reused the existing stopped container. Its original creation time remained, while its uptime reset. Redis returned `PONG` again.

Compose resolves the service names `web` and `cache` to their project containers. I can target a service without typing its generated container name.

### Logs from multiple services

```bash
docker compose logs --tail 5
docker compose logs --tail 3 cache
```

The first command displayed recent lines from both services with `web-1` and `cache-1` prefixes. Nginx logs contained successful `HEAD /` requests with HTTP status `200`. Redis logs showed that it was ready to accept TCP connections.

`--tail 5` applies to each selected service; it does not limit the whole project's output to five lines. Adding `cache` selected only Redis logs, with up to three recent lines in the second command.

### Desired configuration versus runtime state

I changed the web port mapping in `compose.yaml` to:

```yaml
    ports:
      - "127.0.0.1:8081:80"
```

```bash
docker compose config
docker compose ps
```

`config` showed desired host port `8081`, while `ps` still showed runtime host port `8080`. Validation reads and resolves configuration; it does not apply changes to running containers.

To apply the change to the web service, I ran:

```bash
docker compose up -d web
docker compose ps
curl -I http://127.0.0.1:8081
curl -I --max-time 2 http://127.0.0.1:8080
echo $?
```

Verified results:

- Compose recreated only `web`;
- the cache container's creation time and uptime showed that it was neither recreated nor restarted;
- `ps` showed `127.0.0.1:8081->80/tcp`;
- port `8081` returned `HTTP/1.1 200 OK`;
- the request to port `8080` returned curl exit code `7` because nothing was listening there.

The command distinction was reviewed:

| Command | Behaviour |
|---|---|
| `docker compose start web` | Starts the existing stopped service container. |
| `docker compose restart web` | Restarts the existing service container without applying changed Compose configuration. |
| `docker compose up -d web` | Reconciles runtime state with `compose.yaml`, recreating the service when required, and starts it in the background. |

### Stopping the project and recovering from a mistake

During the first no-hint attempt, I accidentally used `docker compose down` instead of `docker compose stop`. This safely removed both temporary containers and `lesson10_default`.

I recovered the project with `docker compose up -d`. Compose recreated both containers and the default network from `compose.yaml`.

I also completed and verified the intended stop workflow:

```bash
docker compose stop
docker compose ps
docker compose ps -a
docker network ls --filter name=lesson10
```

- `stop` stopped both services but kept their containers and the default network;
- `ps` showed only running services, so no service rows remained;
- `ps -a` included both stopped containers with `Exited (0)`;
- the filtered network listing confirmed that `lesson10_default` remained.

This provided practical evidence of the differences:

| Command | Project behaviour in this lab |
|---|---|
| `stop` | Stops services and keeps containers and the network. |
| `down` | Removes project containers and the default network. |
| `up -d` | Creates or recreates services as needed and starts the desired services. |

### Container, socket, and application checks

Starting only `web` left `cache` stopped:

```bash
docker compose start web
docker compose ps -a
ss -lnt | grep ':8081'
curl -I http://127.0.0.1:8081
```

These checks answer different questions:

- `ps -a` showed the container states;
- `ss -lnt` showed listening TCP sockets, and the filter confirmed a listener on port `8081`;
- `curl -I` confirmed the HTTP application response with `200 OK`.

### Short preview of service-name DNS

Running `ping cache` on the Ubuntu host failed with:

```text
Temporary failure in name resolution
```

Compose service-name DNS is intended for containers attached to the Compose network, not normal host DNS. This host check did not test Redis's application `PING`. Deeper container networking and service discovery are reserved for Lesson 11.

### Cleanup

Final cleanup used `docker compose down`, which removed both lesson containers and `lesson10_default`.

Before removing the temporary directory, verification showed:

- `docker compose ps -a` displayed only headers;
- `docker network ls --filter name=lesson10` displayed only headers.

After `/tmp/docker-lesson10` was removed, final checks showed:

- `test ! -d /tmp/docker-lesson10` returned exit status `0`;
- `ss -lnt | grep ':8081'` found no listener and returned exit status `1`;
- `docker ps -a --filter name=lesson10` displayed only headers;
- `nginx:alpine` and `redis:7-alpine` were intentionally retained and verified locally for reuse in Lesson 11;
- no repository files were created during the practical lab.

### My sentence

I can manage multiple Compose services, compare desired configuration with running containers, and verify recovery and cleanup.

## Next step

**Docker Lesson 11 — Docker Networking and Service Discovery**

Lesson 12 remains Image Optimization and Multi-Stage Builds. After Lesson 12, complete one comprehensive Docker checkpoint and one practical Docker project, then begin Python for DevOps.

---

## Lesson 11 — Docker Networking and Service Discovery

**Date:** 2026-09-11

I completed this practical lesson on Ubuntu 24.04 using the temporary project `/tmp/docker-lesson11`. I tested default networking, service discovery, ports, application protocols, and custom network isolation. The temporary project was removed afterward.

### Compose default networking

The initial `compose.yaml` was equivalent to:

```yaml
name: lesson11

services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8081:80"
  cache:
    image: redis:7-alpine
  client:
    image: redis:7-alpine
    command: ["sleep", "3600"]
```

The following Compose commands were run from the temporary project directory:

```bash
docker compose config
docker compose up -d
docker compose ps
```

Verified results:

- `config` showed all three services attached to the default network, named `lesson11_default`;
- `up -d` created three containers and one default bridge network;
- `web` published container port `80` on Ubuntu loopback address `127.0.0.1`, port `8081`;
- `6379/tcp` shown for the Redis image was exposed image metadata, not a published host port or proof of a listening process;
- `cache` ran Redis Server, while `client` ran `sleep 3600` instead of Redis Server. The client image still supplied tools such as `redis-cli`.

### Reading full network inspection output

```bash
docker network inspect lesson11_default
```

I read the full output instead of using a formatted template. I learned to identify:

| Field | Meaning |
|---|---|
| `Name` | Network name, such as `lesson11_default`. |
| `Driver` | `bridge` for the networks used in this lab. |
| `IPAM.Config` → `Subnet` | Address range assigned to the network. |
| `IPAM.Config` → `Gateway` | Gateway address for the network. |
| `Containers` | Containers attached to the network. |
| Container `Name` and `IPv4Address` | Container name and its address on that network. |

Container IP addresses are runtime details and may change when containers are recreated. Applications should use stable Compose service names instead of fixed container IP addresses.

### Docker DNS and service discovery

From `client`, `ping web` and `ping cache` both resolved the service names and succeeded. These were Linux ICMP checks, not application-protocol checks.

```bash
docker compose exec client redis-cli -h cache ping
docker compose exec client wget -qO- http://web | head -n 5
```

- `redis-cli -h cache ping` returned `PONG`; `-h cache` selected the Redis host by service name.
- `wget -qO- http://web | head -n 5` returned Nginx HTML; `-q` reduced output, `-O-` wrote the response body to standard output, and `head -n 5` limited the displayed output to the first five lines.

Docker's service-name DNS resolves these names between containers sharing a Docker network. The Compose names are not normal Ubuntu host DNS names.

### Host ports versus container ports

| Request source | Address used | Result |
|---|---|---|
| Ubuntu host | `http://127.0.0.1:8081` | Reached Nginx through the published host port. |
| Another container on the shared network | `http://web` or `http://web:80` | Reached Nginx directly on container port `80`. |
| Another container on the shared network | `http://web:8081` | Resolved `web`, then returned `Connection refused`. |

Nginx listened on container port `80`, not `8081`. Port `8081` was only the published host-side port. Containers used `web:80` to reach the service directly.

### DNS, TCP, and application-protocol troubleshooting

I separated troubleshooting into three stages:

1. **DNS/name resolution:** translate the service name into an IP address.
2. **TCP transport:** connect to the port where the server is listening.
3. **Application protocol:** exchange messages in the format the application understands, such as HTTP, Redis protocol, PostgreSQL protocol, or SSH.

| Observed failure | Meaning in this lab |
|---|---|
| `bad address` | Docker DNS could not resolve the service name, as when the containers shared no network. |
| `Connection refused` | The name resolved and the destination was reached, but nothing listened on the requested port. |
| Protocol mismatch | DNS succeeded and the port was reachable, but the client and server spoke different application protocols. |

While `client` and `cache` shared a network, I tested:

```bash
docker compose exec client wget -qO- http://cache:80
echo $?

docker compose exec client wget -T 2 -O- http://cache:6379
echo $?

docker compose exec client redis-cli -h cache -p 6379 ping
echo $?
```

Verified differences:

- `wget -qO- http://cache:80` resolved `cache` to its IP address but returned `Connection refused`. Redis did not listen on port `80`.
- `wget -T 2 -O- http://cache:6379` reached the correct Redis port but failed because `wget` spoke HTTP. `-T 2` set a two-second timeout.
- Redis logged a `Possible SECURITY ATTACK` / cross-protocol warning after receiving the HTTP `Host` header. This was intentionally caused by the lab request and was not an external attack.
- `redis-cli -h cache -p 6379 ping` used the correct Redis protocol, returned `PONG`, and exited with code `0`. `-p 6379` explicitly selected the Redis port.

Redis also logged a `vm.overcommit_memory` warning. It did not prevent Redis from reaching `Ready to accept connections` or answering the Redis check.

### Custom networks and isolation

I declared two custom bridge networks:

```yaml
networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
```

The first custom topology used these service memberships:

| Service | Networks |
|---|---|
| `web` | `frontend` only |
| `cache` | `backend` only |
| `client` | `frontend` and `backend` |

```bash
docker network inspect lesson11_frontend lesson11_backend
```

The full inspection output confirmed that:

- `lesson11_frontend` contained `web` and `client`;
- `lesson11_backend` contained `cache` and `client`.

`client` could reach both services because it shared a network with each one. `web` could not resolve `cache` and returned `bad address` because they shared no network.

### Shell command continuation mistake

A trailing backslash accidentally continued `docker network inspect` onto the next line. Bash displayed the `>` continuation prompt. The accidental input was:

```text
docker network inspect lesson11_frontend \
> docker network inspect lesson11_backend
```

Here, `>` is Bash's continuation prompt and was not typed. A trailing `\` continues the same shell command onto another line. The second line did not start a separate Docker command.

The effective command included `docker`, `network`, and `inspect` as extra network-name arguments between the two valid network names. Docker inspected both valid networks and also tried to inspect those invalid names. The corrected single-line command was:

```bash
docker network inspect lesson11_frontend lesson11_backend
```

### Final realistic topology

I changed the service network memberships. The final configuration was equivalent to:

```yaml
name: lesson11

services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8081:80"
    networks:
      - frontend
      - backend
  cache:
    image: redis:7-alpine
    networks:
      - backend
  client:
    image: redis:7-alpine
    command: ["sleep", "3600"]
    networks:
      - frontend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
```

```bash
docker compose up -d
docker compose exec client wget -qO- http://web | head -n 3
```

Verified results:

- Compose recreated only `client` and `web` because their network memberships changed;
- `cache` remained running;
- `client` successfully fetched Nginx HTML through `web` on `frontend`;
- `client` could not resolve `cache`, because they no longer shared a network;
- `web` successfully resolved and pinged `cache` through `backend`.

A container attached to two networks is not automatically a router. It does not automatically forward traffic between those networks. The lab verified Nginx access and network reachability; it did not configure Nginx to use Redis as an application backend.

### Network separation and secrets

Network separation follows least privilege: each service receives only the network access it needs. Preventing unnecessary direct service access reduces attack surface and blast radius, meaning the possible reach and impact of a compromised service.

Network isolation protects access paths to services. It does not directly protect API keys.

Real secrets must not be committed to Markdown, Compose files, source code, images, or Git history. Documentation should use fake placeholders, such as `EXAMPLE_API_KEY`. Real secrets should be injected at runtime through an appropriate secrets mechanism.

### Cleanup

Before removing the temporary project directory, I ran:

```bash
docker compose down
docker compose ps -a
docker network ls --filter name=lesson11
```

Verified results:

- `down` removed all three containers and both custom networks;
- `ps -a` returned only headers;
- the filtered network listing returned only headers.

After `/tmp/docker-lesson11` was removed, the final checks were:

```bash
test ! -d /tmp/docker-lesson11
echo $?
ss -lnt | grep ':8081'
echo $?
docker ps -a --filter name=lesson11
```

- The directory absence check returned `0`.
- The listening-port check produced no output and returned `1`, meaning no match for port `8081`.
- The filtered container listing returned only headers.
- `nginx:alpine` and `redis:7-alpine` images were intentionally retained.

### Important vocabulary

| English | Ukrainian |
|---|---|
| service discovery | виявлення сервісів |
| name resolution | перетворення імені на IP-адресу |
| shared network | спільна мережа |
| network isolation | ізоляція мережі |
| least privilege | принцип найменших привілеїв |
| application protocol | протокол прикладного рівня |

### My sentence

I can use Compose service names, check DNS, ports, and application protocols separately, and limit direct service access with custom networks.

## Next step

**Docker Lesson 12 — Image Optimization and Multi-Stage Builds**

After Lesson 12, complete one comprehensive Docker checkpoint and one practical Docker project, then begin Python for DevOps. The Docker block is not complete yet.

---

## Lesson 12 — Image Optimization and Multi-Stage Builds

**Date:** 2026-09-11

I completed a Go HTTP application lab in `/tmp/docker-lesson12`. I compared single-stage and multi-stage images, inspected image history, tested build-cache behaviour, and reduced the build context with `.dockerignore`.

### Lab application and build process

The small application in `main.go` listened on container port `8080`. Its initial HTTP response was:

```text
Docker Lesson 12: application is running
```

The build used:

```bash
CGO_ENABLED=0 go build -o /app main.go
```

`CGO_ENABLED=0` disabled cgo for this build. `-o /app` selected the compiled binary's output path, and `main.go` was the source file to compile.

| Part | Role |
|---|---|
| Source code | Human-readable instructions in `main.go`. |
| Dependencies | Libraries used by the application; this lab had no external dependencies. |
| Compiler and toolchain | Go tools that turn source code into a compiled program. |
| Compiled binary | The executable `/app` produced by the build. |
| Runtime image | The filesystem and configuration used to run the compiled program in a container. |

In this lab, `docker build` compiled the application through the Dockerfile's `RUN` instruction and created an image. `docker run` started the already compiled `/app`; it did not compile the source again.

### Single-stage image

`Dockerfile.single` used `golang:1.26-alpine` for both building and runtime. The image tag was `lesson12:single`.

Verified results:

- the first build took `19.7s`;
- image disk usage was `489 MB`, and compressed content size was `97.3 MB`;
- `/app` was `8.0 MB`;
- `/usr/local/go` was `269.1 MB`;
- `go version` reported `go1.26.8 linux/amd64`;
- the application worked through `127.0.0.1:8082`, mapped to container port `8080`, and returned the initial HTTP response.

This image retained the Go compiler and toolchain, source/build artifacts, and generated build cache. These were useful during compilation but were unnecessary for running this compiled application.

### Multi-stage image

The builder and runtime stages used these instructions:

```dockerfile
FROM golang:1.26-alpine AS builder
```

The builder compiled `main.go` into `/app`. The runtime stage then began with:

```dockerfile
FROM alpine:3.22
COPY --from=builder /app /app
```

The second `FROM` began a new clean stage based on Alpine. It did not inherit the builder's filesystem. `COPY --from=builder /app /app` copied only the selected compiled binary into the runtime image.

| Measurement | `lesson12:single` | `lesson12:multi` |
|---|---|---|
| Disk usage | `489 MB` | `25.8 MB` |
| Compressed content size | `97.3 MB` | `8.44 MB` |
| `/app` size | `8.0 MB` | Approximately `8.0 MB` |
| Go compiler in runtime image | Present | Absent |
| Host-to-container port mapping | `127.0.0.1:8082:8080` | `127.0.0.1:8083:8080` |

Disk usage fell by approximately `95%`: `(489 - 25.8) / 489 × 100`. Disk usage and compressed content size are different measurements and should be compared separately.

In the final multi-stage image, `/app` existed, but `command -v go` returned no path. The Alpine/BusyBox shell used in this check returned exit code `127`.

The smaller image produced the same initial HTTP response through `127.0.0.1:8083` and logged:

```text
Listening on port 8080
```

### Image history

I compared the histories of the single-stage and final multi-stage images.

| Image | Important non-zero layer | Approximate size |
|---|---|---|
| Single-stage | Inherited Go toolchain | `282 MB` |
| Single-stage | `RUN go build`, including generated build-cache contents | `99.1 MB` |
| Single-stage | Alpine base | `9.07 MB` |
| Multi-stage final image | Alpine base | `8.96 MB` |
| Multi-stage final image | Copied `/app` | `8.35 MB` |

The build layer contained more than the binary because compilation also generated build-cache contents. The final multi-stage history contained only the important non-zero runtime layers: Alpine and the copied binary.

`CMD` and `EXPOSE` showed `0 B` because they are image configuration metadata rather than filesystem content. The builder appeared in build output and cache, but its layers did not appear in the final image history.

### Build-cache experiment

An identical rebuild reused `WORKDIR`, `COPY`, `RUN go build`, and the final `COPY --from=builder` from cache. The whole build took `2.7s`, while the actual cached steps showed `0.0s`.

I then changed `main.go` so that the HTTP response became:

```text
Docker Lesson 12: source code was changed
```

The next build showed:

| Step | Result after the source change |
|---|---|
| `WORKDIR` | Remained cached. |
| `COPY main.go .` | Reran because the source file changed. |
| `RUN go build` | Reran and took `6.3s`. |
| `COPY --from=builder /app /app` | Reran because `/app` changed. |
| Total build | Completed in `8.6s`. |

Running the rebuilt image returned the changed HTTP response. A cache miss invalidates the affected step and dependent later steps, not earlier steps.

For a real Go project with module files, the recommended dependency ordering was explained conceptually:

```dockerfile
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o /app .
```

Stable dependency files should be copied before frequently changing source files. This lets Docker reuse dependency downloads when only application source changes. The lab had no `go.mod`, `go.sum`, or external dependencies, so these instructions were not added to the lab.

### Build context and `.dockerignore`

Build context is the set of files made available to the Docker build. It is not the same as final-image contents.

For a deliberate experiment, `Dockerfile.context` changed `COPY main.go .` to `COPY . .`. I created an unnecessary `20 MB` file named `unnecessary.bin`.

Without `.dockerignore`:

- Docker transferred approximately `20.98 MB` of context;
- `COPY . .` invalidated the builder cache, and `go build` unnecessarily reran;
- the `lesson12:context-bad` final image still used `25.8 MB` because `unnecessary.bin` stayed in the builder stage and only `/app` crossed into the final stage.

I then created `.dockerignore` with:

```text
unnecessary.bin
```

With this exclusion, the transferred context dropped to approximately `194 B` / `172 B`. A repeated build of `lesson12:context-good` reused all relevant cached steps and completed in `2.1s`.

I increased `unnecessary.bin` to `30 MB`. Docker still transferred only `172 B`, all relevant build steps remained cached, and the build completed in `1.7s`. Changes to the ignored file no longer affected the copied build inputs.

`.dockerignore`:

- reduces build context;
- improves build speed;
- prevents ignored-file changes from invalidating cache;
- helps prevent accidental inclusion of unwanted files.

| File | What it controls |
|---|---|
| `.dockerignore` | Files included in the Docker build context. |
| `.gitignore` | Untracked files considered by Git. |

Neither file automatically protects or removes a secret already tracked in Git history.

### Key takeaways

- Building and running are separate operations: this build compiled `/app`, and the container ran it.
- Source code, dependencies, the compiler, the compiled binary, and the runtime image have different roles.
- A second `FROM` starts a new stage; multi-stage builds copy only selected artifacts into the runtime image.
- Build context can contain files that never enter the final image.
- Copy stable dependency files before frequently changing source files to preserve useful cache.
- Smaller runtime images improve transfer and deployment efficiency and reduce unnecessary attack surface. They do not automatically reduce application RAM, CPU usage, or HTTP response time.

### Cleanup

Final lab cleanup was verified:

- all `lesson12` containers were removed;
- tags `lesson12:single`, `lesson12:multi`, `lesson12:context-bad`, and `lesson12:context-good` were removed;
- `docker image ls lesson12` returned no lesson images;
- `/tmp/docker-lesson12` was removed, and the directory absence check returned `0`;
- ports `8082` and `8083` had no listeners; the grep check returned `1`, meaning no matches.

The final `docker system df` output showed:

| Resource | Remaining state |
|---|---|
| Images | `3` unused images, `152.1 MB` |
| Containers | `0` |
| Local volumes | `6` unused volumes, `356 B` |
| Build cache | `21` entries, `879.4 MB` reclaimable |

Removing lesson image tags did not remove all build cache. No global prune was run because it could affect cache or resources from unrelated projects.

### Important vocabulary

| English | Ukrainian |
|---|---|
| compiler | компілятор |
| compiled binary | скомпільований виконуваний файл |
| builder stage | етап збирання |
| runtime image | образ для запуску програми |
| build context | контекст збирання |
| cache invalidation | втрата можливості повторного використання кешу |

### My sentence

I can build a smaller runtime image, explain which files it contains, and use build cache and `.dockerignore` to avoid unnecessary work.

## Next step

**Comprehensive Docker checkpoint**

Docker Lessons 01–12 and the Docker lesson block are complete. The comprehensive Docker checkpoint is the immediate next step, followed by one practical Docker project, then Python for DevOps. The checkpoint and practical project are not complete yet.

---

## Comprehensive Docker checkpoint — completed

**Date:** 2026-09-12

I passed the comprehensive Docker checkpoint with approximately **7.3/10** after completing Docker Lessons 01–12.

### Strong areas

- Ports and Compose lifecycle.
- Service-name DNS and network isolation.
- Multi-stage builds, build context/cache, and `.dockerignore`.
- Logs, persistence, and troubleshooting.

### Areas for continued review

| Topic | Point to remember |
|---|---|
| Dockerfile → image → container | A Dockerfile describes build instructions; `docker build` creates an image; `docker run` creates and starts a container from an image. This project's build compiles `/app`, and its container runs the compiled binary. |
| `docker start` | Starts an existing stopped container, preserving its ID, configuration, and writable layer. It does not create a replacement container or rebuild the image. |
| Missing bind-mount paths | With `docker run`, `-v` creates a missing host source as a directory; `--mount type=bind` fails by default when the source path does not exist. |
| Environment-variable security | Environment variables are not secure secret storage. Docker inspection, process environments, plain-text environment files, and shell history can expose values. |
| `ENTRYPOINT` and `CMD` | `ENTRYPOINT` sets the executable when configured; `CMD` supplies its default arguments, or the default command when no entrypoint is set. Exec form avoids an extra shell. |
| PID 1 and `--rm` | The container's main process runs as PID 1; its exit stops the container. `--rm` automatically removes the container after exit, including its writable layer, but does not delete named volumes. |
| `localhost` inside containers | Refers to the current container. Reach another Compose service using its service name and container port on a shared network. |

### My sentence

I can investigate Docker problems using ports, networks, logs, and storage checks, and I know which concepts need more practice.

---

## Docker Visitor Counter mini-project — completed

**Date:** 2026-09-12

I successfully completed a containerized visitor counter with Nginx, Go, and Redis. The [project README](../Projects/docker-visitor-counter/README.md) contains the architecture diagram, file descriptions, commands, troubleshooting guidance, and cleanup procedure.

### Finished project structure

```text
Projects/docker-visitor-counter/
├── .dockerignore
├── Dockerfile
├── compose.yaml
├── main.go
├── nginx/
│   └── default.conf
└── README.md
```

### Permanent reference — from a Dockerfile to a running Go application

This reference connects the checkpoint's build-sequence review to the finished project. Lesson 12 above records the earlier image-size and cache experiments; they are not repeated here. The following commands are for future practice and were not run during this documentation update.

`nano Dockerfile.single` opens the file `Dockerfile.single`, or lets me create it by saving if it does not exist. `nano` is a text editor, not part of Docker. `Dockerfile.single` is an optional comparison file, not a file in the finished project structure above. The completed project uses its multi-stage `Dockerfile`.

From the repository root, open the optional file:

```bash
cd Projects/docker-visitor-counter
nano Dockerfile.single
```

Enter this complete single-stage example, then save with `Ctrl+O`, confirm the filename with `Enter`, and exit with `Ctrl+X`:

```dockerfile
# syntax=docker/dockerfile:1

FROM golang:1.26-alpine

WORKDIR /src
COPY main.go .
RUN CGO_ENABLED=0 go build -o /app main.go

EXPOSE 8080
CMD ["/app"]
```

| Instruction | Meaning in this example |
|---|---|
| `# syntax=docker/dockerfile:1` | Selects the Dockerfile syntax frontend. |
| `FROM golang:1.26-alpine` | Starts the image stage from Alpine with the Go compiler and toolchain included. |
| `WORKDIR /src` | Sets the working directory for later instructions, creating it if necessary. |
| `COPY main.go .` | Copies source `main.go` from the build context into destination `.` inside the image. Because the working directory is `/src`, the destination file is `/src/main.go`. |
| `RUN CGO_ENABLED=0 go build -o /app main.go` | Compiles the source during image building. `CGO_ENABLED=0` disables cgo, and `-o /app` selects the output binary. |
| `EXPOSE 8080` | Records the intended container port as image metadata. It does not publish a host port. |
| `CMD ["/app"]` | Sets the default main process when a container starts. With no entrypoint in this example, `/app` runs directly as PID 1; it does not compile the source again. |

Build and run the comparison image:

```bash
docker build -f Dockerfile.single -t docker-visitor-app:single .
docker run -d --name visitor-single -p 127.0.0.1:8086:8080 docker-visitor-app:single
curl --fail http://127.0.0.1:8086/health
```

`-f` selects the Dockerfile; `-t` names the image `docker-visitor-app` with tag `single`; the final `.` is the build context. `--name` names the container, `-d` runs it in the background, and `-p` maps localhost host port `8086` to container port `8080`. If the first request arrives before the server starts, check its logs and retry.

This standalone check uses `/health`, which returns `healthy` without Redis. It does not start Redis or attach the container to the Compose backend network. A counter request to `/` requires Redis and returns HTTP `503` when Redis cannot be reached. Use the complete Compose workflow below to test the visitor counter.

Inspect the running container, logs, size, and image contents:

```bash
docker ps -a --filter name=visitor-single
docker logs visitor-single
docker image ls docker-visitor-app:single
docker image inspect docker-visitor-app:single --format '{{.Size}}'
docker run --rm docker-visitor-app:single sh -c 'go version; ls -l /src/main.go /app; cat /etc/alpine-release'
```

Image inspection reports `.Size` in bytes; it is not a compressed content-size measurement. The temporary `--rm` container overrides the default `CMD` with a shell to inspect the image and is removed when that shell exits.

The single-stage image is large because it retains all four parts: the Go toolchain, source code, compiled binary, and Alpine runtime filesystem. Generated build cache can also remain in its build layer.

After this optional exercise, remove its container and image:

```bash
docker stop visitor-single
docker rm visitor-single
docker image rm docker-visitor-app:single
```

### Comparison with the completed multi-stage build

The project's `Dockerfile` starts with `FROM golang:1.26-alpine AS builder`. This builder stage contains Go and the source and compiles `/app`. The runtime stage starts clean with `FROM alpine:3.22`; it does not inherit the builder filesystem. `COPY --from=builder /app /app` copies source `/app` from the builder to destination `/app` in the runtime stage, transferring only the compiled binary.

The final image contains neither the Go compiler nor `main.go`. Its measured result was **25.8 MB disk usage** and **8.45 MB content size**, as recorded for this completed project. The builder's tools and cache can still exist in Docker's build cache without becoming part of the final image.

### Architecture and configuration

The request path is host/browser → Nginx proxy → Go application → Redis.

| Service | Network membership | Role |
|---|---|---|
| `proxy` | `frontend` | Nginx publishes `127.0.0.1:8085:80` and forwards HTTP to `app:8080`. |
| `app` | `frontend`, `backend` | Go serves HTTP on `8080` and increments the Redis `visits` key. No published host port. |
| `cache` | `backend` | Redis listens on `6379`. No published host port. |

`.dockerignore` excludes Git metadata, Markdown, Compose configuration, and Nginx configuration from the build context.

Redis runs with append-only persistence and stores data in `/data` on the `cache-data` named volume. Nginx configuration is mounted read-only. The Go application receives `REDIS_ADDR=cache:6379` and `APP_MESSAGE="Docker visitor counter is running"` through Compose.

### Health checks and dependency ordering

Redis is checked with `redis-cli ping`, Go through `/health`, and Nginx through `/nginx-health`. All checks use a `5s` interval, `3s` timeout, and `5` retries.

`depends_on` with `service_healthy` makes the app wait for healthy Redis and the proxy wait for a healthy app at startup. This does not continuously restart dependent services after a dependency failure. The Go health endpoint does not check Redis, and the Nginx health endpoint does not check Go. Counter requests test the complete application path; health requests do not increment visits.

### Complete mini-project command reference

Run these commands from `Projects/docker-visitor-counter` during a future lab. They describe the complete workflow; the cleaned-up project was not restarted for this documentation update. Resource names below assume the default Compose project name `docker-visitor-counter`.

Validate, build, start, and inspect health and logs:

```bash
docker compose config --quiet
docker compose up -d --build --wait
docker compose ps
docker compose ps -q | xargs -r docker inspect --format '{{.Name}} {{json .State.Health}}'
docker compose logs --tail 30 proxy app cache
docker compose exec proxy nginx -t
```

`config --quiet` only validates configuration. `up --wait` waits for healthy services. The inspection command shows each container's health status and recent check output.

Send two counter requests and inspect the application's non-secret configuration:

```bash
curl --fail http://127.0.0.1:8085/
curl --fail http://127.0.0.1:8085/
docker compose exec app printenv REDIS_ADDR APP_MESSAGE
```

With a fresh volume and no other counter requests, the responses contain `Visits: 1` and `Visits: 2`. Browser requests to other paths can also increment the count. Inspect only the needed variables; environment output can expose secrets in other projects.

Test Redis persistence by removing and recreating the containers while keeping the named volume:

```bash
docker compose down
docker compose up -d --wait
curl --fail http://127.0.0.1:8085/
docker compose exec cache redis-cli GET visits
```

The next request returns `Visits: 3`, and Redis reports `3`, if no extra counter requests occurred. Do not add `--volumes` to the persistence-test `down` command.

Check network membership, connectivity, and isolation:

```bash
docker network inspect docker-visitor-counter_frontend docker-visitor-counter_backend
docker compose exec proxy wget -qO- http://app:8080/health
docker compose exec proxy nslookup cache
echo $?
docker compose exec app nc -z -w 2 cache 6379
echo $?
```

The proxy reaches the app's health endpoint without changing the counter. Resolving `cache` from the proxy fails with exit code `1`; connecting from the app to `cache:6379` succeeds with exit code `0`.

Verify the read-only Nginx bind mount:

```bash
docker compose ps -q proxy | xargs -r docker inspect --format '{{json .Mounts}}'
docker compose exec proxy sh -c ': >> /etc/nginx/conf.d/default.conf'
echo $?
```

Inspection should show the configuration mount with `RW: false`. The second command attempts to open the file for append without writing any content. The read-only filesystem rejects the open with `Read-only file system` and exit code `1`.

Finally, delete the project's saved counter and clean up its resources:

```bash
docker compose down --volumes
docker image rm docker-visitor-app:1.0
docker compose ps -a
docker network ls --filter label=com.docker.compose.project=docker-visitor-counter
docker volume ls --filter label=com.docker.compose.project=docker-visitor-counter
docker image ls docker-visitor-app:1.0
ss -lnt 'sport = :8085'
```

`--volumes` deletes the named volume and its data. The final listings should show no matching containers, project networks, volume, app image, or listener on port `8085`. No global prune or host sysctl change is part of this workflow.

### Verified practical results

| Check | Recorded result |
|---|---|
| Application image | `25.8 MB` disk usage and `8.45 MB` content size; these are separate measurements. |
| Health status | `proxy`, `app`, and `cache` all passed their checks. |
| Nginx configuration | `nginx -t` passed. |
| First two counter requests | Returned `Visits: 1` and `Visits: 2`. |
| Persistence after `docker compose down` and `up` | The named volume preserved the counter; the next request returned `Visits: 3`. |
| Proxy → app | Reached `app:8080`. |
| Proxy → cache DNS | Could not resolve `cache` because they shared no network; exit code `1`. |
| App → cache | Connected to `cache:6379`; exit code `0`. |
| Writing to mounted Nginx configuration | Failed with `Read-only file system`; exit code `1`. |
| Host port publication | Only `127.0.0.1:8085`; no app or Redis host ports. |

### Troubleshooting lessons

- A host-port conflict concerns the published host port, not the port used between containers.
- Service-name DNS requires shared network membership; the proxy's failure to resolve Redis demonstrated the intended isolation.
- `localhost` inside the app cannot address Redis; `cache:6379` selects the correct service.
- Health checks and logs help locate failures, but separate component health checks do not prove the full request path works.
- Redis logged a non-blocking `vm.overcommit_memory` warning. It became healthy, and the persistence test passed. No host sysctl settings were changed.

### Cleanup

Final cleanup removed all three containers, both project networks, the named volume, and the locally built application image. Port `8085` was released. These results came from the completed practical lab; the documentation update did not start or recreate the cleaned-up project.

### My sentence

I can connect a proxy, an application, and a database with Docker Compose, verify persistence and network isolation, and clean up the project's resources.

## Next step

**Python for DevOps**

Docker Lessons 01–12, the comprehensive checkpoint, and the Docker Visitor Counter mini-project are complete. Begin Python for DevOps while continuing short reviews of the checkpoint gaps.
