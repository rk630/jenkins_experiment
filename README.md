
# jenkins_experiment

## Jenkins CI CD pipeline for flask application

### Objective:

Set up a Jenkins pipeline that automates the testing and deployment of a simple Python web application.

### Requirements:

1. Setup:

   - Install Jenkins on a virtual machine or use a cloud-based Jenkins service.

   - Configure Jenkins with Python and any necessary libraries.

2. Source Code:

  - Fork the provided Python web application repository on GitHub (provide a link to a sample Python web application repository).

  - Clone the forked repository into your Jenkins server.


3. Jenkins Pipeline:

   - Create a Jenkinsfile in the root of your Python application repository.

   - Define a pipeline with the following stages:

     - Build: Install dependencies using pip.

     - Test: Run unit tests using a testing framework like pytest.
![Screenshot 2024-01-04 155638](https://github.com/rk630/jenkins_experiment/assets/139606316/c300f590-9572-4c41-b8d1-24a41c715ccf)
     - Deploy: If tests pass, deploy the application to a staging environment.

![Screenshot 2024-01-04 155655](https://github.com/rk630/jenkins_experiment/assets/139606316/e1ffd3c8-6bec-4fae-819b-0025c835fa40)
![Screenshot 2024-01-04 155754](https://github.com/rk630/jenkins_experiment/assets/139606316/f98870cb-13a1-469a-add4-132269967953)


4. Triggers:

   - Configure the pipeline to trigger a new build whenever changes are pushed to the main branch of the repository.

5. Notifications:

   - Set up a notification system to alert via email when the build process fails or succeeds.
![image](https://github.com/rk630/jenkins_experiment/assets/139606316/ff9ee91b-3d39-42db-8c2c-7b138e8852fc)
![image](https://github.com/rk630/jenkins_experiment/assets/139606316/dee76873-4f73-48b2-9427-87d824c91895)

## GitHub Actions CI/CD Pipeline Flask App

### Objective:

# Implement a CI/CD workflow using GitHub Actions for a Python application.

## Requirements:


1. Setup:

   - Use a provided Python application repository on GitHub (provide a link to a sample Python application repository).

   - Ensure the repository has a main branch and a staging branch.


2. GitHub Actions Workflow:

   - Create a .github/workflows directory in your repository.

   - Inside the directory, create a YAML file to define the workflow.


3. Workflow Steps:

   - Define a workflow that performs the following jobs:

     - Install Dependencies: Install all necessary dependencies for the Python application using pip.

     - Run Tests: Execute the test suite using a framework like pytest.

     - Build: If tests pass, prepare the application for deployment.

     - Deploy to Staging: Deploy the application to a staging environment when changes are pushed to the staging branch.

     - Deploy to Production: Deploy the application to production when a release is tagged.


4. Environment Secrets:

   - Use GitHub Secrets to store sensitive information required for deployments (e.g., deployment keys, API tokens).

![Screenshot 2024-01-05 133346](https://github.com/rk630/jenkins_experiment/assets/139606316/c9a6a750-c538-4c2d-8bb5-21fdf5defcf1)

![image](https://github.com/rk630/jenkins_experiment/assets/139606316/7f79b8c0-aa56-41ce-9133-4718a15f78d3)
