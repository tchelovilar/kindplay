# kindplay

kindplay is an automation command line to setup a local Kubernetes cluster with a collection of addons using Helm charts.

It's a helpful tool to fast setup a reusable local cluster using yaml and helm charts to experiment tools and also create local development environment.

## How to Use

### Pre-requisites

1. Python and pip
2. Docker 
3. Kubernetes Kind tool. ([Install kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)) 
4. Helm. ([Install Helm](https://helm.sh/docs/intro/install/)) 

### Install kindplay

Use pip to install the kindplay package: 

```
pip install kindplay
```

### Create or use an existent playground structure

You can find a playground catalog at [tchelovilar/kind-playgrounds](https://github.com/tchelovilar/kind-playgrounds) repository. Once you have a playground structure, run `kindplay start` to start your cluster:

```
kindplay start <playground_path>
```

## Playground folder structure

kindplay use kind config file and helm charts to spin up the local kubernetes cluster.

**root\kind.yaml**

Contains the kind settings, you can find more from [kind documentation](https://kind.sigs.k8s.io/docs/user/configuration/).

**root\playground.yaml**

General special settings, can be used to specify extra commands or define the helm charts instalation order. 

**root\kubernetes**

Directory which contains folder structure composed by namespace and helm chart folder with helm
