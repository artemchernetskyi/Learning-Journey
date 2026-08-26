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
