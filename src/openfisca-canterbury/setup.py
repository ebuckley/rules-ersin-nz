from setuptools import setup, find_packages

setup(name='OpenFisca-Canterbury',
      version='1.0',
      description='An implementation of regional rules for canterbury',
      author='Ersin Buckley',
      author_email='ersin@mediasuite.co.nz',
      keywords='benefit microsimulation social tax',
      license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
      url='api.rules.ersin.nz',
      install_requires=[
          'OpenFisca-Core >= 24.3.0, < 25.0',
          'OpenFisca-Aotearoa >= 5.1.4'
      ],
      include_package_data=True,
      packages=find_packages(),
      extras_require={
          'test': [
              'flake8 >=3.4.0,<3.7.0',
              'flake8-print',
              'nose',
          ]
      },
      test_suite='nose.collector')