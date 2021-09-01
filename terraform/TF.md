# Best practices used for TF

1. Remote state. When multiple people work on the same project, it is good
    to prevent race condition. When state is managed remotely, the race
    condition is avoided. However, in this project it is redundant since
    I am the only developer
1. Using variables.tf to avoid hard-coding common values such as project,
    name, region, network etc.
1. Using service account with restricted access to API rather than own account
