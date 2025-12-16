
from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.01)

def train(history):
    model.fit(np.array(history))

def is_anomaly(features):
    X = np.array(features).reshape(1, -1)
    return model.predict(X)[0] == -1
