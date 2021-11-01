# HeartDiseaseDetector Project
## Problem Statement
Medical services need to be advanced so that better decisions for patient diagnosis and treatment options can be made.Instead of diagnosis, when a disease prediction is implemented using certain machine learning predictive algorithms then healthcare can be made smart. Some cases can occur when early diagnosis of a disease is not within reach. Hence disease prediction can be effectively implemented. Thus Machine learning in healthcare aids the humans to process huge and complex medical datasets and then analyze them into clinical insights. This then can further be used by physicians in providing medical care. This project focus on the development of a system which would able to provide prediction of Heart Disease based on early symptoms and medical history of the inidividual.

## Approach
* **`Data Exploration`**    : Exploration of Dataset using numpy and pandas librarie.
* **`Data Visualizaation`** : Data Visualization or plotting the data of the various features of the data to get the various insights. Tools used were matplotlib , Seaborn.
* **`Data Preprocessing`**  : Some of the datatypes of some features aren't quite right. I chnaged them into the correct datatypes. Finally encoding of the categorical datas and scaling of the continous datas were done so that the model fit properly.
* **`Model Building`**      : Different models were trained based on default parameters and evaluated with the help of evalutaion metrics. After that I perform hyperparameter tuning of all the models with the help of GridSearch CV. This lets me to find the optimal values for all the models to use instead of just using the default parameters or just randomly using some values. Finally I evaluate all the models using evaluation metrics.
*  **`Plotting ROC curve`** : I plot the True Positive Rate(TPR) and the False Positive Rate(FPR) of all the models. This graph shows the performance of all the classification model at all classification thresholds. This help us to select the best model and finally created the pickle file and saved it.
*  **`Web application`**    : I will expose the created model as a web API to be consumed by the client/client APIs. The tools used were Flask, HTML, CSS and  bootstrap.
*  **`Cloud Deployemnt`**   : I deployed the web app on Heroku.

## Project Interface

Link: https://heartdiseaseprediction1.herokuapp.com/predict
