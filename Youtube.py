
import webbrowser
import speech_recognition as sr

r = sr.Recognizer()
print("Speak now...")
with sr.Microphone() as source:
    audio = r.listen(source)
    command = r.recognize_google(audio).lower()
    print(f"You said: {command}")
    if "open youtube" in command:
        webbrowser.open("https://youtube.com")








