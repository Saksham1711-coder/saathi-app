from flask import Flask, request, jsonify, render_template
import joblib
import requests

app = Flask(__name__)

API_KEY = "YOUR ML KEY"

model = joblib.load("heart_model.pkl")

def text_to_features(text):
    text = text.lower()

    age = 50            #I have used the values from the dataset to make the model work, you can change them to your own values
    sex = 1
    cp = 2
    trestbps = 130
    chol = 240
    fbs = 0
    restecg = 1
    thalach = 150
    exang = 0
    oldpeak = 1.0
    slope = 1
    ca = 0
    thal = 2

    if "chest pain" in text:
        cp = 3
    if "fatigue" in text:
        thalach = 120
    if "exercise pain" in text:
        exang = 1
    if "high bp" in text:
        trestbps = 150

    return [[age, sex, cp, trestbps, chol, fbs,
             restecg, thalach, exang, oldpeak,
             slope, ca, thal]]

def ask_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        result = res.json()

        if "choices" not in result:
            return "AI error: " + str(result)

        return result["choices"][0]["message"]["content"]
    except:
        return "Request failed"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.json.get("text", "")

    features = text_to_features(text)

    pred = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]

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