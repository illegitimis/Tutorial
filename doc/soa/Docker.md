# Docker

The microservices architecture introduces the need for _independent deployment_, _scalability_ and _portability_.

**containers**: as light-weight runtime environments with many of the core components of a virtual machine and isolated services of an operating system, designed to make packaging easy and execution of services smooth.

**Docker** can provide an ideal environment for deployment of these services with respect to speed, isolation management, and lifecycle. Isolates containers to one process or service. This intentional containerization of single service or process makes it very simple to manage and update these services.

Kubernetes, an open source project designed for microservices by extending Docker's capabilities. By describing the characteristics of an image Kubernetes can deploy and manage multiple Docker containers of the same type.

## Key points

* virtual machines aren’t the right unit of work
* (CEO Docker Golub, ex dotCloud PaaS) 
> containerization can be one of the most significant enablers of the next generation of computing
* lightweight containers like Docker offer a nice mix of _encapsulation_ and _interoperability_
* aims to automate the deployment of applications inside portable containers that are independent of hardware, host operating system, and language
* In contrast with Virtual Machines, Docker containers **do not include a guest operating system** but _share the operating system with other containers_.
* What docker provides more than other linux containers do is to package an application and all of its dependencies in a virtual container that can run on any Linux server which docker runs. 
* **Resource Utilization**: Containers comprise just the application and its dependencies, neither more nor less. Each container runs as an isolated process in userspace on the host operating system, sharing the kernel with other containers. Thus, it enjoys the resource isolation and allocation benefits of virtual machines but is much more portable and efficient. This does not mean that containers can run not only on VMs, but also on physical servers. Due to the lightweight nature of containers, you can run more containers on  a physical server than virtual machines. The result is higher resource utilization.

## Unvisited

* [official website](https://www.docker.com/)
* [DockerCon Europe 2017](http://europe-2017.dockercon.com/)
* [OASIS Topology and Orchestration Specification for Cloud Applications (TOSCA) TC](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tosca)
* [Docker Container Overview for Business Leaders](https://blogs.msdn.microsoft.com/allthingscontainer/2016/11/07/docker-container-overview-for-business-leaders/) nov 2016
* [Building a Docker Container with an ASP.NET MVC Web API application connected to PostGres on Linux](https://blogs.msdn.microsoft.com/allthingscontainer/2016/10/13/building-a-docker-container-with-an-asp-net-mvc-web-api-application-connected-to-postgres-on-linux/) October, 2016

## courses

* [Getting Started with Docker on Windows](https://app.pluralsight.com/library/courses/docker-windows-getting-started/table-of-contents) by Wes Higbee
* [docker deep dive](https://app.pluralsight.com/library/courses/docker-deep-dive-update/table-of-contents) by Nigel Poulton
* several [course notes](https://gist.github.com/g0t4), and 'Getting Started with Docker on Windows' [notes](https://gist.github.com/g0t4/0d97a9595c87736a8a72a2bd21afc0d9)

Hyper-V on windows image location: _C:\Users\Public\Documents\Hyper-V\Virtual Hard Disks\MobyLinuxVM.vhdx_

Windows containers completely separated from Linux containers. Can be _windows server_ containers or _Hyper-V_ containers. Former use **process** isolation, latter use **VM** isolation.

Container has its own network adapter, file system, processes, registry.

Union file system - set theory union of layer files. File in above layer will trump same file in layer below.

```bash
docker info
docker version
docker ps -a # both started and stopped
docker run hello-world # pull image, create container
docker run -it ubuntu bash # interactive
docker run -p 80:80 nginx
docker stop container_id # or name, or short id
docker start part_of_identifier
docker images
docker rm container_id*
docker rmi --help
# interactive + named terminal for docker docs
# ctrl+c sent to running process
# ctrl+pq sends to background, enables terminal
docker run -p 4000:4000 -it --name docs docs/docker.github.io
# detach from container / background
docker run -p 81:80 -d --name iis microsoft/iis:nanoserver
# dispose container on exit process inside it
docker run --rm -it --isolation=hyperv microsoft/dotnet:nanoserver powershell
docker save microsoft/iis:nanoserver -o iis.tar
docker pull alpine # down lightweight alpine linux
docker run -it alpine sh # run it with a shell
docker run --rm -v C:/ alpine ls ./ # mount win c drive
docker run --rm -it -v C:/hw.tar:/media/hw.tar alpine sh
# test nginx running locally om port 8080
docker run --rm -it -p 8080:80 nginx
# volume mount static website folder from the into existing nginx image
docker run --rm -it -p 8080:80 -v static-website:/usr/share/nginx/html nginx
# container name will be static-website-nginx (docker ps -a -n 1 --no-trunc)
docker run --rm -it -p 8080:80 --name static-website-nginx -v C:\static-website:/usr/share/nginx/html nginx
```

build new image on top of existing, sample is static website on top of nginx

* by hand

```cmd
# start container detached, run bash process inside it, copy from local fs to container, create new image with changes
docker run -d -p 8080:80 --name static-website-nginx nginx
docker exec -it static-website-nginx bash
docker cp .\static-website\. static-website-nginx:/usr/share/nginx/html
docker commit static-website-nginx-container static-website-nginx:some-tag
docker diff dbc
```

* alternative with a dockerfile and docker client over nginx linux image/iis native windows image

```dockerfile
FROM nginx
COPY app /usr/share/nginx/html
```

```dockerfile
FROM microsoft/iis:nanoserver
COPY static-website C:/inetpub/wwwroot
```

```bash
# . is current directory
docker build -t my-account/static-website-nginx:tag-v1 .
docker build -t static-website-iis:iis-nano .
docker tag local-image:with-tag username/image:tag
docker push username/image:tag
docker login
```

databases and volumes: read heavy data in images, write heavy data in volumes

```sh
docker volume ls
# container cleanup
docker rm -f containerids*
docker stop $(docker ps -aq)
docker rm -fv container_and_associated_unnamed_volumes
# volume cleanup
docker volume rm $(docker volume ls -q)
docker volume prune -f
```

docker compose, teamcity with agent and db deployment, `docker-compose.yml`.

Composing containers is the same thing as composing layers for an image with a dockerfile.

embedded dns server with user defined private networks. 

```yml
version: '2'
services:
    teamcity:
        image: sjoerdmulder/teamcity
        ports:
            - 8111: 8111
    teamcity-agent:
        image: sjoerdmulder/teamcity-agent
        environment:
            - TEAMCITY_SERVER=http://teamcity:8111
    postgres:
        image: postgres
        environment:
            - POSTGRES_DB=teamcity
```

```bash
docker-compose help up
docker-compose up docker-compose.yml
docker network inspect bridge
docker-compose exec postgres bash
docker-compose down
```

[<<](../soa.md) | [home](../../README.md)