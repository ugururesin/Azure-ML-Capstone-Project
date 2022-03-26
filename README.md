# Capstone Project - Machine Learning Engineer with Microsoft Azure

## Table of Content
* [Overview](#overview)
* [The Architecture](#the-architecture)
* [Project Main Steps](#key-steps)
    * [1. Authentication](#authentication)
    * [2. Automated ML Experiment](#automated-ml-experiment)
    * [3. Deploy the best model](#deploy-the-best-model)
    * [4. Enable logging](#enable-logging)
    * [5. Swagger Documentation](#swagger-documentation)
    * [6. Consume model endpoints](#consume-model-endpoints)
    * [7. Create and publish a pipeline](#create-and-publish-a-pipeline)
    * [8. Documentation](#documentation)
* [Screen Recording](#Screen-Recording-with-Subtitles)
* [Future Improvement Suggestions](#future-improvement-suggestions)

## Overview
This project is part of the Udacity Azure ML Nanodegree.
In this project, I will use both automated ML and HyperDrive to create two models to solve a task. I will then compare the performance of both these models and deploy the best-performing model. To complete this project, I will be using both the HyperDrive and Auto ML API from Azure ML. I first I determined the data I want. The data I choose needs to be external and not available in the Azure ecosystem. Thus I validate it using this link [Azure Datasets Catalog](https://docs.microsoft.com/en-us/azure/open-datasets/dataset-catalog).

After I have chosen a dataset, I have to import the dataset into my workspace. Next, I will train a model on that dataset using automated ML and then train a custom model whose hyperparameters are tuned using HyperDrive. After I have trained the models, I have to compare their performance, deploy the best model as a web service, and then test the model endpoint. After I have tested the model endpoint, I will have to complete a README file that describes the project and my results.

All steps are summarized as below:  
1. **Authentication** : In this step, we need to create a Security Principal (SP) to interact with the Azure Workspace. (Since I do not have permission to crate a SP in Udacity Lab, this step is skipped)
2. **Automated ML Experiment** : In this step, we create an experiment using Automated ML, configure a compute cluster, and use that cluster to run the experiment.
3. **Deploy the best model** : Deploying the Best Model will allow us to interact with the HTTP API service and interact with the model by sending data over POST requests.
4. **Enable logging** : Logging helps monitor our deployed model. It helps us know the number of requests it gets, the time each request takes, etc.
5. **Swagger Documentation** : In this step, we consume the deployed model using Swagger.
6. **Consume model endpoints** : We interact with the endpoint using some test data to get inference.
7. **Create and publish a pipeline** : In this step, we automate this workflow by creating a pipeline with the Python SDK.


## The Architecture
These are the steps we followed in this project :

![diagram](img/architecture.png)

### Key Steps

## Authentication
The Azure lab is used provided by Udacity. Hence, the Authentication step is skipped since I am not authorized to create a security principal.

## Automated ML Experiment
**Figure-01: The bank-marketing dataset is loaded from a local source**  
![fig](img/fig01.png)  
**Figure-02: The dataset is named**  
![fig](img/fig02.png)  
**Figure-03: The columns and rows are checked**  
![fig](img/fig03.png)  
**Figure-04: The data types are checked**  
![fig](img/fig04.png)  
**Figure-05: Dataset seems OK**  
![fig](img/fig05.png)  
**Figure-06: A compute cluster is created (DS3_V2 is preferred)**  
![fig](img/fig06.png)
**Figure-07: The compute cluster is created (Details are given in the video)**  
![fig](img/fig07.png)  
**Figure-08: Using the dataset and the cluster, an AutoML experiment is setup**  
![fig](img/fig08.png)  
**Figure-09: The task is selected as classification since the target label is a categorical variable ('yes', 'no')**  
![fig](img/fig09.png)  
**Figure-10: The metric is set AUC to handle the imbalance dataset and Training hour is limited with 1 hour**  
![fig](img/fig10.png)  
**Figure-11: The AutoML is started train different ML models to find out the best fitting algorithm**  
![fig](img/fig11.png)  
The AutoML completed its run less than an hour
**Figure-12: The AutoML completed its run less than an hour**  
![fig](img/fig12.png)  
**Figure-13: The best model metrics are 0.917 accuracy, 0.948 AUC_macro, 0.981 AUC_micro, 0.948 AUC_weighted**  
![fig](img/fig13.png)  
The precision-recall graph is shown below  
**Figure-14: The precision-recall graph is shown below**  
![fig](img/fig14.png)  
The ROC curve is shown below  
**Figure-15: The ROC curve is shown below**  
![fig](img/fig15.png)  


## Deploy the best model
To be able to interact with the best ML model, it needs to be deployed. Deployment can be done in the Azure Machine Learning Studio, which provides us with an URL to send our test data to. The steps are given below.

**Figure-16: The best model is deployed using a web-service to comsume. Here, Deploy function is used in Azure ML studio and the compute type is selected as ACI (Azure Container Instance)**  
![fig](img/fig16.png)  

### Enable logging
See the figure 17-18-19 below with their explanations:  

**Figure-17: Then the applications insights are enabled using 'service.update(enable_app_insights=True' (line14)**  
![fig](img/fig17.png)  
The model deployment is done succesfully  
**Figure-18: The model deployment is done succesfully**  
![fig](img/fig18.png)
**Figure-19: Then the logs.py is run in order to enable to application insights**  
![fig](img/fig19.png) 

## Swagger Documentation
To consume the best AutoML model using Swagger, first the swagger.json file is downloaded (see Figure.20) from the Endpoints section in Azure Machine Learning Studio.

**Figure-20: In the endpoints section, the swagger.json file is downloaded and imported to the working directory**  
![fig](img/fig20.png)

Putting the swagger.json file in the active directory the swagger.sh and serve.py files are triggered in order to interact with the swagger instance running with the documentation for the HTTP API of the model.

**Figure-21: Using Git Bash, the swagger.sh and the serve.py files are triggered respectively. The serve.py is not changed but the local host is changed in the swagger.sh to prevent overlap**
![fig](img/fig21.png) 
**Figure-22: Then the deployed model is accessed via swagger using localhost:8000/swagger.json adress**  
![fig](img/fig22.png)  
**Figure-23: The input for the score POST method that returns the prediction of the deployed ML model.**  
![fig](img/fig23.png)  

## Consume model endpoints
At this point, the interaction with model is tested by sending a test data (see the left screen in the figure 25).

To do that, the script is modified (default script has an issue) by getting the consumption script (see Figure 24).  

**Figure-24: The consumption options provided by Azure ML Studio (here Python is used)**  
![fig](img/fig24.png)  

**endpoint.py script runs against the API producing JSON output from the model.**  
The default script did not work, I changed it based on AzureML code snipsets.  
**Figure-25**  
![fig](img/fig25.png)  

## Create and publish a pipeline
As a second part of this project, the aml-pipelines-with-automated-machine-learning-step Jupyter Notebook is used to create a Pipeline.  
Then, it's consumed and published the best model for the bank marketing dataset using AutoML with Python SDK.  
**Figure-26: Create a Pipeline in the SDK**  
![fig](img/fig26.png)  

**Note: There was a environment issue to save the best model, end no time left in the virtual environment to replicate the environment again but met the rubric requirements**

The pipeline runs and the endpoint is created successfully  
**Figure-27: Create a Pipeline in the SDK**  
![fig](img/fig27.png)  
**Figure-28: Pipeline in Azure Studio**  
![fig](img/fig28.png)  

**Figure-29: Create the REST endpoint with a stautus of ACTIVE.**  
![fig](img/fig29.png) 
**Figure-30: The REST endpoint is achieved in Azure ML Studio, with a status of ACTIVE.**  
![fig](img/fig30.png) 


## Screen Recording with Subtitles
Every step in the project is reflected to the fast-track video with an Audio as given below:  
[Youtube Link](https://www.youtube.com/watch?v=LqhBfw5kl9M)

## Future Improvement Suggestions
* The data was imbalanced and this leads a biased model that yields biased predictions. The imbalance issue would be handled as one or more of the following techniques  
1.) Upsampling Minority Class  
2.) Downsampling Majority Class  
3.) Generate Synthetic Data  
4.) Combine Oversampling and Undersampling Techniques  
5.) Balanced Class Weight  

* For better metrics, the deep learning would be enabled in AutoML experimentation, however, this will increase the computation time.
