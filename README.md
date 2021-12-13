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

Building the documentation runs in two stages. Run the following commands in a terminal in the project root folder:

1. Auto build documentation RST files for all modules in the hippo project:

    * `poetry run sphinx-apidoc -q -f -o docs\source hippo --implicit-namespaces`

2. Build final documentation set:

    * `poetry run sphinx-build -q -b html docs\source docs\build\html`

The documentation can be viewed by opening the `.\docs\build\html\index.html` file.

## Contribution Guidelines

TBC

## Contributors

* Matei Moldoveanu (matei.moldoveanu@gmail.com)
* Yohahn Ribeiro (yohahnribeiro29@gmail.com)
