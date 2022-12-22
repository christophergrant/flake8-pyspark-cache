[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.flake8-match?branchName=main)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=69&branchName=main)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/69/main.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=69&branchName=main)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/flake8-match/main.svg)](https://results.pre-commit.ci/latest/github/asottile/flake8-match/main)

## disclaimer
this plugin, although tested, is not battle hardened just yet.

flake8-pyspark-cache
============

flake8 plugin which forbids DataFrame.cache()

## installation

```bash
pip install flake8-pyspark-cache
```

## flake8 codes

| Code   | Description          |
|--------|----------------------|
| PS002 | do not use cache() |

## rationale

lol

## as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/pycqa/flake8
    rev: 3.8.4
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-pyspark-cache==1.0.0]
```
