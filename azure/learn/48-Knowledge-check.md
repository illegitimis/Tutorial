# Knowledge check

Consider the following scenario. Then choose the best response for each question that follows and select Check your answers.

Tailwind Traders is moving its online payment system to Azure. The processing of online orders begins through a website, which Tailwind Traders manages through Azure App Service. (App Service is a way to host web applications on Azure.)

The web application that runs the website passes order information to virtual machines (VMs), which further process each order. These VMs exist on an Azure virtual network, but they need to access the internet to retrieve software packages and system updates.

Here's a diagram that shows the basic architecture of the company's payment system:

![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-network-connectivity-azure/media/8-architecture.png)

An architecture diagram that shows network traffic flowing into Azure. Azure App Service receives passes public network traffic to virtual machines running on a virtual network.

The security team wants to ensure that only valid network traffic reaches the company's Azure resources. As an extra layer of defense, the team also wants to ensure that the VMs can reach only trusted hosts on specific ports.

1. An attacker can bring down your website by sending a large volume of network traffic to your servers. Which Azure service can help Tailwind Traders _protect its App Service instance_ from this kind of attack?
- [ ] Azure Firewall
- [ ] Network security groups
- [X] _Azure DDoS Protection_. DDoS Protection helps protect your Azure resources from DDoS attacks. A DDoS attack attempts to overwhelm and exhaust an application's resources, making the application slow or unresponsive to legitimate users.

2. What's the best way for Tailwind Traders to **limit all outbound traffic** from VMs to _known hosts_?
- [ ] Configure Azure DDoS Protection to limit network access to trusted ports and hosts.
- [x] Create _application rules in Azure Firewall_.
Azure Firewall enables you to *limit outbound HTTP/S traffic to a specified list of fully qualified domain names* (FQDNs).
- [ ] Ensure that all running applications communicate with only trusted ports and hosts.

3. How can Tailwind Traders most easily implement a **deny by default policy** so that VMs can't connect to each other?
- [ ] Allocate each VM on its own virtual network.
- [x] Create a network security group rule that prevents access from another VM on the same network.
A network security group rule enables you to filter traffic to and from resources by source and destination IP address, port, and protocol.
- [ ] Configure Azure DDoS Protection to limit network access within the virtual network.