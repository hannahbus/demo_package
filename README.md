# HBussi

Demo package!

To upload new versions on PyPi follow the routine: 

(1) First navigate to the correct directory 

(2) Make sure that the version in the *setup.py* file and the link to the release on Github is correct

(3) Then, run the following commands in the terminal

```
python setup.py sdist 
twine upload --skip-existing dist/*
```

You are all set, a new release of your package should be available on PyPI!


## Demo 

In the Anaconda Prompt (Windows) or Terminal (Unix-based OS) type

````
pip install hbussi==4.0 
python 
from hbussi import beautify 
PRIMES = [123, 456, 99484848, 890933] 
beautify.main(PRIMES)
```
