from flask import Flask, request, jsonify, render_template
import requests
import joblib

app = Flask(__name__)

# 🔑 PUT YOUR API KEY HERE
API_KEY = "YOUR_OPENROUTER_KEY"

# load ML model
model = joblib.load("heart_model.pkl")

# ================= AI CALL =================
def ask_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        result = res.json()
        return result["choices"][0]["message"]["content"]
    except:
        return "AI error"

# ========== TEXT → FEATURES ==========
def extract_features(text):
    prompt = f"""
Convert this into heart disease dataset values.

Text: {text}

Return ONLY numbers separated by commas in this order:
age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal

Example:
52,1,2,130,250,0,1,170,0,1.2,2,0,2
"""

    response = ask_ai(prompt)

    try:
        values = list(map(float, response.split(",")))
        return values
    except:
        return None

# ========== ML PREDICTION ==========
def predict_heart(features):
    pred = model.predict([features])[0]
    prob = model.predict_proba([features])[0][1]
    return pred, prob

# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.json.get("text", "")

    features = extract_features(text)

    if not features:
        return jsonify({"result": "Could not understand symptoms"})

    pred, prob = predict_heart(features)

    explanation = ask_ai(f"""
User symptoms: {text}
Heart disease risk: {prob*100:.2f}%

Explain clearly and give precautions.
""")

    return jsonify({
        "result": explanation,
        "risk": f"{prob*100:.2f}%"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)