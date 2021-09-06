# Docker setup

The playbook runs docker-compose on a VMs from group `label_service_application`.
Group is obtained from labels set in terraform.

## Install dependencies

```sh
ansible-galaxy install -r requirements.yml # for collections
```

## Test

We can use `Vagrant` to test playbook and see that it works as expected.
First you need to create a VM with docker via Vagrantfile in `docker` folder.
Our Vagrantfile references the same VM, so to run additional playbook with
our application, just run `vagrant provision` here.

```sh
vagrant provision
```
