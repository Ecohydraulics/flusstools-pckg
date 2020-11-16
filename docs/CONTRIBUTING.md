## Basics

Make sure to understand the basics of building a PyPI package ([example tutorial](https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7)).

## Requirements (PyPI)

* Create a [TestPyPI](https://test.pypi.org/) account
* Create a [PyPI](https://pypi.org/) account 
* Install requirements for developers (in *Terminal*)</br>`pip install -r requirements_dev.txt`

## Build and push test version

If you made changes in *setup.py*, run first (and troubleshoot any error message):

```
python setup.py develop
```

1. `cd` to your local *flusstools* folder (in *Terminal*)
1. Create *flusstools* locally </br>`python setup.py sdist bdist_wheel` 
1. Upload the (new version) to TestPyPI (with your TestPyPI account):</br>`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`</br>*If any error occurs, fix it and rebuild the package (previous step).
1. Create a new environment and activate it to test if the upload and installation work
    * On *Linux*:</br>`python -m venv test_env`</br>`source test_env/bin/activate`
    * On *Windows* (with Anaconda):</br>`conda activate flusstools-test`
1. Install the new version of *flusstools* in the environment:</br>`pip install -i https://test.pypi.org/simple/ flusstools`
1. Launch python and import *flusstools*:</br>`python`</br>`>>> import flusstools`

## Push to PyPI

If you could build and install the test version successfully, you can push the new version to PyPI. **Make sure to increase the `"major.minor.micro"` version number in *ROOT/__init__.py***. Then push to PyPI (with your PyPI account):

`twine upload dist/*`

## Create a new release on GitHub

Please note that we are currently still in the *growing* phase of *flusstools* (version < 0.2). Since *version 0.2*, login at github.com and create a new *release* after merging branches.


