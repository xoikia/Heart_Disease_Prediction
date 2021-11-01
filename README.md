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
<p align='center'>Web Interface</p>
<p align="center">
  <img src="https://github.com/xoikia/Heart_Disease_Prediction/blob/main/ReadMe%20Images/Interface.png" alt="interface">
</p>
<p align='center'>Prediction Result</p>
<p align="center">
  <img src="https://github.com/xoikia/Heart_Disease_Prediction/blob/main/ReadMe%20Images/Result.png" alt="result">
</p>

## Libraries and Tools used
* `Python`
* `Numpy`
* `Pandas`
* `Matplotlib`
* `Seaborn`
* `Sklearn`
* `Flask`
* `HTML 5`
* `CSS 3`
* `Bootstrap`
* `Heroku`

## Repository Files
* [heart.csv](https://github.com/xoikia/Heart_Disease_Prediction/blob/main/heart.csv) : This is the dataset I have used to build the model.
* [Heart_Disease_Prediction](https://github.com/xoikia/Heart_Disease_Prediction/blob/main/Heart_Disease_Prediction.ipynb) : This jupyter notebook file is where the data analysis, data exploration, visualization and finally the model building is being done.
* [HeartDiseasePrediction](https://github.com/xoikia/Heart_Disease_Prediction/tree/main/HeartDieseasePrediction) : This folder contains all the html, css, python code and the model which is used to build the Flask web app.
* [ReadMe Images](https://github.com/xoikia/Heart_Disease_Prediction/tree/main/ReadMe%20Images) : Stores the images used in README file.

## Feedback
Hello reader if you find any bug please consider raising issue. I will try to fix it. If you like the project please give a :star:
