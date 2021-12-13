# hippo

Main repository for the hippo project.

JIRA Project: https://hippo-the-app.atlassian.net/

## Introduction

The Hippo app allows users to run inference on custom medical images and get diagnoses. The app
will also include online training as a future feature.

Look forward to all the cool new features!

## Test Instructions

TBC

## Build Instructions

### Project Build

TBC

### Documentation Build

For this section ensure the poetry virtual environment is activated in the terminal.

Building the documentation runs in two stages:

1. Auto build documentation RST files for all modules in the hippo project:

    * `poetry run sphinx-apidoc -q -f -o docs\source hippo --implicit-namespaces`

2. Build final documentation set:

    * `.\docs\make.bat html`

The documentation can be viewed by opening the `.\docs\build\html\index.html` file.

## Contribution Guidelines

TBC

## Contributors

* Matei Moldoveanu (matei.moldoveanu@gmail.com)
* Yohahn Ribeiro (yohahnribeiro29@gmail.com)
