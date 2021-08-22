# Best practices used

* Precommit linting is used, Dockerfile passes it
* Based on docker alpine, which may slow down build for huge projects
    but works just fine with such a small project
* Base image version is fixed
* Apk dependency versions are fixed
* Application port is exposed
* Runs perfectly in any timezone
* Can be deployed via provided helm chart
