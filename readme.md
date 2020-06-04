AppDirect is a sample Python Flask application used to test various technologies. This application is meant to be containerized and run in a Kubernetes Pod.

The current directory contains the following files:

* **Dockerfile:** This file is used to containerize AppDirect as 'cremerfc/appdirect'
* **Jenkinsfile:** This file does an scm checkout on the repository and builds the container, pushes it Docker Hub using the build number and 'latest' as the image tag. It then creates a new release version in Replicated.
