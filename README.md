# Hello World Docker action based on Python

[![Unit Test](https://github.com/p2well/gha-template-python/actions/workflows/unit-test.yml/badge.svg)](https://github.com/p2well/gha-template-python/actions/workflows/unit-test.yml)

This action prints "Hello World" to the log or "Hello" + the name of a person to greet. To learn how this action was built, see "[Creating a Docker container action](https://help.github.com/en/articles/creating-a-docker-container-action)" in the GitHub Help documentation.

## Inputs

### `who-to-greet`

**Required** The name of the person to greet. Default `"World"`.

## Outputs

### `time`

The time we greeted you.

## Example usage

```yaml
uses: p2well/gha-template-python@main
with:
  who-to-greet: 'Mona the Octocat'
```
