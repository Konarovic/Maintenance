## INFORMATION
Maintenance project based on a Kaggkle csv
The goal is to establish a model capable of predicting failures based on tool parameters. Based on machine learning algorithms.

## REPOSITERY

README.md                           informations about the project

maintenance.yml                     environment for conda

requirements.txt                    environment for streamlit

config.py                           python file for folders paths

streamlit.py                        streamlit app

model                               generated model with various extensions

notebook                            dataframe exploration + dataviz + model

src  
- utils  
    - Functions.py                  function to get custom metrics

## START

### 0- OS

Ubuntu

### 1- Installation

conda create -p ./env -f maintenance.yml

### 2- Model

> model/lgbmc_model.joblib

### 3- Notebook

- data exploration
- dataviz
- lazypredict / modelisation
- Fine tunning

I made some tests on dimension reduction using PCA, which could be used in conjunction with SMOTE. The final chosen model is a Light Gradient Boosting Machine classifier.