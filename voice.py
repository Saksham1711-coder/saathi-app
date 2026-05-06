import speech_recognition as sr
import pyttsx3
import requests

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        return ""

print("Say 'sathi' to activate")

while True:
    text = listen()

    if "sathi" in text:
        speak("Yes, I am listening")

        command = listen()

        if command:
            res = requests.post(
                "http://127.0.0.1:5000/predict",
                json={"text": command}
            )

            speak(res.json()["result"])