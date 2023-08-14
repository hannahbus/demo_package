# Demo package!

To upload new versions on PyPi follow the routine: 

(1) First navigate to the correct directory 

(2) Make sure that the version in the *setup.py* file is correct (specifying a correct version)

(3) Then, run the following commands in the terminal

(4) Make sure that you specify the correct version in the directory dist

```
python setup.py sdist 
twine upload --skip-existing dist/*
```

You are all set, a new release of your package should be available on PyPI!


# Testing the Demo package!

Before uploading the package on PyPI, include TestPyPI in the workflow. This is to test the package, in particular, the ``setup.py`` in new environments and different OS. 

(0) Set up a TestPyPI account. Apparently, it is not uncommon to be deleted. So don't worry and re-register [here](https://test.pypi.org/account/register/)

(1) Again, make sure that the *setup.py* is correct (package and Python versioning). The new default is to specify package versions with ``==``. This is to rule out possible issues introduced by other packages being updated more frequently.

(2) Navigate to the correct directory in the terminal.

```
python setup.py sdist
```

(3) Upload the package ``foo`` as follows (presuming you have already uploaded the package before on TestPyPI)

```
twine upload --verbose --repository testpypi --skip-existing dist/*
```

(4) Install as follows (addition ``--extra-index-url`` for install requires in ``setup.py`` to work as well)

```
python3 --extra-index-url pip install --index-url https://test.pypi.org/simple/ foo
```
For Windows relate commands refer to the [official documentation](https://packaging.python.org/en/latest/guides/using-testpypi/)
