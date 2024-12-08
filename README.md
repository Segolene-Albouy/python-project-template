.. image:: https://github.com/legau/kanon/workflows/CI/badge.svg
    :target: https://github.com/legau/kanon/actions
    :alt: GitHub Pipeline Status
.. image:: https://codecov.io/gh/legau/kanon/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/legau/kanon/branch/master
    :alt: Coverage
.. image:: https://readthedocs.org/projects/kanon/badge/?version=latest
    :target: https://kanon.readthedocs.io/en/latest/?badge=latest
    :alt: Docs status
.. image:: https://img.shields.io/pypi/v/kanon
    :target: https://pypi.org/project/kanon/
    :alt: Kanon Pypi
.. image:: https://shields.io/badge/python-v3.8-blue
    :target: https://www.python.org/downloads/release/python-380/
    :alt: Python 3.8
.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
    :target: http://www.astropy.org
    :alt: Powered by Astropy Badge
.. image:: https://zenodo.org/badge/344498058.svg
   :target: https://zenodo.org/badge/latestdoi/344498058


[![PyPI - Version](https://img.shields.io/pypi/v/panoptic.svg)](https://pypi.org/project/panoptic)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/panoptic.svg)](https://pypi.org/project/panoptic)


--------

**Kanon** is the History of Astronomy Python package and tools.

Current Features
________________

`units`

- Define standard positional numeral systems with standard arithmetics (`BasedReal`)
- Set your own precision contexts and algorithms on arithmetical operations (`PrecisionContext`)
- Keep track of all operations

`tables`

- Build or import ancient astronomical tables
- Perform arithmetical and statistical operations
- Support for `BasedReal` values

`calendars`

- Define new calendar types
- Date conversions

`models`

- Collection of mathematical models used for all kinds of geocentric astronomical tables

How to use
__________

Install the package with `pip`

.. code:: bash

    pip install kanon

Import Kanon and begin trying all its features

.. code:: python

    import kanon.units as u

    a = u.Sexagesimal(1,2,3)
    b = u.Sexagesimal(2,1,59)

    a + b
    # 3,4,2 ;


Development
___________

To start developing on this project you need to install
the package with `poetry` (`Installing Poetry <https://python-poetry.org/docs/>`)

.. code:: bash

    git clone https://github.com/legau/kanon.git
    cd kanon
    poetry install

The changes you make in the code are reflected on your Python environment.

Activate pre-commit checks :

.. code:: bash

    pre-commit install

Tests
_____

Run tests with tox

.. code:: bash

    # source code tests
    tox -e test

    # example notebooks tests
    tox -e test_notebooks

    # linting
    pre-commit run --all-files

# Python project template

> This repository is a template for Python projects.
> It includes a basic structure and files to get started with a new project with linting and testing.
> The following README gives template instructions for setting up the project.

# Project Title

A brief description of what the project does and its purpose.

> **Table of Contents**
>
> - [Getting Started](#getting-started)
> - [Installation](#installation)
> - [Contributing](#contributing)
> - [Contact](#contact)

## Getting Started

Instructions on setting up the project locally for development or testing.

### Prerequisites

- **Sudo** privileges
- **Python** >= 3.10
- **Git**: `sudo apt install git`

### Installation

Step-by-step instructions on how to install the project and its dependencies.

1. Clone the repository:
    ```bash
    git clone git@github.com:<username>/<repository>.git
    cd <repository>
    ```
2. Set up environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    pre-commit install
    ```
4. Run the project:
    ```bash
    python src/main.py
    ```

### Tests

Explain how to run the automated tests for this system.
```bash
pytest
```

## Contributing
Guidelines for contributing to the project:

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature`)
3. Commit your changes (`git commit -m '[FEATURE] addition of this feature'`)
4. Push to the branch (`git push origin feature`)
5. Open a Pull Request

## Contact

Your Name – your.email@example.com
