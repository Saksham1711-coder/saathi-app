import speech_recognition as sr
import pyttsx3
import requests

engine = pyttsx3.init()
engine.setProperty("voice", "english")

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text
    except:
        return ""

while True:
    text = listen()

    if text:
        res = requests.post(
            "http://127.0.0.1:5000/predict",
            json={"text": text}
        )

        data = res.json()
        speak(data["result"])