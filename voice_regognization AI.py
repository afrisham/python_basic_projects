import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime

# =========================
# VOICE ENGINE SETUP
# =========================

engine = pyttsx3.init()

engine.setProperty('rate', 170)   # speed
engine.setProperty('volume', 1)

voices = engine.getProperty('voices')

# Female voice
engine.setProperty('voice', voices[1].id)


# =========================
# SPEAK FUNCTION
# =========================

def speak(text):

    print("AI:", text)

    engine.stop()

    engine.say(text)

    engine.runAndWait()


# =========================
# LISTEN FUNCTION
# =========================

def take_command():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source)

        recognizer.pause_threshold = 1

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            print("Recognizing...")

            command = recognizer.recognize_google(audio)

            print("You:", command)

            return command.lower()

        except sr.UnknownValueError:

            speak("Sorry, I did not understand.")

            return ""

        except sr.RequestError:

            speak("Internet connection problem.")

            return ""

        except Exception as e:

            print("Error:", e)

            return ""


# =========================
# START MESSAGE
# =========================

speak("Hello! I am your AI assistant. How can I help you today?")


# =========================
# MAIN LOOP
# =========================

while True:

    command = take_command()

    if command == "":
        continue

    # =====================
    # GREETINGS
    # =====================

    elif 'hello' in command:

        speak("Hello! Nice to meet you.")

    elif 'how are you' in command:

        speak("I am fine. Thank you for asking.")

    elif 'your name' in command:

        speak("My name is Mona, your AI assistant.")

    # =====================
    # TIME
    # =====================

    elif 'time' in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")

    # =====================
    # OPEN APPS
    # =====================

    elif 'open edge' in command:

        speak("Opening Microsoft Edge")

        os.system("start msedge")

    elif 'open calculator' in command:

        speak("Opening Calculator")

        os.system("start calc")

    elif 'open notepad' in command:

        speak("Opening Notepad")

        os.system("start notepad")
    elif "open power bi "in command:

        speak("Opening Power BI")

        os.system("start powerbi")
    elif 'open vs code' in command:

        speak("Opening Visual Studio Code")

        os.system("code")



    elif 'open google' in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    elif 'open youtube' in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    

    elif 'exit' in command or 'goodbye' in command:

        speak("Okay goodbye. Have a nice day!")

        break

    

    else:

        speak("Sorry, I don't know that command yet.")



