from setuptools import setup, find_packages

setup(name = 'exrepo',
      packages=['exrepo'],
      version='0.1',
      # packages=find_packages(),
      install_requires = ["numpy"],
      extras_require = {
        "scipy": ["scipy"],
      },
      package_dir={'exrepo': 'exrepo'},
      package_data={'exrepo': ['data/*']},
     )
