# Best practices used

* Precommit linting is used, app and requirements pass it
* Uses flask, which is very lightweight, so fits good in for such a simple app
* Timezone is not hardcoded, ENV is used instead
* Proper .gitignore added
* Pytest unit tests present, they check response code,
    and if app returns datetime in ISO format
