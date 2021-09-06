# Docker setup

The playbook `docker` sets up Docker and installs Traefik as reverse proxy on
VMs from group `label_docker_true`. Group is obtained from labels set in terraform.
Since most apps are http ones, Traefik will automatically issue a certificate
and serve http/https traffic for them.

## Install dependencies

```sh
ansible-galaxy install -r requirements.yml # for roles
ansible-galaxy install -r requirements.yml # for collections
```

## Test

We can use `Vagrant` to test playbook and see that it works and installs docker
as expected:

```sh
vagrant up
```

Expected output would be:

```
docker_vagrant: Importing base box 'generic/debian10'...
==> docker_vagrant: Matching MAC address for NAT networking...
==> docker_vagrant: Checking if box 'generic/debian10' version '3.2.20' is
 up to date...
==> docker_vagrant: Setting the name of the VM:
 docker_docker_vagrant_1630942906263_69564
==> docker_vagrant: Clearing any previously set network interfaces...
==> docker_vagrant: Preparing network interfaces based on configuration...
    docker_vagrant: Adapter 1: nat
==> docker_vagrant: Forwarding ports...
    docker_vagrant: 22 (guest) => 2222 (host) (adapter 1)
==> docker_vagrant: Running 'pre-boot' VM customizations...
==> docker_vagrant: Booting VM...
==> docker_vagrant: Waiting for machine to boot. This may take a few minutes...
    docker_vagrant: SSH address: 127.0.0.1:2222
    docker_vagrant: SSH username: vagrant
    docker_vagrant: SSH auth method: private key
    docker_vagrant:
    docker_vagrant: Vagrant insecure key detected. Vagrant will automatically replace
    docker_vagrant: this with a newly generated keypair for better security.
    docker_vagrant:
    docker_vagrant: Inserting generated public key within guest...
    docker_vagrant: Removing insecure key from the guest if it's present...
    docker_vagrant: Key inserted! Disconnecting and reconnecting using new SSH key...
==> docker_vagrant: Machine booted and ready!
==> docker_vagrant: Checking for guest additions in VM...
    docker_vagrant: The guest additions on this VM do not match the installed
    docker_vagrant: VirtualBox! In most cases this is fine, but in rare cases it
    docker_vagrant: prevent things such as shared folders from working properly.
    docker_vagrant: shared folder errors, please make sure the guest additions
    docker_vagrant: virtual machine match the version of VirtualBox you have
    docker_vagrant: your host and reload your VM.
    docker_vagrant:
    docker_vagrant: Guest Additions Version: 5.2.0 r68940
    docker_vagrant: VirtualBox Version: 6.1
==> docker_vagrant: Running provisioner: ansible...
    docker_vagrant: Running ansible-playbook...
    .......
# Ansible output
    .......
PLAY RECAP *********************************************************************
docker_vagrant             : ok=20   changed=13   unreachable=0    failed=0
skipped=7    rescued=0    ignored=0
```
