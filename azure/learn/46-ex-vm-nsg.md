# Exercise - Configure network access to a VM by using a network security group

In this [exercise](https://docs.microsoft.com/en-us/learn/modules/secure-network-connectivity-azure/6-configure-access-network-security-group), you configure network access to a virtual machine (VM) running on Azure.

You start by creating a **Linux VM** and installing `Nginx`, a popular web server, on that VM. To make your web server accessible, you then *create a network security group* (NSG) rule that allows _inbound access on port 80_ (HTTP).

There are many ways to create and manage VMs, including their network settings. For example, you can use the Azure portal, the Azure CLI, Azure PowerShell, or an Azure Resource Manager (ARM) template.

Here, you use the Azure CLI. The Azure CLI enables you to connect to Azure and run administrative commands on Azure resources. As with other command-line interfaces, you can run commands directly from a terminal or you can add commands to a Bash script or a PowerShell script. The Azure CLI runs on Windows, macOS, or Linux.

Here, you access the Azure CLI from Azure Cloud Shell. Cloud Shell is a browser-based shell experience that you use to manage and develop Azure resources. Think of Cloud Shell as an interactive console that runs in the cloud.

## Create a Linux virtual machine and install Nginx

Use the following Azure CLI commands to create a Linux VM and install Nginx. After your VM is created, you'll use the Custom Script Extension to install Nginx. The `Custom Script Extension` is an easy way to download and run scripts on your Azure VMs. It's just one of the many ways you can configure the system after your VM is up and running.

1. From Cloud Shell, run the following az vm create command to create a Linux VM:

```sh
az vm create \
  --resource-group [sandbox resource group name] \
  --name my-vm \
  --image UbuntuLTS \
  --admin-username azureuser \
  --generate-ssh-keys
```

Your VM will take a few moments to come up.

```json
{
  "fqdns": "",
  "id": "/subscriptions/651da11b-7757-4742-ac91-148e47c2869b/resourceGroups/learn-eb451d26-c448-42bd-ae79-2de93ae5bef3/providers/Microsoft.Compute/virtualMachines/my-vm",
  "location": "westus",
  "macAddress": "00-0D-3A-32-D2-DF",
  "powerState": "VM running",
  "privateIpAddress": "10.0.0.4",
  "publicIpAddress": "104.210.54.131",
  "resourceGroup": "learn-eb451d26-c448-42bd-ae79-2de93ae5bef3",
  "zones": ""
}
```

You name the VM my-vm.
You use this name to refer to the VM in later steps.

2. Run the following az vm extension set command to configure Nginx on your VM:

```sh
az vm extension set \
  --resource-group [sandbox resource group name] \
  --vm-name my-vm \
  --name customScript \
  --publisher Microsoft.Azure.Extensions \
  --version 2.1 \
  --settings '{"fileUris":["https://raw.githubusercontent.com/MicrosoftDocs/mslearn-welcome-to-azure/master/configure-nginx.sh"]}' \
  --protected-settings '{"commandToExecute": "./configure-nginx.sh"}'
```

This command uses the Custom Script Extension to run a Bash script on your VM. The script is stored on GitHub.

While the command runs, you can choose to examine the [Bash script](https://raw.githubusercontent.com/MicrosoftDocs/mslearn-welcome-to-azure/master/configure-nginx.sh) from a separate browser tab.

To summarize, the script:

- Runs apt-get update to download the latest package information from the internet. This step helps ensure that the next command can locate the latest version of the Nginx package.
- Installs Nginx.
- Sets the home page, /var/www/html/index.html, to print a welcome message that includes your VM's host name.

```json
{
  "autoUpgradeMinorVersion": true,
  "enableAutomaticUpgrade": null,
  "forceUpdateTag": null,
  "id": "/subscriptions/651da11b-7757-4742-ac91-148e47c2869b/resourceGroups/learn-eb451d26-c448-42bd-ae79-2de93ae5bef3/providers/Microsoft.Compute/virtualMachines/my-vm/extensions/customScript",
  "instanceView": null,
  "location": "westus",
  "name": "customScript",
  "protectedSettings": null,
  "provisioningState": "Succeeded",
  "publisher": "Microsoft.Azure.Extensions",
  "resourceGroup": "learn-eb451d26-c448-42bd-ae79-2de93ae5bef3",
  "settings": {
    "fileUris": [
      "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-welcome-to-azure/master/configure-nginx.sh"
    ]
  },
  "suppressFailures": null,
  "tags": null,
  "type": "Microsoft.Compute/virtualMachines/extensions",
  "typeHandlerVersion": "2.1",
  "typePropertiesType": "customScript"
}
```

## Access your web server

In this procedure, you get the IP address for your VM and attempt to access your web server's home page.

1. Run the following az vm list-ip-addresses command to get your VM's IP address and store the result as a Bash variable:

```sh
IPADDRESS="$(az vm list-ip-addresses \
  --resource-group learn-eb451d26-c448-42bd-ae79-2de93ae5bef3 \
  --name my-vm \
  --query "[].virtualMachine.network.publicIpAddresses[*].ipAddress" \
  --output tsv)"
```

2. Run the following curl command to download the home page:

```Bash
curl --connect-timeout 5 http://$IPADDRESS
```
The --connect-timeout argument specifies to allow up to five seconds for the connection to occur. After five seconds, you see an error message that states that the connection timed out:

```Output
curl: (28) Connection timed out after 5001 milliseconds
```

This message means that the VM was not accessible within the timeout period.

3. As an optional step, try to access the web server from a browser:

Run the following to print your VM's IP address to the console:

```Bash
echo $IPADDRESS
```

You see an IP address, for example, 23.102.42.235 / 104.210.54.131.

Open a new browser tab and go to your web server.

After a few moments, you see that the connection isn't happening.
Hmmm… can't reach this page
104.210.54.131 took too long to respond

## List the current network security group rules

Your web server wasn't accessible. To find out why, let's examine your current NSG rules.

1. Run the following az network nsg list command to list the network security groups that are associated with your VM:

```sh
az network nsg list \
  --resource-group learn-eb451d26-c448-42bd-ae79-2de93ae5bef3 \
  --query '[].name' \
  --output tsv
```

You see this Output `my-vmNSG`. Every VM on Azure is associated with at least one network security group. In this case, Azure created an NSG for you called my-vmNSG.

2. Run the following az network nsg rule list command to list the rules associated with the NSG named my-vmNSG:

```Azure CLI
az network nsg rule list \
  --resource-group learn-eb451d26-c448-42bd-ae79-2de93ae5bef3 \
  --nsg-name my-vmNSG
```

You see a large block of text in JSON format in the output. In the next step, you'll run a similar command that makes this output easier to read.

```json
[
  {
    "access": "Allow",
    "description": null,
    "destinationAddressPrefix": "*",
    "destinationAddressPrefixes": [],
    "destinationApplicationSecurityGroups": null,
    "destinationPortRange": "22",
    "destinationPortRanges": [],
    "direction": "Inbound",
    "etag": "W/\"d4808b76-6829-440d-acab-fd63cab1e61e\"",
    "id": "/subscriptions/651da11b-7757-4742-ac91-148e47c2869b/resourceGroups/learn-eb451d26-c448-42bd-ae79-2de93ae5bef3/providers/Microsoft.Network/networkSecurityGroups/my-vmNSG/securityRules/default-allow-ssh",
    "name": "default-allow-ssh",
    "priority": 1000,
    "protocol": "Tcp",
    "provisioningState": "Succeeded",
    "resourceGroup": "learn-eb451d26-c448-42bd-ae79-2de93ae5bef3",
    "sourceAddressPrefix": "*",
    "sourceAddressPrefixes": [],
    "sourceApplicationSecurityGroups": null,
    "sourcePortRange": "*",
    "sourcePortRanges": [],
    "type": "Microsoft.Network/networkSecurityGroups/securityRules"
  }
]
```

3. Run the az network nsg rule list command a second time.

This time, use the --query argument to retrieve only the name, priority, affected ports, and access (Allow or Deny) for each rule.

The --output argument formats the output as a table so that it's easy to read.

```sh
az network nsg rule list \
  --resource-group learn-eb451d26-c448-42bd-ae79-2de93ae5bef3 \
  --nsg-name my-vmNSG \
  --query '[].{Name:name, Priority:priority, Port:destinationPortRange, Access:access}' \
  --output table
```

```output
Name               Priority    Port    Access
-----------------  ----------  ------  --------
default-allow-ssh  1000        22      Allow
```

You see the default rule, default-allow-ssh. This rule allows inbound connections over port 22 (SSH). SSH (Secure Shell) is a protocol that's used on Linux to allow administrators to access the system remotely.

The priority of this rule is 1000. Rules are processed in priority order, with lower numbers processed before higher numbers.

By default, a Linux VM's NSG allows network access only on port 22. This enables administrators to access the system. You need to also allow inbound connections on port 80, which allows access over HTTP.

## Create the network security rule

Here, you create a network security rule that allows inbound access on port 80 (HTTP).

1. Run the following az network nsg rule create command to create a rule called allow-http that allows inbound access on port 80:

```sh
az network nsg rule create \
  --resource-group learn-eb451d26-c448-42bd-ae79-2de93ae5bef3 \
  --nsg-name my-vmNSG \
  --name allow-http \
  --protocol tcp \
  --priority 100 \
  --destination-port-ranges 80 \
  --access Allow
```

For learning purposes, here you set the priority to 100. In this case, the priority doesn't matter. You would need to consider the priority if you had overlapping port ranges.

```json
{
  "access": "Allow",
  "description": null,
  "destinationAddressPrefix": "*",
  "destinationAddressPrefixes": [],
  "destinationApplicationSecurityGroups": null,
  "destinationPortRange": "80",
  "destinationPortRanges": [],
  "direction": "Inbound",
  "etag": "W/\"85d39786-f28c-4477-a463-72d9391fdbcf\"",
  "id": "/subscriptions/651da11b-7757-4742-ac91-148e47c2869b/resourceGroups/learn-eb451d26-c448-42bd-ae79-2de93ae5bef3/providers/Microsoft.Network/networkSecurityGroups/my-vmNSG/securityRules/allow-http",
  "name": "allow-http",
  "priority": 100,
  "protocol": "Tcp",
  "provisioningState": "Succeeded",
  "resourceGroup": "learn-eb451d26-c448-42bd-ae79-2de93ae5bef3",
  "sourceAddressPrefix": "*",
  "sourceAddressPrefixes": [],
  "sourceApplicationSecurityGroups": null,
  "sourcePortRange": "*",
  "sourcePortRanges": [],
  "type": "Microsoft.Network/networkSecurityGroups/securityRules"
}
```

2. To verify the configuration, run az network nsg rule list to see the updated list of rules:

` az network nsg rule list --resource-group learn-eb451d26-c448-42bd-ae79-2de93ae5bef3 --nsg-name my-vmNSG`

## Access your web server again

Now that you've configured network access to port 80, let's try to access the web server a second time.

```txt
acpopescu@Azure:~$ curl --connect-timeout 5 http://$IPADDRESS
<html><body><h2>Welcome to Azure! My name is my-vm.</h2></body></html>
```

delete resource group

```sh
az group delete --name ExampleResourceGroup
```

```output
(AuthorizationFailed) The client 'live.com#acpopescu@outlook.com' with object id '5fc0fce4-cef2-4efc-b36a-0ea7e8b6fa6a' does not have authorization to perform action 'Microsoft.Resources/subscriptions/resourcegroups/delete' over scope '/subscriptions/651da11b-7757-4742-ac91-148e47c2869b/resourcegroups/ExampleResourceGroup' or the scope is invalid. If access was recently granted, please refresh your credentials.
Code: AuthorizationFailed
```

`az group delete --name learn-eb451d26-c448-42bd-ae79-2de93ae5bef3`