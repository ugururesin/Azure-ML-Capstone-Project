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
    * [7. Application Insights](#application-insights)
    * [8. Proof of Allocated Resource Removal](#proof-of-allocated-resource-removal)
    * [9. Documentation](#table-of-content)
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
The AutoML is used to generate different ML models to pick the best one, deploy and consume.  
I choose the followimng AutoML settings.  

* **experiment_timeout_minutes:** 15 minutes is set since the dataset is small.  

* **iterations:** 50 is set since the dataset is small.  

* **max_concurrent_iterations:** Represents the maximum number of iterations that would be executed in parallel.  

* **n_cross_validations:** To avoid overfitting and ensure randomness.  

* **primary_metric:** Accuracy is selected to be able to compare with HyperDrive's results.  

* **task:** Classification is selected since the response variable is binary (0 or 1).  

* **enable_early_stopping:** Activated to avoid overfitting.  

'''
automl_settings = {
    "experiment_timeout_minutes": 15,
    "iterations": 50,
    "max_concurrent_iterations": 3,
    "n_cross_validations": 3,
    "primary_metric" : 'accuracy',
    "featurization" : 'auto',
    "verbosity": logging.INFO
}
'''

'''
automl_config = AutoMLConfig(
    task = "classification", 
    training_data = train_data,
    label_column_name="DEATH_EVENT",
    enable_early_stopping= True,
    debug_log = "automl_errors.log",
    compute_target = compute_target,
    **automl_settings
)
'''

This configuration is yielded the following models:  
![aml_runs1](/img/03_aml_runs1.png)

![aml_runs1](/img/04_aml_runs2.png)

#### AML Results
The best model is a 'VotingEnsemble' whose details is given in the following figures including it's metrics.  

![aml_best_detail](/img/05_bestmodel_details_aml.png)
![aml_best_graph](/img/06_bestmodel_metric_graph_aml.png)
![aml_best_metrics](/img/07_metrics_aml.png)


## HyperDrive 
In addition to the AutoML, the Hyperdrive is also used to generate a ML model for the health-failure dataset.  
In this step, scikit-learn library is used to fit a **logistic-regression** model which can be considered as a fundamental classification algorithm especially for binary classification problems for small datasets. Therefore, it's logical to choose this model before training more complex models to get an insight about the metrics and the best fit.  

I used 2 hyperparameters in the hyper-drive as shown in the figure below:  
![hdr_config](/img/08_hdr_config.png)

**C: The regularization strength.** Regularization generally refers the concept that there should be a complexity penalty for more extreme parameters. The idea is that just looking at the training data and not paying attention to how extreme one's parameters are leads to overfitting. A high value of C tells the model to give high weight to the training data, and a lower weight to the complexity penalty. A low value tells the model to give more weight to this complexity penalty at the expense of fitting to the training data. Basically, a high C means "Trust this training data a lot", while a low value says "This data may not be fully representative of the real world data, so if it's telling you to make a parameter really large, don't listen to it".

**Reference:** https://stackoverflow.com/questions/67513075/what-is-c-parameter-in-sklearn-logistic-regression

**max_iter:** The number of iterations. There is a trade-off between the max_iter and training time. Thus, I selected the max_iter intuitively.

#### HyperDrive Results
As you can see the graph below, the best accuracy for the hyperdrive experiments is around 77% and it's way lower than the model created by the AML.

![hdr_metrics](/img/09_metrics_hdr.png)  

The details of the LR model is given below:
![hdr_details](/img/10_bestmodel_details_hdr.png)  

## Result Comparison  
-|AutoML| HyperDrive
--- | --- | ---  
Best Model | VotingEnsemble | Logistic-Regression
Accuracy | 0.962 | 0.777


## Model Deployment
Since the HyperDrive yielded a model with a low accuracy, only the AutoML model is deployed.  
This could be seen in the following screenshot:  

![end_aci](/img/12_endpoint_aci.png)  


## Testing the Model and Endpoint
To test the deployment and consume the endpoint a data is generated as follows (in the endpoint.py file):  
![hdr_details](/img/13_sample_data_to_test.png)  

The REST endpoint and the primary key is generated in the Endpoint section and put in the endpoint.py file.  
Then, the endpoint is tested. This worked and yielded the following predictions:  
![consume_test](/img/14_consume_testresult.png)  

## Application Insights
![app_insights](/img/15_appins.png)  

## Proof of Allocated Resource Removal
![comp_deletion1](/img/17_deletion1.png)  
![comp_deletion2](/img/18_deletion2.png)  

## Screen Recording
Every step in the project is reflected to the fast-track video with an Audio as given below:  
[Youtube Link](https://www.youtube.com/watch?v=BfEJqNmfxJo)

## Future Improvement Suggestions
* The target feature was imbalanced (see the screenshot below) and this leads a biased model that yields biased predictions.  

![tf_imbalance](/img/tf_imbalance.png)

**The imbalance issue would be handled as one or more of the following techniques:**  
1.) Upsampling Minority Class  
2.) Downsampling Majority Class  
3.) Generate Synthetic Data  
4.) Combine Oversampling and Undersampling Techniques  
5.) Balanced Class Weight  

* For better metrics, the deep learning would be enabled in AutoML experimentation, however, this will increase the computation time.
