import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# load dataset
df = pd.read_csv("heart.csv")

X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "heart_model.pkl")

print("✅ Model trained!")