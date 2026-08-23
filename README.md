# SecureCloud

SecureCloud is a practical DevSecOps portfolio project demonstrating how to build, test, containerize, secure, and deploy a Python API to Microsoft Azure.

The project combines application development, containerization, CI/CD, Infrastructure as Code, cloud deployment, database integration, and security scanning into one end-to-end workflow.

## Project Objective

The objective of SecureCloud is to demonstrate a complete cloud application delivery lifecycle:

Developer
    |
    v
Git
    |
    v
GitHub
    |
    v
GitHub Actions CI
    |
    +-------------------+-------------------+
    |                   |                   |
    v                   v                   v
  pytest              Bandit              Trivy
    |                   |                   |
    +-------------------+-------------------+
                        |
                        v
                  Docker Build
                        |
                        v
             Azure Container Registry
                        |
                        v
              Azure Container Apps
                        |
                        v
                   FastAPI API
                        |
                        v
                Azure PostgreSQL

Terraform is used for Infrastructure as Code for the Azure environment.

## Technology Stack

### Application

- Python
- FastAPI
- Pydantic
- Psycopg
- PostgreSQL

### DevOps

- Git
- GitHub
- GitHub Actions
- Docker
- Terraform

### Security

- Bandit
- Trivy
- Non-root Docker container
- Container vulnerability analysis
- Secret-based database configuration

### Cloud

- Microsoft Azure
- Azure Container Registry
- Azure Container Apps
- Azure Database for PostgreSQL Flexible Server
- Azure Managed Identity
- Azure Log Analytics

## Application Features

The API provides:

- Health check endpoint
- PostgreSQL connectivity verification
- Create item
- Read items
- Update item
- Delete item
- Input validation
- HTTP error handling

## Current Project Status

The application has been successfully deployed to Azure and verified through the live HTTPS endpoint.

The following have been demonstrated:

- FastAPI application running in Docker
- PostgreSQL database connectivity
- CRUD operations
- Automated tests
- GitHub Actions CI
- Bandit security scanning
- Trivy container scanning
- Terraform infrastructure validation
- Azure Container Registry
- Azure Container Apps deployment
- Live HTTPS API verification
- Database credential rotation

## DevSecOps Lifecycle

Code
  |
  v
Version Control
  |
  v
Automated Testing
  |
  v
Static Security Analysis
  |
  v
Container Build
  |
  v
Container Security Scan
  |
  v
Cloud Deployment
  |
  v
Live Verification

## Security Controls

Current security controls include:

- Bandit static application security analysis
- Trivy container vulnerability scanning
- Non-root container execution
- OS package updates during Docker image build
- Secret-based database configuration
- HTTPS API endpoint
- Automated CI testing
- Infrastructure validation with Terraform

## Verification Evidence

The deployed application was successfully verified through the live Azure endpoint.

Health check:

    status    database
    ------    --------
    healthy   connected

CRUD verification was also completed against the live Azure API:

    POST    /items
    GET     /items
    PUT     /items/{id}
    DELETE  /items/{id}

The final GitHub Actions pipeline completed successfully.

Terraform reported:

    No changes. Your infrastructure matches the configuration.

## Project Structure

SecureCloud/
|
+-- app/
|   +-- main.py
|
+-- tests/
|   +-- test_main.py
|
+-- infrastructure/
|   +-- terraform/
|       +-- main.tf
|
+-- .github/
|   +-- workflows/
|       +-- ci.yml
|
+-- Dockerfile
+-- requirements.txt
+-- schema.sql
+-- .trivyignore
+-- README.md

## Learning Goals

This project is being developed to build practical experience in:

- Linux
- Python
- Git and GitHub
- Docker
- CI/CD
- Terraform
- Microsoft Azure
- Cloud Security
- DevSecOps
- Infrastructure as Code
- Container Security

## Future Improvements

Planned improvements include:

- Authentication and authorization
- Dependency vulnerability scanning
- Secret scanning
- Infrastructure security scanning
- SBOM generation
- Improved monitoring and observability
- Threat modeling
- Stronger cloud security controls
- Security-gated CI/CD deployment
- Improved Azure infrastructure automation