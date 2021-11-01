from joblib import load
from flask import Flask, render_template, request
from DataPreprocessing import preprocess_data
import numpy as np
# from flask_cors import CORS, cross_origin


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        r = request.form.to_dict()
        preprocessed_data = preprocess_data(r)
        model_name = "KNNmodel.pkl"
        model = load(model_name)
        prediction = ('Heart Disease' if model.predict(preprocessed_data)[0] == 1 else 'No Heart Disease')

        return render_template('result.html', out=prediction)
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)

