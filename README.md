# MarkovM

<p align="center">
    <a href="https://github.com/HH-MWB/markovm/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/markovm.svg"></a>
    <a href="https://pypi.org/project/markovm/"><img alt="PyPI Latest Release" src="https://img.shields.io/pypi/v/markovm.svg"></a>
    <a href="https://pypi.org/project/markovm/"><img alt="Package Status" src="https://img.shields.io/pypi/status/markovm.svg"></a>
    <a href="https://github.com/psf/black/"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
    <a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1"></a>
</p>

## Installation

Install from [Python Package Index](https://pypi.org/project/markovm/):

```sh
pip install markovm
```

Install from [Source Code](https://github.com/HH-MWB/markovm):

```sh
pip install .
```

## Quickstart

### Create Model

```python
>>> import markovm
>>> import numpy
>>> m = markovm.create_markov_model(
...     states=("A", "B", "C"),
...     transitions=numpy.array([
...         [0.0, 1.0, 0.0],  # A must goto B
...         [0.2, 0.0, 0.8],  # B can goto A (20%) or C (80%)
...         [0.0, 0.5, 0.5],  # C can goto B or stay
...     ]),
... )
```

### Random Walk

```python
>>> import itertools
>>> for state in itertools.islice(
...     markovm.random_walk(m, seed=0), 5
... ):
...     print(state)
... 
A
B
C
B
A
```
