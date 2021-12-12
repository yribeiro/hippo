# hippo
Main repository for the hippo project. 

JIRA Project: https://hippo-the-app.atlassian.net/

# Introduction

The Hippo app allows users to run inference on custom medical images and get diagnoses. The app
will also include online training as a future feature.

Look forward to all the cool new features!

# Test Instructions

TBC

# Build Instructions

TBC

# Contribution Guidelines

TBC

 # Contributors
 Matei Moldoveanu (matei.moldoveanu@gmail.com)
 Yohahn Ribeiro (yohahnribeiro29@gmail.com)

# Dataset

The dataset used for training the model is https://www.kaggle.com/c/siim-isic-melanoma-classification/. The aim of the model is to identify malign skin leasions. The dataset has 33126 images coming from 2056 different patients. OF the total iamges 98% of them represent healthy skin leasions while 2% represent diseased ones. 
The data is in DICOM format. Each dicom file holds both the image and image metadata. The matadata of each image contains:
- Age
- Patient_id
- Sex
- Anatomy site
- Diagnosis (this is the type of leasion, while the malign leasions are all melanomas, the benign leasions can be of different types)
- Benign/malign flag

More thoughts on this can be found in a google doc : https://docs.google.com/document/d/1w2Dpw_u-rHY7RAp5br8B-S1Gb5Nd7l3omIhqSkBfKgM/edit?usp=sharing
