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

## courses

[Getting Started with Docker on Windows](https://app.pluralsight.com/library/courses/docker-windows-getting-started/table-of-contents) by Wes Higbee

Hyper-V on windows image location: _C:\Users\Public\Documents\Hyper-V\Virtual Hard Disks\MobyLinuxVM.vhdx_

Windows containers completely separated from Linux containers. Can be _windows server_ containers or _Hyper-V_ containers. Former use **process** isolation, latter use **VM** isolation.

Container has its own network adapter, file system, processes, registry.

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

```

[<<](../soa.md) | [home](../../README.md)