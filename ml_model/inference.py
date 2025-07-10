import joblib
from ml_model.preprocessing import prepare_features

model = joblib.load("ml_model/model.pkl")

def run_prediction(df):
    X = prepare_features(df)
    preds = model.predict(X)
    return preds
