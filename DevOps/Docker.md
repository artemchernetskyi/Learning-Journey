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
