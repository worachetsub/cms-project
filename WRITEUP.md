# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

For the deployment of the FlaskWebProject, I chose to use Azure App Service instead of a Virtual Machine (VM). This decision was based on several factors:

Lightweight Application: The FlaskWebProject is a lightweight web application that does not require the extensive resources that a VM would provide. Azure App Service is well-suited for hosting small to medium-sized web applications efficiently.

Ease of Maintenance: Azure App Service simplifies the deployment and management of web applications. It provides built-in features such as automatic scaling, load balancing, and easy integration with CI/CD pipelines, which significantly reduces the operational overhead compared to managing a VM.

Cost-Effectiveness: Using Azure App Service can be more cost-effective for lightweight applications, as it allows for a pay-as-you-go pricing model without the need to provision and manage a full virtual machine.

Quick Deployment: Azure App Service offers a streamlined deployment process, allowing for rapid updates and changes to the application without the need for complex configurations.

Overall, the choice of Azure App Service aligns with the project requirements for a lightweight, easily maintainable web application, making it the ideal solution for deploying the FlaskWebProject.
