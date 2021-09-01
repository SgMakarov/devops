# Usage

First, you need to authorize into gcloud with `gcloud auth application-default login`
Second, run terraform you need a keyfile for the service account that manages terraform
(It is possible to do this with your credentials too, but the preferred way is using
service account dedicated only to terraform). Run

```
gcloud iam service-accounts keys create <keyfile-name>.json --iam-account=<service-account-name>@<project-id>.iam.gserviceaccount.com
```

Note, there are multiple variables used for the GCP VM deployment, you might want
to create `terraform.tfvars` file not to enter them manually on each run. It may
look like this:

```
network = "default"
project_id = <your project>
region = "us-central1"
```
