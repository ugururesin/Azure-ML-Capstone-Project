# Capstone Project - Machine Learning Engineer with Microsoft Azure

## Table of Content
* [Overview](#overview)
* [The Project Flow](#the-project-flow)
* [Project Main Steps](#project-main-steps)
    * [1. The Dataset](#the-dataset)
    * [2. Automated ML Experiment](#automated-ml)
    * [3. HyperDrive](#hyperdrive)
    * [4. Result Comparison](#result-comparison)
    * [5. Model Deployment](#model-deployment)
    * [6. Testing the Model and Endpoint](#testing-the-model-and-endpoint)
    * [7. Documentation](table-of-content)
* [Screen Recording](#Screen-Recording-with-Subtitles)
* [Future Improvement Suggestions](#future-improvement-suggestions)

## Overview
This project is part of the Udacity Azure ML Nanodegree.
In this project, I will use both automated ML and HyperDrive to create two models to solve a task. I will then compare the performance of both these models and deploy the best-performing model. To complete this project, I will be using both the HyperDrive and Auto ML API from Azure ML. I first I determined the data I want. The data I choose needs to be external and not available in the Azure ecosystem. Thus I validate it using this link [Azure Datasets Catalog](https://docs.microsoft.com/en-us/azure/open-datasets/dataset-catalog).

Thus, in this project, the [Heart Failure Prediction](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) dataset from Kaggle is used. This dataset can be used to predict mortality from heart failure.

After I have chosen a dataset, I have to import the dataset into my workspace. Next, I will train a model on that dataset using automated ML and then train a custom model whose hyperparameters are tuned using HyperDrive. After I have trained the models, I have to compare their performance, deploy the best model as a web service, and then test the model endpoint. After I have tested the model endpoint, I will have to complete a README file that describes the project and my results.

## The Project Flow
These are the steps I followed in this project:  
![diagram](img/capstone-diagram.png)

### Project Main Steps
The project steps are explained in the following sections.

## The Dataset
In this project, the [Heart Failure Prediction](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) dataset from Kaggle is used. The description of the dataset is provided below.  

Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worlwide. Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure.
Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies. People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

**The dataset has the following features:**  

* age: Age (numeric)  
* anaemia: Decrease of red blood cells or hemoglobin (boolean)  
* creatinine_phosphokinase: Level of the CPK enzyme in the blood (mcg/L)  
* diabetes: If the patient has diabetes (boolean)  
* ejection_fraction: Percentage of blood leaving the heart at each contraction (percentage)  
* high_blood_pressure: If the patient has hypertension (boolean)  
* platelets: Platelets in the blood (kiloplatelets/mL)  
* serum_creatinine: Level of serum creatinine in the blood (mg/dL)  
* serum_sodium: Level of serum sodium in the blood (mEq/L)  
* sex: Woman or man (binary)  

**The task:**
Developing a ML model to predict death events using 12 clinical features.  

## Automated ML
tbd  

## HyperDrive 
tbd  

## Result Comparison  
tbd  

## Model Deployment
tbd  

## Testing the Model and Endpoint
tbd  

## Screen Recording
Every step in the project is reflected to the fast-track video with an Audio as given below:  
[Youtube Link](https://www.youtube.com/TBD)

## Future Improvement Suggestions
* The data was imbalanced and this leads a biased model that yields biased predictions. The imbalance issue would be handled as one or more of the following techniques  
1.) Upsampling Minority Class  
2.) Downsampling Majority Class  
3.) Generate Synthetic Data  
4.) Combine Oversampling and Undersampling Techniques  
5.) Balanced Class Weight  

* For better metrics, the deep learning would be enabled in AutoML experimentation, however, this will increase the computation time.
