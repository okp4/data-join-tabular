---
noteId: "dc6b5190feb111ecae102f281db96559"
tags: []

---

# Data-join-tabular

> Template for Python Projects [@okp4](okp4.com).

[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

## Purpose & Philosophy

This repository contains data tabular join service.
**Description**:
2 sets of input data, giving 1 output with associated data based on a common column.
**Specification**:

- Read different file format (geojson, shp, xlsx, xsl, Xslx, csv)
- Optional argument depending on the type of input file (ex: separator for a csv)
- The name of the new columns created (suffix, prefix...)
- Type of join ('left', 'right', 'outer', 'inner', 'cross)
- Validate the output file

## Technologies

## [pandas.merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)

The join is done on columns or indexes. If joining columns on columns, the DataFrame indexes will be ignored. Otherwise if joining indexes on indexes or indexes on a column or columns, the index will be passed on. When performing a cross merge, no column specifications to merge on are allowed.

- the use of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/), [semantic versionning](https://semver.org/) and [semantic releasing](https://github.com/cycjimmy/semantic-release-action) which automates the whole package release workflow including: determining the next version number, generating the release notes, and publishing the artifacts (project tarball, docker images, etc.)
- a uniform way for managing the project lifecycle (depencencies management, building, testing)
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
                                  result DataFrame. If False, the order of the
                                  join keys depends on the join type (how
                                  keyword).
  -or, --onrigh TEXT              Column name to join in the right DataFrame.
  -ol, --onleft TEXT              Column name to join in the left DataFrame
  -out, --output DIRECTORY        output directory where output file will be
                                  written  [default: .]
  -f, --force                     overwrite existing file
  --dry-run                       passthrough, will not write anything
  --help                          Show this message and exit.
```

```shell
poetry run python3 src/data_join_tabular/main.py data-tabular-join -i1 ./data/inputs/DEPARTEMENT.shp -i2 ./data/inputs/ADECOGC_3-1_SHP_WGS84G_FRA/COMMUNE.shp -o INSEE_DEP -f -out ./data/outputs
```

## How to use

> 🚨 do not fork this repository as it is a [template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)

1. Click on [Use this template](https://github.com/okp4/template-python/generate)
2. Give a name to your project
3. Wait until the first run of CI finishes
4. Clone your new project and happy coding!

## System requirements

### Python

The repository targets python `3.9` and higher.

### Poetry

The repository uses [Poetry](https://python-poetry.org) as python packaging and dependency management. Be sure to have it properly installed before.

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

### Docker

You can follow the link below on how to install and configure **Docker** on your local machine:

- [Docker Install Documentation](https://docs.docker.com/install/)

## What's included

This template provides the following:

- [poetry](https://python-poetry.org) for dependency management.
- [flake8](https://flake8.pycqa.org) for linting python code.
- [mypy](http://mypy-lang.org/) for static type checks.
- [pytest](https://docs.pytest.org) for unit testing.

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

**Code linting** is performed by [flake8](https://flake8.pycqa.org).

```sh
poetry run flake8 --count --show-source --statistics
```

**Static type check** is performed by [mypy](http://mypy-lang.org/).

```sh
poetry run mypy .
```

To improve code quality, we use other linters in our workflows, if you don't want to be rejected by the CI,
please check these additional linters.

**Markdown linting** is performed by [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli).

```sh
markdownlint "**/*.md"  
```

**Docker linting** is performed by [dockerfilelint](https://github.com/replicatedhq/dockerfilelint) and
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

## Contributing

So you want to contribute? Great. We appreciate any help you're willing to give. Don't hesitate to open issues and/or submit pull requests.

Remember that this is the template we use at [OKP4](okp4.com/), and that we apply everywhere in our private and public Python projects. This is why we may have to refuse change requests simply because they do not comply with our internal requirements, and not because they are not relevant.
