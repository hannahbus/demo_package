# HBussi

Demo package!

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


