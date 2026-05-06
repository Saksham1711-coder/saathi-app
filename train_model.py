import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("heart_disease_uci.csv")

df = df.drop(["id", "dataset"], axis=1)
df["num"] = df["num"].apply(lambda x: 1 if x > 0 else 0)

df = df.fillna(df.mode().iloc[0])

df["sex"] = df["sex"].map({"Male": 1, "Female": 0})
df["cp"] = df["cp"].astype("category").cat.codes
df["restecg"] = df["restecg"].astype("category").cat.codes
df["slope"] = df["slope"].astype("category").cat.codes
df["thal"] = df["thal"].astype("category").cat.codes

df["exang"] = df["exang"].astype(int)
df["fbs"] = df["fbs"].astype(int)

X = df.drop("num", axis=1)
y = df["num"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "heart_model.pkl")

print("✅ Model trained!")