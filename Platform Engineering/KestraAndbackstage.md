# Kestra
Kestra is an open-source platform for creating IDPs with YAML-based workflows.

### Key features:

Thousands of plugins for seamless integration with tools like Terraform, GitHub, and AWS.

Minimal coding requirement—only YAML knowledge needed.

Supports existing Terraform scripts and CI/CD pipelines.

Robust scalability and high availability.

Available as both open-source and SaaS offerings

## Kestra vs. Backstage
Backstage requires extensive knowledge of JavaScript, TypeScript, and its plugin ecosystem.

Kestra simplifies onboarding with easy-to-use blueprints and YAML workflows.

Offers better compatibility with existing DevOps infrastructure.

## Setting Up Kestra

Kestra can be installed locally using Docker Compose or deployed on cloud platforms (e.g., AWS).

Steps:

Install Kestra using Docker Compose.

Configure workflows with YAML files.

Use plugins to integrate with AWS, Kubernetes, and CI/CD pipelines.

Enable authentication and RBAC for secure access.

### Example: Creating an S3 bucket.

Define workflow metadata (ID, namespace).

Specify inputs for developer-provided values (e.g., bucket name).

Use plugins to automate tasks like S3 bucket creation.

Secrets (e.g., AWS keys) are encoded and managed securely.

Execution logs and analytics help monitor workflow performance.