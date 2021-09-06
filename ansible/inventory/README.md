# inventory

Get dynamic inventory from GCP

Documentation of dynamic inventory provider - [click](https://docs.ansible.com/ansible/latest/collections/google/cloud/gcp_compute_inventory.html#ansible-collections-google-cloud-gcp-compute-inventory).
Source code - [click](https://github.com/ansible-collections/google.cloud)

## Install dependencies

```
ansible-galaxy collection install -r requirements.yml # for collections
ansible-galaxy install -r requirements.yml # for roles
pip3 install -r requirements.txt
```

## Obtain key for ansible service account

SA is created via terraform, so just write

```sh
gcloud iam service-accounts keys create <keyfile-name>.json --iam-account=<service-account-name>@<project-id>.iam.gserviceaccount.com
```

## Test

For inventory test, we can simply write

```sh
ansible inventory -i inventory.gcp.yml --graph
```

and see something like

```
@all:
  |--@label_docker_true:
  |  |--34.135.4.189
  |--@label_environment_production:
  |  |--34.135.4.189
  |--@label_service_application:
  |  |--34.135.4.189
  |--@ungrouped:
  |--@zone_us_central1_a:
  |  |--34.135.4.189
```
