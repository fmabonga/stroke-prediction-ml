import pickle
from flask import Flask
from flask import request
from flask import jsonify
import xgboost as xgb

with open('stroke-prediction-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('predict')

@app.route('/predict', methods=['POST'])
def predict():

    patient = request.get_json()

    if patient is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    X = dv.transform([patient])

    dmatrix = xgb.DMatrix(X, feature_names=list(dv.get_feature_names_out()))

    pred = model.predict(dmatrix)[0]

    stroke_prediction = (pred >= 0.5)
    print("pred: %f" % (pred))
    return jsonify({
        "stroke_prediction": str(stroke_prediction)
    })