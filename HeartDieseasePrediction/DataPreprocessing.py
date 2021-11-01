import numpy as np
import pandas as pd
from joblib import load


def preprocess_data(user_data):
    data = pd.DataFrame(data=[user_data], columns=user_data.keys())
    data['age'] = data['age'].astype('int64')
    data['sex'] = data['sex'].astype('int64')
    data['cp'] = data['cp'].astype('int64')
    data['trestbps'] = data['trestbps'].astype('int64')
    data['chol'] = data['chol'].astype('int64')
    data['fbs'] = data['fbs'].astype('int64')
    data['restecg'] = data['restecg'].astype('int64')
    data['thalach'] = data['thalach'].astype('int64')
    data['exang'] = data['exang'].astype('int64')
    data['oldpeak'] = data['oldpeak'].astype('float64')
    data['slope'] = data['slope'].astype('int64')
    data['ca'] = data['ca'].astype('int64')
    data['thal'] = data['thal'].astype('int64')

    transformer = load('Transformer.pkl')
    transform_data = transformer.transform(data)

    return transform_data
