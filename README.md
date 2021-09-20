
# F21 DevOps homeworks

## About The Project

### Project structure

```
├── ansible
│   ├── application
│   ├── docker
│   └── inventory
├── app_python
├── helm
│   └── templates
├── k8s
├── monitoring
│   ├── screenshots
│   └── secrets
├── terraform
│   └── pub_keys
└── vagrant
```

### Project description

[![Test and build](https://github.com/SgMakarov/devops/actions/workflows/CI.yml/badge.svg)](https://github.com/SgMakarov/devops/actions/workflows/CI.yml)

This is a simple python app that returns UTC time and local time
(Moscow by default, but can be changed).
It is built on top of lightweight [Chrony](https://git.tuxfamily.org/chrony/chrony.git/tree/)
ntp server to provide precise time,no matter in which timezone it is runned.
This server by default is configured to sync with UTC servers, so in my app
I simply return this time, udjusted to the timezone provided.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

The application runs in a docker container.

* docker

    ```sh
    curl -sLS get.docker.com | sh
    ```

### Run application

1. Pull the docker image

   ```sh
   docker pull sgmakarov/devops:latest
   ```

1. Run it with

   ```sh
   # without --cap-add chrony will not be allowed to set time inside container
   docker run -d --cap-add SYS_TIME -p 127.0.0.1:5000:5000  sgmakarov/devops:latest
   ```

1. Go to [localhost](http://localhost:5000/)

### Build locally

```sh
docker build [-t image:tage] app_python
```

## Usage

### Setting custom timezone

By default, `Europe/Moscow` is used. However, this can be changed:

```sh
# provide custom timezone via environment variable
docker run -d --cap-add SYS_TIME -p 127.0.0.1:5000:5000 -e TZ='US/Central' sgmakarov/devops:latest
```

### Running with helm

Another option is to run it with helm. Just set values you want to change in `helm/values.yaml`
   and run

```sh
helm upgrade --install <Release name> [-n <namespace>] helm/
```

## Unit tests

To run unit tests, you need to either run `pytest` locally (with installed `requirements.test.txt`)
   or simply build a test docker image via `Dockerfile.test`

## CI

### Github Actions

It just works, you may take a look on them in `.github/workflows/CI.yaml`

### Jenkins

To run a pipeline you will need to:

1. Run jenkins with

   ```sh
   docker run --rm --name jenkins -p 8080:8080 -p 50000:50000 -u 0 -v \
   pwd:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock \
   jenkinsci/blueocean
   ```

1. Install Docker plugin
1. Set up credentials for github and dockerhub in settings
1. Run a pipeline
1. Get result

![](https://i.imgur.com/iZ3pZcw.png)

## Infrastructure as a code

### Local testing

For local usage we have Vagrant. Just run `vagrant up` in `vagrant` folder,
I have set up a simple VM. Vagrant can automatically provision ansible playbooks
on this VM, which will be useful later.

### VPC provider

For VPC management we will use terraform.

The detailed usage will be covered in `terraform/README.md`.

### Ansible

General workflow with ansible is the following:

1. Obtain the key with the command provided in ansible inventory `README.md`

1. Run docker playbook

```sh
ansible-playbook -i inventory/inventory.gcp.yml -u serveruser docker/docker.yml
```

1. Run application playbook with similar command
