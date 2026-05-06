# ❤️ Saathi — AI Heart Health Assistant

Saathi is a simple AI-based project that helps users understand possible heart-related risks based on symptoms.

It supports both voice and text input, predicts risk using a machine learning model, and explains the result in an easy way.

---

## ✨ What it does

- Takes symptoms (voice or text)
- Converts them into basic medical features
- Uses a trained ML model to predict heart disease risk
- Explains the result in simple language using AI

---

## 🧠 How it works

1. User enters symptoms (or speaks them)
2. Text is converted into structured features
3. A Random Forest model predicts risk
4. AI generates a clear explanation + precautions

---

## 🧠 How prediction works (simple)

The model uses inputs like:
- age
- chest pain type
- blood pressure
- cholesterol
- heart rate

These values are estimated from user symptoms.

Output:
- 0 → low risk  
- 1 → high risk  

This is converted into a probability percentage.

---

## 🧠 Tech used

- Python
- Flask
- Scikit-learn (Random Forest)
- OpenRouter API
- SpeechRecognition + pyttsx3

---

## 📊 Dataset

UCI Heart Disease Dataset

---

## 📁 Project Structure

saathi-app/

├── app.py              # Flask backend  
├── voice.py            # Voice assistant  
├── train_model.py      # Model training  
├── heart_model.pkl     # Trained model  
├── templates/  
│   └── index.html      # Web UI  
├── requirements.txt  

---

## ⚙️ Setup (step-by-step)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/saathi-app.git
cd saathi-app

Train the model
python3 train_model.py

This will generate:

heart_model.pkl
