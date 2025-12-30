import pickle
import xgboost as xgb

with open('stroke-prediction-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

def predict(patient):
    result = model.predict(patient)[0]
    return float(result)

def lambda_handler(event, context):
    patient = event['patient']
    X = dv.transform([patient])
    dmatrix = xgb.DMatrix(X, feature_names=list(dv.get_feature_names_out()))

    prob = predict(dmatrix)

    return {
        "stroke_probability": prob,
        "stroke prediction": bool(prob >= 0.5)
    }