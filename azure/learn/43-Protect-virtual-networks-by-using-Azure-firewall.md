# Protect virtual networks by using Azure Firewall

> 43 [source](https://docs.microsoft.com/en-us/learn/modules/secure-network-connectivity-azure/3-protect-network-azure-firewall)

A firewall is a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules. You can create firewall rules that specify ranges of IP addresses. Only clients granted IP addresses from within those ranges are allowed to access the destination server. Firewall rules can also include specific network protocol and port information.

Tailwind Traders currently runs firewall appliances, which combine hardware and software, to protect its on-premises network. These firewall appliances require a monthly licensing fee to operate, and they require IT staff to perform routine maintenance. As Tailwind Traders moves to the cloud, the IT manager wants to know what Azure services can protect both the company's cloud networks and its on-premises networks.

## What's Azure Firewall?

[Azure Firewall](https://azure.microsoft.com/services/azure-firewall) is a managed, cloud-based network security service that helps protect resources in your Azure virtual networks. A virtual network is similar to a traditional network that you'd operate in your own datacenter. It's a fundamental building block for your private network that enables virtual machines and other compute resources to securely communicate with each other, the internet, and on-premises networks.

Here's a diagram that shows a basic Azure Firewall implementation:

![alt](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-network-connectivity-azure/media/3-firewall-overview.png)

Azure Firewall is a *stateful* firewall.

 - A stateful firewall analyzes the complete context of a network connection, not just an individual packet of network traffic.
 - Azure Firewall features high availability and unrestricted cloud scalability.

Azure Firewall provides a central location to create, enforce, and log application and network connectivity policies across subscriptions and virtual networks. Azure Firewall uses a *static* (unchanging) public IP address for your virtual network resources, which enables outside firewalls to identify traffic coming from your virtual network. The service is integrated with Azure Monitor to enable logging and analytics.

Azure Firewall provides many features, including:

- Built-in high availability.
- Unrestricted cloud scalability.
- Inbound and outbound filtering rules.
- Inbound Destination Network Address Translation (DNAT) support.
- Azure Monitor logging.

You typically deploy Azure Firewall on a central virtual network to control general network access.

This short video explains how Azure Firewall monitors incoming and outgoing network traffic based a defined set of security rules.
The [video](https://www.microsoft.com/en-us/videoplayer/embed/RWyFpp?postJsllMsg=true) also explains how Azure Firewall compares to traditional firewall appliances.

## What can I configure with Azure Firewall?

With Azure Firewall, you can configure:

- Application rules that define fully qualified domain names (FQDNs) that can be accessed from a subnet.
- Network rules that define source address, protocol, destination port, and destination address.
- Network Address Translation (NAT) rules that define destination IP addresses and ports to translate inbound requests.

[Azure Application Gateway](https://azure.microsoft.com/services/application-gateway) also provides a firewall that's called the web application firewall (WAF).

- WAF provides centralized, inbound protection for your web applications against common exploits and vulnerabilities.
- [Azure Front Door](https://azure.microsoft.com/services/frontdoor/) and [Azure Content Delivery Network](https://azure.microsoft.com/services/cdn/) also provide WAF services.