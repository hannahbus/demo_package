from distutils.core import setup
setup(
  name = 'hbussi',         # How you named your package folder (MyLib)
  packages = ['hbussi'],   # Chose the same as "name"
  version = '4.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TEST',   # Give a short description about your library
  author = 'hannahbussi',                   # Type in your name
  author_email = 'hannah.busshoff@unisg.ch',      # Type in your E-Mail
  url = 'https://github.com/hannahbus/hbussi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/hannahbus/hbussi/archive/refs/tags/v4.0.tar.gz',    # I explain this later on
  keywords = ['TEST'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
