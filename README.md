
# F21 DevOps homeworks

## About The Project

### Project structure

```
├── app_python
│   ├── app.py
│   ├── Dockerfile
│   ├── DOCKER.md
│   ├── example.env
│   ├── PYTHON.md
│   └── requirements.txt
├── helm
│   ├── .helmignore
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── templates (folder)
└── README.md
```

### Project description

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
   docker pull sgmakarov/devops:lab1
   ```

1. Run it with

   ```sh
   # without --cap-add chrony will not be allowed to set time inside container
   docker run -d --cap-add SYS_TIME -p 127.0.0.1:5000:5000  sgmakarov/devops:lab1
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
docker run -d --cap-add SYS_TIME -p 127.0.0.1:5000:5000 -e TZ='US/Central' sgmakarov/devops:lab1
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
