# KOTS YAML File Overview

The following summarizes what has been modified in the yaml files found in the `/manifests` directory. The original files where copied from [this github template](https://github.com/replicatedhq/replicated-starter-kots/tree/master/manifests)

**config.yaml:** Created a *text* config option where the customer can enter a message to be diplayed on a web page. The message is displayed when the user browses to `http://<app-url>/msg`after the deployment is updated.

**config-map.yaml:** Created a config map key to use the value entered by the user in the config specified in the *config.yaml* file.

**Deployment.yaml:** Deploys the `cremerfc/appdirect:latest` container with a replicaset of 1. It is configured to expose port 5000 and use the value for the key configured in the *config-map.yaml* file as an environment variable.

