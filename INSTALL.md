# Installation Guide

## Dependencies

The following libraries are required:

- [python 3.6+](https://www.python.org/downloads/release/python-360/) (ubuntu 18.04 or equivalent)
- [pip](https://pip.pypa.io/en/stable/)
- [pipenv](https://github.com/pypa/pipenv)

## Install dependencies

### Installing MariaDB or Mysql
Refer to the following [gudie](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
### Installing python

In ubuntu 18.04, `python 3.6` should be already installed. It can be checked using:

```bash
# NOTE: In this guide will use `python3` explicitly.
$ which python3
$ python3 -V
```

If `python` is not installed, install it.

```bash
$ sudo apt-get update -y
$ sudo apt-get install python3.6
```

### Installing Pip

We will not use `pip` from system package manager. We will do custom installation for `pip`.
To install `pip`, download installation script and install `pip`:

```bash
# install distutils
$ sudo apt install python3-distutils
$ cd

# the following will install `pip` in user environment.
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py
```

### Installing Pipenv

Install `pipenv` in user environment:

(To learn more: https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv)

```bash
$ pip install --user pipenv
```

To initialize python3 virtual environment, run:

```bash
$ cd /path/to/project

# NOTE: pipenv will automactically convert and create Piplock
# from requirements.txt.
$ pipenv --three

# pipenv will install required libraries.
$ pipenv install

# to activate python environment:
$ pipenv shell

# to deactivate python environment:
$ exit
```
## Configuration
Copy .env.example to .env with the database credentials you just created above. You can use any database name as long as it matches with the one you created.

## Testing app

To test the app, activate python environment first.

```bash
$ cd /path/to/project

# NOTE: activate environment if not activated yet.
$ pipenv shell

$ TESTING=true tox

$ exit
```

## Running webserver (with gunicorn)

To run webserver:

```bash
$ cd /path/to/project

$ pipenv shell

# Press Ctrl+C to stop web server
$ gunicorn wsgi:app
```
