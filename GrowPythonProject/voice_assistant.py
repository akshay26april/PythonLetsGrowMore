import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
from gtts import gTTS
import os

# Function to convert text to speech
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    os.system("start temp.mp3")


# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-US")
            print(f"User: {query}")
            return query.lower()

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""

# Function to perform actions based on user commands
def perform_action(command):
    if "open Google" in command:
        webbrowser.open("https://www.google.com/")

    elif "open YouTube" in command:
        webbrowser.open("https://www.youtube.com/")

    elif "play music" in command:
        music_dir = "C:\\Path\\To\\Your\\Music\\Directory"
        songs = os.listdir(music_dir)
        random_song = os.path.join(music_dir, random.choice(songs))
        os.startfile(random_song)

    elif "what's the time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm sorry, I don't understand that command.")

# Main function for voice assistant
def main():
    speak("Hello! How can I assist you today?")

    while True:
        command = recognize_speech()

        if command:
            perform_action(command)

if __name__ == "__main__":
    main()
