import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return listen()
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the internet. Please try again later.")
        return None

# Function to perform actions based on user's commands
def perform_action(command):
    command = command.lower()

    if 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'search' in command:
        speak("What would you like me to search for?")
        search_query = listen()
        if search_query:
            try:
                result = wikipedia.summary(search_query, sentences=2)
                speak(f"According to Wikipedia, {result}")
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple matches. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I couldn't find any relevant information.")
    elif 'exit' in command or 'bye' in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I don't understand that command. Can you please repeat?")

# Main loop
if __name__ == "__main__":
    speak("Initializing Voice Assistant. Hello there!")
    
    while True:
        user_command = listen()
        if user_command:
            perform_action(user_command)
