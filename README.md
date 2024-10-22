# Data-join-tabular

[![version](https://img.shields.io/github/v/release/okp4/data-join-tabular?style=for-the-badge&logo=github)](https://github.com/okp4/data-join-tabular/releases)
[![lint](https://img.shields.io/github/actions/workflow/status/okp4/data-join-tabular/lint.yml?branch=main&label=lint&style=for-the-badge&logo=github)](https://github.com/okp4/data-join-tabular/actions/workflows/lint.yml)
[![build](https://img.shields.io/github/actions/workflow/status/okp4/data-join-tabular/build.yml?branch=main&label=build&style=for-the-badge&logo=github)](https://github.com/okp4/data-join-tabular/actions/workflows/build.yml)
[![test](https://img.shields.io/github/actions/workflow/status/okp4/data-join-tabular/test.yml?branch=main&label=test&style=for-the-badge&logo=github)](https://github.com/okp4/data-join-tabular/actions/workflows/test.yml)
[![codecov](https://img.shields.io/codecov/c/github/okp4/data-join-tabular?style=for-the-badge&token=G5OBC2RQKX&logo=codecov)](https://codecov.io/gh/okp4/data-join-tabular)
[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=for-the-badge&logo=conventionalcommits)](https://conventionalcommits.org)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg?style=for-the-badge)](https://github.com/semantic-release/semantic-release)
[![contributor covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=for-the-badge)](https://github.com/okp4/.github/blob/main/CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=for-the-badge)](https://opensource.org/licenses/BSD-3-Clause)

## Purpose & Philosophy

This repository contains data tabular join service.

### Description

2 sets of input data, giving 1 output with associated data based on a common column.

### Specification

- Read different file format (csv, geojson, shp)
- Optional argument depending on the type of input file (ex: separator for a csv)
- The name of the new columns created (suffix, prefix...)
- Type of join ('left', 'right', 'outer', 'inner', 'cross)
- Validate the output data

## Technologies

__[pandas.merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)__

The join is done on columns or indexes. If joining columns on columns, the DataFrame indexes will be ignored. Otherwise if joining indexes on indexes or indexes on a column or columns, the index will be passed on. When performing a cross merge, no column specifications to merge on are allowed.

- the use of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/), [semantic versioning](https://semver.org/) and [semantic releasing](https://github.com/cycjimmy/semantic-release-action) which automates the whole package release workflow including: determining the next version number, generating the release notes, and publishing the artifacts (project tarball, docker images, etc.)
- a uniform way for managing the project lifecycle (dependencies management, building, testing)
- KISS principles: simple for developers
- a consistent coding style
  
## Usage

The usage is given as follows:

```sh
Usage: data-join-tabular join [OPTIONS]

  Represents cli 'join' command

Options:
  -i1, --input1 FILE              path to first file to join  [required]
  -i2, --input2 FILE              path to second file to join  [required]
  -s1, --sep1 TEXT                separtor for reading the first file
  -s2, --sep2 TEXT                separtor for reading the second file
  -sr, --sufrigh TEXT             the suffix to add to overlapping column
                                  names in right
  -sl, --sufleft TEXT             the suffix to add to overlapping column
                                  names in left
  -onm, --outname TEXT            output file name, if not provioded, output
                                  name will be the same as file1
  -o, --on TEXT                   Column or index level names to join on.
                                  These must be found in both DataFrames.
                                  If on is None and not merging on indexes
                                  then this defaults to the intersection of
                                  the columns in both DataFrames
  -v, --validate [one_to_one|one_to_many|many_to_one|many_to_many]
                                  If specified, checks if merge is of
                                  specified type.        “one_to_one” or
                                  “1:1”: check if merge keys are unique in
                                  both left and right datasets.
                                  “one_to_many” or “1:m”: check if merge keys
                                  are unique in left dataset.
                                  “many_to_one” or “m:1”: check if merge keys
                                  are unique in right dataset.
                                  “many_to_many” or “m:m”: allowed, but does
                                  not result in checks.
                                  It will raise a MergeError if the validation fails
  -how, --how [left|right|outer|inner|cross]
                                  Type of merge to be performed.    left: use
                                  only keys from left frame, similar to a SQL
                                  left outer join; preserve key order.
                                  right: use only keys from right frame,
                                  similar to a SQL right outer join; preserve
                                  key order.    outer: use union of keys from
                                  both frames, similar to a SQL full outer
                                  join; sort keys lexicographically.    inner:
                                  use intersection of keys from both frames,
                                  similar to a SQL inner join; preserve the
                                  order of the left keys.    cross: creates
                                  the cartesian product from both frames,
                                  preserves the order of the left keys.
  -so, --sort TEXT                Sort the join keys lexicographically in the
                                  result DataFrame. If False,        the order
                                  of the join keys depends on the join type
                                  (how keyword).
  -or, --onrigh TEXT              Column name to join in the right DataFrame
  -ol, --onleft TEXT              Column name to join in the left DataFrame, 
                                  it must be sorted to match the on_right columns
  -out, --output DIRECTORY        output directory where output file will be
                                  written  [default: .]
  -f, --force                     overwrite existing file
  -ft, --fix-types                fix types issues
  --dry-run                       passthrough, will not write anything
  --help                          Show this message and exit.
```

```shell
poetry run data-join-tabular  join -i1 ./tests/data/inputs1/input_test1.csv -i2 ./tests/data/inputs2/input_test1.csv -o categorie -o statut -o effectif -o genre -s1 ';' -s2 ';' -out ./tests/data -f
```

## System requirements

### Python

The repository targets python `3.9` and higher.

### Poetry

The repository uses [Poetry](https://python-poetry.org) as python packaging and dependency management. Be sure to have it properly installed before.

```sh
  curl -sSL https://install.python-poetry.org | python3 
```

### Docker

You can follow the link below on how to install and configure __Docker__ on your local machine:

- [Docker Install Documentation](https://docs.docker.com/install/)

## What's included

This template provides the following:

- [poetry](https://python-poetry.org) for dependency management.
- [flake8](https://flake8.pycqa.org) for linting python code.
- [mypy](http://mypy-lang.org/) for static type checks.
- [pytest](https://docs.pytest.org) for unit testing.
- [click](https://palletsprojects.com/p/click/) to easily setup your project commands

The project is also configured to enforce code quality by declaring some CI workflows:

- conventional commits
- lint
- unit test
- semantic release

## Everyday activity

### Build

Project is built by [poetry](https://python-poetry.org).

```sh
poetry install
```

### Lint

> ⚠️ Be sure to write code compliant with linters or else you'll be rejected by the CI.

__Code linting__ is performed by [flake8](https://flake8.pycqa.org).

```sh
poetry run flake8 --count --show-source --statistics
```

__Static type check__ is performed by [mypy](http://mypy-lang.org/).

```sh
poetry run mypy .
```

To improve code quality, we use other linters in our workflows, if you don't want to be rejected by the CI,
please check these additional linters.

__Markdown linting__ is performed by [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli).

```sh
markdownlint "**/*.md"  
```

__Docker linting__ is performed by [dockerfilelint](https://github.com/replicatedhq/dockerfilelint) and
[hadolint](https://github.com/hadolint/hadolint).

```sh
dockerfilelint Dockerfile
```

```sh
hadolint Dockerfile
```

### Unit Test

> ⚠️ Be sure to write tests that succeed or else you'll be rejected by the CI.

Unit tests are performed by the [pytest](https://docs.pytest.org) testing framework.

```sh
poetry run pytest -v
```

### Build & run docker image (locally)

Build a local docker image using the following command line:

```sh
docker build -t data-join-tabular .
```

Once built, you can run the container locally with the following command line:

```sh
docker run -ti --rm data-join-tabular
```

## You want to get involved? 😍

Please check out OKP4 health files :

- [Contributing](https://github.com/okp4/.github/blob/main/CONTRIBUTING.md)
- [Code of conduct](https://github.com/okp4/.github/blob/main/CODE_OF_CONDUCT.md)
