import speech_recognition as sr
import pyttsx3
import time
import datetime
r = sr.Recognizer()
word = pyttsx3.init()
with sr.Microphone(device_index=1) as source:
    print("say anything")
    audio = r.listen(source)
    
query = r.recognize_google(audio, language="uz-UZ")
print(query)
time.sleep(1)
if query:
    word.say(f"today {datetime.datetime.date}")
    word.runAndWait()