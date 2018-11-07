# What is this?
A knowledge base for understanding and working with openfisca-aotearoa

# Getting started

```
sudo apt install libyaml-dev
git clone --recursive # get all the submodules
pipenv install --two 
```


# Playbooks
Before you run any commands:
1. Do all the steps under #getting-started.
2. make sure that you have activated your environment by using `pipenv shell`.

## Starting the api
```
openfisca serve --port 5000
```

## Starting the legislation explorer..

This component allows you to navigate and search through the definition of legislation

```
cd legislation-explorer
npm install
npm build
npm run start
```

## running a test
Test cases are core to the implementation of legislation as code
```
# from the project root directory
openfisca-run-test openfisca-aotearoa/openfisca_aotearoa/tests/income_tax/family_scheme/minimum_family_tax_credit.yaml
```



# Use cases
There is some prior art on the core documentation [here](https://openfisca.org/doc/openfisca-web-api/index.html#use-cases). But we have identified the following potential use-cases/

## Building local govt rules that depend on openfisca-aotearoa

## Creating tools that depend on openfisca-aotearoa

## Simulation
