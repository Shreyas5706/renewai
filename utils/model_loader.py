import joblib

def load_model(path):
    try:
        return joblib.load(path)
    except:
        return None
