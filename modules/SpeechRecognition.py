import pyttsx3
import speech_recognition as sr
from FileManager import update_json_key

path_eva = 'files/eva.json'


def initialize_tts_engine(rate=140, volume=1.0, gender="default"):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Select voice based on gender preference
    if gender == 'female':
        engine.setProperty('voice', r'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
    if gender == 'male':
        engine.setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')

    return engine


def listen(recognizer, microphone, timeout=10, phrase_time_limit=5):
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    
    try:
        print("Recognizing...")
        update_json_key(path_eva, 'status', 'recognizing')
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio. Please speak clearly.")
    except sr.RequestError as e:
        print(f"Service unavailable: {e}")
    return None


def speak(engine, text):
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        print("No text provided to speak.")
