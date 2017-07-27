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

- [official website](https://www.docker.com/)
- [DockerCon Europe 2017](http://europe-2017.dockercon.com/)
- [OASIS Topology and Orchestration Specification for Cloud Applications (TOSCA) TC](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tosca)



[<<](../SOA.md)
|
[home](README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki)