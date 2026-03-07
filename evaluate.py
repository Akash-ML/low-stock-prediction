from train import X_test, y_test

import joblib
from sklearn.metrics import classification_report

model = joblib.load("model.pkl")

y_pred = model.predict(X_test)
report = classification_report(y_pred, y_test)
print(report)
