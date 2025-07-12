
## Basics

Make sure to understand the basics of building a PyPI package ([example tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)).

IMPORTANT UPDATE SINCE THE LAST PUSH: WE NEED TO USE A pyproject.toml FILE NOW.

## Requirements (PyPI)

* Create a [TestPyPI](https://test.pypi.org/) account
* Create a [PyPI](https://pypi.org/) account
* Install requirements for developers:

```sh
pip install --upgrade build
pip install --upgrade twine
```

## Build and publish

### Generate new version archives

Generate distribution archives (use Terminal in the directory `flusstools-pckg/`:

```sh
python3 -m build
```

### Setup testpypi / pypi (first-time use only)

Make sure you have a pypi user account and Token ready for uploading the package. I not, get it from https://test.pypi.org/manage/account/#api-tokens and https://pypi.org/manage/account/#api-tokens .

To enable tokens, create a .pypirc file in the HOME directory with the following contents (replace `<your-token>` with API tokens from testpypi and pypi):

```commandline
[distutils]
  index-servers =
    testpypi
    pypi
    flusstools-test
    flusstools

[testpypi]
  username = __token__
  password = <your-testpypi.org.token>
[pypi]
  username = __token__
  password = <your-pypi.org.token>
[flusstools-test]
  repository = https://pypi.org/project/flusstools/
  username = __token__
  password = <your-testpypi.org.token>
[flusstools]
  repository = https://pypi.org/project/flusstools/
  username = __token__
  password = <your-pypi.org.token>
```

### Upload distribution archives

```sh
python3 -m twine upload --repository testpypi dist/*

python3 -m twine upload --repository flusstools dist/*

```

That's it, thanks for contributing - please still test the usage!

## Test

1. Create a new environment and activate it to test if the upload and installation work
    * On *Linux*:</br>`python -m venv test_env`</br>`source test_env/bin/activate`
    * On *Windows* (with Anaconda):</br>`conda activate flusstools-test`
1. Install the new version of *flusstools* in the environment:
	* `pip install flusstools`
1. Launch python and import *flusstools*:
	* `python`
	* `>>> import flusstools`




## OLD

Make sure to understand the basics of building a PyPI package ([example tutorial](https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7)).

**Because of a Bug in GDAL, new versions of FlussTools must currently be build on Linux only. Windows will crash!**

## Requirements (PyPI)

* Create a [TestPyPI](https://test.pypi.org/) account
* Create a [PyPI](https://pypi.org/) account
* Install requirements for developers (in *Terminal*)</br>`pip install -r requirements_dev.txt`

## Build and push test version

If you made changes in *setup.py*, run first (and troubleshoot any error message):

```
python setup.py develop
```

Before adding a new version of *flusstools*, please inform about the severity and version numbering semantics on [python.org](https://www.python.org/dev/peps/pep-0440/).

1. `cd` to your local *flusstools* folder (in *Terminal*)
1. Create *flusstools* locally 
	* Linux (in Terminal): `sudo python setup.py sdist bdist_wheel`
	* Window (in Anaconda Prompt with flussenv): `python setup.py sdist bdist_wheel`
1. Upload the (new version) to TestPyPI (with your TestPyPI account):
	* `twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*`
	* If any error occurs, fix it and rebuild the package (previous step).
1. Create a new environment and activate it to test if the upload and installation work
    * On *Linux*:</br>`python -m venv test_env`</br>`source test_env/bin/activate`
    * On *Windows* (with Anaconda):</br>`conda activate flusstools-test`
1. Install the new version of *flusstools* in the environment:
	* `pip install -i https://test.pypi.org/simple/ flusstools`
1. Launch python and import *flusstools*:
	* `python`
	* `>>> import flusstools`

## Push to PyPI

If you could build and install the test version successfully, you can push the new version to PyPI. **Make sure to increase the `VERSION="major.minor.micro" in *ROOT/setup.py***. Then push to PyPI (with your PyPI account):

`twine upload dist/*`

## Create a new release on GitHub

Please note that we are currently still in the *growing* phase of *flusstools*. Since *version 0.2*, login at github.com and create a new *release* after merging branches.

## Update docs

Because `gdal` can still not be imported remotely on *readthedocs*, it is currently not possible that the docs automatically synchronize with the latest *flusstools* version. For this reason, please manually update your code also in the *flusstools-docs* repo:

```
git clone https://github.com/Ecohydraulics/flusstools-docs.git
cd flusstools-docs
```

Then copy your changed scripts locally to `flusstools-docs/flusstools/YOUR-MODULE`, along with possible changes in `flusstools-docs/docs/YOUR-MODULE.rst`. Push your update to the remote docs:

```
git add .
git commit -m "updated SOMETHING"
git pull --rebase
git push
```

Sebastian will be notified and regenerate the docs.
