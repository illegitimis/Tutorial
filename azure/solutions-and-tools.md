# Solutions and Management Tools

## IoT Solutions

Azure provides several IoT services for connecting, monitoring, and managing IoT devices:

- **Azure IoT Hub** -- messaging hub that provides secure communications and monitoring of millions of IoT devices. Communicates by sending and receiving messages.
- **IoT Central** -- fully managed global IoT SaaS solution that quickly creates a web-based management portal to enable reporting and communication with IoT devices.
- **Azure Sphere** -- provides the highest degree of security to ensure devices have not been tampered with.

## AI and Machine Learning

Azure offers a range of AI and machine learning services:

- **Azure Machine Learning** -- enables you to build models to predict the likelihood of a future result. Cloud-based environment for developing, training, testing, deploying, managing, and tracking machine learning models.
- **Azure Cognitive Services** -- prebuilt APIs for solving complex problems, including vision services that can identify the content of an image. Ideal for identifying product images to automatically create alt tags.
- **Azure Bot Service** -- creates virtual agent solutions that utilize natural language. Ideal for creating human-computer interfaces that use natural language to answer customer questions.

## Serverless Computing

Azure provides two primary serverless compute options:

- **Azure Functions** -- execute code in response to events. Best for processing messages from a queue using existing imperative logic (e.g., written in Java) and sending them to a third-party API.
- **Azure Logic Apps** -- designer-first (declarative) approach to orchestrate workflows using APIs from well-known services. Best for teams with limited custom code experience that want to automate important business processes.

## DevTools

Azure DevOps brings together people, processes, and technology by automating software delivery:

- **Azure Pipelines** -- CI/CD tool for building an automated toolchain. It lacks features to assign individual developers tasks to work on, but it can automate other tools to assign tasks.
- **Azure Boards** -- project-management tool. Would not be used to automate a CI/CD process.
- **GitHub Actions** -- CI/CD automation integrated with GitHub repositories
- **Azure Repos** -- private Git repositories
- **Azure DevTest Labs** -- used to manage VMs for testing, including configuration, provisioning, and automatic de-provisioning. Ideal for managing VMs that developers and testers need across various operating systems.

## Monitoring

Azure provides tools for managing, configuring, and monitoring your environment:

### Management Tools

- **Azure CLI** -- enables you to use `Bash` to run one-off tasks on Azure. Best for retrieving IP addresses or running administrative commands.
- **Azure portal** -- best for newcomers setting up their first VM or performing initial configuration tasks.
- **Azure PowerShell** -- scripting and automation for Azure resource management.
- **ARM templates** -- the best _infrastructure-as-code_ option for quickly and reliably setting up your entire cloud infrastructure declaratively.

### Monitoring Services

- **Azure Advisor** -- provides recommendations to improve your cloud environment. Alerts you when new recommendations are available.
- **Azure Monitor** -- the platform that powers Application Insights, monitoring for VMs, containers, and Kubernetes. Does not supply root cause analyses (RCAs).
- **Azure Service Health** -- provides official outage root cause analyses (RCAs), incident history, and service health notifications for Azure incidents.

## Knowledge Check

1. Q: A company wants to build a new voting kiosk for sales to governments. Which IoT technology ensures the highest degree of security?
   A: **Azure Sphere** provides the highest degree of security to ensure the device has not been tampered with.

2. Q: A company wants to quickly manage its individual IoT devices by using a web-based user interface. Which IoT technology?
   A: **IoT Central** quickly creates a web-based management portal to enable reporting and communication with IoT devices.

3. Q: You want to send messages from the IoT device to the cloud and vice versa. Which IoT technology?
   A: **IoT Hub** communicates to IoT devices by sending and receiving messages.

4. Q: You need to predict future behavior based on previous actions. Which product?
   A: **Azure Machine Learning** enables you to build models to predict the likelihood of a future result.

5. Q: You need to create a human-computer interface that uses natural language to answer customer questions. Which product?
   A: **Azure Bot Service** creates virtual agent solutions that utilize natural language.

6. Q: You need to identify the content of product images to automatically create alt tags. Which product?
   A: **Azure Cognitive Services** provides vision services that can identify the content of an image.

7. Q: You need to process messages from a queue, parse them using existing imperative logic written in Java, and send them to a third-party API. Which serverless option?
   A: **Azure Functions**.

8. Q: You want to orchestrate a workflow by using APIs from several well-known services. Which option?
   A: **Azure Logic Apps**.

9. Q: Which choice would not be used to automate a CI/CD process?
   A: **Azure Boards** is a project-management tool, not a CI/CD automation tool.

10. Q: Which service could help manage VMs for testing across various operating systems?
    A: **Azure DevTest Labs** is used to manage VMs for testing, including configuration, provisioning, and automatic de-provisioning.

11. Q: Which service lacks features to assign individual developers tasks to work on?
    A: **Azure Pipelines** is a CI/CD tool for building an automated toolchain and lacks task assignment features.

12. Q: As an administrator, you need to retrieve the IP address from a particular VM by using Bash. Which tool?
    A: **Azure CLI** enables you to use Bash to run one-off tasks on Azure.

13. Q: You are a developer setting up your first VM. Which tool is best?
    A: **The Azure portal** is best for newcomers.

14. Q: What is the best infrastructure-as-code option for setting up your entire cloud infrastructure declaratively?
    A: **ARM templates**.

15. Q: You want to be alerted when new recommendations to improve your cloud environment are available. Which service?
    A: **Azure Advisor**.

16. Q: Which service provides official outage root cause analyses (RCAs) for Azure incidents?
    A: **Azure Service Health** provides incident history and RCAs.

17. Q: Which service is the platform that powers Application Insights, monitoring for VMs, containers, and Kubernetes?
    A: **Azure Monitor**.

[<<](./index.md) | [home](../README.md)
