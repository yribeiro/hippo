# hippo

Main repository for the hippo project.

JIRA Project can be found [here](https://hippo-the-app.atlassian.net/).

## Introduction

The Hippo app allows users to run inference on custom medical images and get diagnoses. The app
will also include online training as a future feature.

Look forward to all the cool new features!

## Test Instructions

To run tests using the poetry virtual environment run the following command in the project root directory:

```bash
poetry run pytest .\tests\
```

To run tests and generate coverage reports run the following commands in the project root directory:

```bash
poetry run coverage erase
poetry run coverage run -m pytest -v -s
poetry run coverage report -m
```

## Build Instructions

### Project Build

TBC

### Documentation Build

Building the documentation runs in two stages. Run the following commands in a terminal in the project root folder:

1. Auto build documentation RST files for all modules in the hippo project:

    * `poetry run sphinx-apidoc -f -o docs\source hippo --implicit-namespaces`

2. Build final documentation set:

    * `poetry run sphinx-build -c docs\source -b html docs\source docs\build\html`

The documentation can be viewed by opening the `.\docs\build\html\index.html` file.

## Contribution Guidelines

TBC

## Pre-commit setup

Setting up the pre-commit library to run the pre-commit hooks whenever you commit your code is done as follows:

1. To setup pre-commit to run using poetry run the command :
    * `poetry run pre-commit install`

2. If you want to run the pre-commit checks manually run the command:
    * `poetry run pre-commit run --all-files`

## Dataset

The dataset used for training the model is located [here](https://www.kaggle.com/c/siim-isic-melanoma-classification/). The aim of the model is to identify malignant skin lesions. The dataset has 33126 images coming from 2056 different patients. Of the total images, 98% of them represent healthy skin lesions while 2% represent diseased ones.

The data is in [DICOM format](https://en.wikipedia.org/wiki/DICOM). Each .dicom file holds both the image and image metadata. The metadata of each image contains the following fields:

* Age
* Patient_id
* Sex
* Anatomy site
* Diagnosis (this is the type of lesion, while the malignant lesions are all melanomas, the benign lesions can be of different types)
* Benign/malignant flag

More thoughts on this can be found in a [google doc](https://docs.google.com/document/d/1w2Dpw_u-rHY7RAp5br8B-S1Gb5Nd7l3omIhqSkBfKgM/edit?usp=sharing)

## Contributors

* Matei Moldoveanu (matei.moldoveanu@gmail.com)
* Yohahn Ribeiro (yohahnribeiro29@gmail.com)
