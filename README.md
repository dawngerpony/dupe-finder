# dupe-finder

![check](https://github.com/dawngerpony/dupe-finder/actions/workflows/check.yml/badge.svg)

Find duplicate files.

:warning: This is a personal project only! I have some specific needs and I'm also having fun.

## How to contribute

Prerequisites:

* [pipx] for running `tox`
* [pyenv]
* [pyenv-virtualenv]

Set up a Python 3.12 virtual environment:

```shell
pipx install tox
pyenv install 3.12
pyenv virtualenv 3.12 dupe-finder
```

Clone the repo, then in the root directory:

```shell
pyenv local dupe-finder
```

then:

```shell
pip install -r requirements-dev.txt
```

Run the tests:

```shell
pyenv
```

Run tox:

```shell
tox
```

## Project information

This project:

* uses [Typer] to provide CLI features
* runs [tox] during CI via [tox-gh]

## Resources

* <https://www.pythoncentral.io/finding-duplicate-files-with-python/>
* <https://deplicate.github.io/>
* <https://stackoverflow.com/questions/748675/finding-duplicate-files-and-removing-them>

[pipx]: https://pipx.pypa.io/stable/installation/
[pyenv]: https://github.com/pyenv/pyenv?tab=readme-ov-file#installation
[pyenv-virtualenv]: https://github.com/pyenv/pyenv-virtualenv
[tox]: https://tox.wiki
[tox-gh]: https://github.com/tox-dev/tox-gh
[typer]: https://typer.tiangolo.com
