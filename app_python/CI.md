# Best practices for CI/CD

1. Use caching for docker builds
1. Good image naming (I used commit sha for usual commits and tag
   for MRs in OCI format). With this kind of naming images will not
   be accidentaly replaced, but still with major releases we can add
   some human-readable tag.
1. Build and push only tests are passed
1. No need to lint, as precommit is used and we
    do not expect unlinted code to be pushed
1. Secrets handled by github
