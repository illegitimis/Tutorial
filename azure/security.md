# Security and Network Security

## Azure Firewall

A firewall is a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules.

Azure Firewall is a managed, cloud-based network security service that helps protect resources in your Azure virtual networks. It is a **stateful** firewall that analyzes the complete context of a network connection, not just an individual packet of network traffic.

Azure Firewall provides a central location to create, enforce, and log application and network connectivity policies across subscriptions and virtual networks. It uses a static (unchanging) public IP address for your virtual network resources, which enables outside firewalls to identify traffic coming from your virtual network.

Key features:

- Built-in high availability
- Unrestricted cloud scalability
- Inbound and outbound filtering rules
- Inbound **Destination Network Address Translation** (DNAT) support
- Azure Monitor logging

### Configuration Options

With Azure Firewall, you can configure:

- **Application rules** that define fully qualified domain names (FQDNs) that can be accessed from a subnet
- **Network rules** that define source address, protocol, destination port, and destination address
- **NAT rules** that define destination IP addresses and ports to translate inbound requests

Azure Application Gateway also provides a web application firewall (WAF) that gives centralized, inbound protection for web applications against common exploits and vulnerabilities. Azure Front Door and Azure Content Delivery Network also provide WAF services.

## DDoS Protection

A **distributed denial of service** attack attempts to overwhelm and exhaust an application's resources, making the application slow or unresponsive to legitimate users.

Azure DDoS Protection (Standard) helps protect your Azure resources from DDoS attacks. It uses the scale and elasticity of Microsoft's global network to bring DDoS mitigation capacity to every Azure region. The service analyzes and discards DDoS traffic at the Azure network edge, before it can affect your service's availability.

### Service Tiers

- **Basic** -- automatically enabled for free as part of your Azure subscription. Provides always-on traffic monitoring and real-time mitigation of common network-level attacks.
- **Standard** -- provides additional mitigation capabilities tuned specifically to Azure Virtual Network resources. Relatively easy to enable and requires no changes to your applications. Policies are tuned through dedicated traffic monitoring and machine learning algorithms.

### Attack Types

The Standard service tier can help prevent:

- **Volumetric** attacks -- flood the network layer with a substantial amount of seemingly legitimate traffic
- **Protocol** attacks -- render a target inaccessible by exploiting a weakness in layer 3 and layer 4 protocol stack
- **Resource-layer** (application-layer) attacks -- target web application packets to disrupt the transmission of data between hosts. Requires a web application firewall (WAF) to protect against L7 attacks.

## Network Security Groups

A network security group (NSG) enables you to filter network traffic to and from Azure resources within an Azure virtual network. You can think of NSGs like an _internal firewall_.

An NSG can contain multiple inbound and outbound security rules. Each rule specifies:

Property | Description
---|---
Name | A unique name for the NSG
Priority | A number between 100 and 4096; lower numbers processed first
Source or Destination | A single IP address or IP address range, service tag, or application security group
Protocol | TCP, UDP, or Any
Direction | Whether the rule applies to inbound or outbound traffic
Port Range | A single port or range of ports
Action | Allow or Deny

Azure creates default rules when you create a network security group. You cannot remove the default rules, but you can override them by creating new rules with higher priorities.

### Exercise: Configure Network Access to a VM

The exercise demonstrates creating a Linux VM, installing `Nginx`, and configuring an NSG rule to allow inbound access on port 80 (HTTP). Key steps:

1. Create a Linux VM using `az vm create`
2. Install Nginx using the Custom Script Extension via `az vm extension set`
3. Verify the web server is not accessible (default NSG only allows port 22/SSH)
4. Create an NSG rule allowing HTTP traffic: `az network nsg rule create` with `--destination-port-ranges 80 --access Allow`
5. Verify the web server is now accessible via `curl`

## Key Vault

Azure Key Vault enables you to store secrets in a single, central location. It makes it easier to enroll and renew certificates from public certificate authorities.

Key Vault operations via Azure CLI:

```bash
az keyvault secret set --vault-name <name> --name <secret> --value <value>
az keyvault secret show --name <secret> --vault-name <name> --query value --output tsv
az keyvault secret list --vault-name <name>
az keyvault secret list-versions --vault-name <name> --name <secret>
```

## Defense in Depth

Defense in depth is the overriding theme for network security. Think about security as a multiple-layer, multiple-vector concern. Threats come from places we do not expect, and they can come with surprising strength.

### Secure the Perimeter Layer

The perimeter layer protects your organization's resources from network-based attacks:

- Use **Azure DDoS Protection** to filter large-scale attacks before they can cause a denial of service
- Use _perimeter firewalls_ with **Azure Firewall** to identify and alert on malicious attacks

### Secure the Network Layer

The focus is on limiting network connectivity across all resources to allow only what is required:

- Limit communication between resources by segmenting your network and configuring access controls
- **Deny by default**
- Restrict inbound internet access and limit outbound where appropriate
- Implement secure connectivity to on-premises networks

### Combine Services

You can combine Azure networking and security services for increased layered protection:

- **NSGs and Azure Firewall** -- Azure Firewall complements NSGs. Together they provide better **defense-in-depth** network security. NSGs provide distributed network-layer traffic filtering; Azure Firewall provides centralized network and application-level protection.
- **Azure Application Gateway WAF and Azure Firewall** -- WAF provides centralized inbound protection for web applications. Azure Firewall provides inbound protection for non-HTTP/S protocols and outbound network-level protection for all ports and protocols.

## Knowledge Check

1. Q: How can Tailwind Traders enforce having only certain applications run on its VMs?
   A: **Create an application control rule in Azure Security Center**. You can define a list of allowed applications to ensure only applications you allow can run. Azure Security Center can also detect and block malware.

2. Q: What is the easiest way to combine security data from all monitoring tools into a single report?
   A: **Collect security data in Azure Sentinel**. Azure Sentinel is Microsoft's cloud-based SIEM that aggregates security data from many different sources.

3. Q: What is the best way to safely store certificates so they are accessible to cloud VMs?
   A: **Store the certificates in Azure Key Vault**. It enables you to store secrets in a single, central location.

4. Q: How can Tailwind Traders ensure that certain VM workloads are physically isolated from other Azure customers?
   A: **Run the VMs on Azure Dedicated Host**. It provides dedicated physical servers to host your Azure VMs for Windows and Linux.

5. Q: An attacker sends a large volume of network traffic to your servers. Which Azure service protects your App Service instance?
   A: **Azure DDoS Protection** helps protect your Azure resources from DDoS attacks.

6. Q: What is the best way to limit all outbound traffic from VMs to known hosts?
   A: **Create application rules in Azure Firewall**. It enables you to limit outbound HTTP/S traffic to a specified list of FQDNs.

7. Q: How can Tailwind Traders most easily implement a deny by default policy so that VMs cannot connect to each other?
   A: **Create a network security group rule** that prevents access from another VM on the same network.

[<<](./index.md) | [home](../README.md)
