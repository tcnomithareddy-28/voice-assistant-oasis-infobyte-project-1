# Voice Assistant Python
# Developed as part of a Python internship.

import io
import webbrowser
from datetime import datetime

import numpy as np
import pyttsx3
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

SAMPLE_RATE = 16_000
RECORD_SECONDS = 6

engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text: str) -> None:
    """Convert text into spoken output."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen() -> str:
    """Record microphone audio and convert it to text."""
    try:
        print("Listening...")
        audio_data = sd.rec(
            int(RECORD_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32",
        )
        sd.wait()

        buffer = io.BytesIO()
        sf.write(buffer, np.squeeze(audio_data), SAMPLE_RATE, format="WAV")
        buffer.seek(0)

        with sr.AudioFile(buffer) as source:
            audio = recognizer.record(source)

        command = recognizer.recognize_google(audio).lower().strip()
        print(f"You: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
    except sr.RequestError:
        speak("Speech recognition service is unavailable right now.")
    except Exception as exc:
        print(f"Audio error: {exc}")
        speak("I could not access the microphone correctly.")
    return ""


def handle_command(command: str) -> bool:
    """Handle a recognized command. Return False when the assistant should exit."""
    if not command:
        return True

    if "time" in command:
        speak(datetime.now().strftime("The time is %I:%M %p"))
    elif "date" in command:
        speak(datetime.now().strftime("Today is %A, %B %d, %Y"))
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif command.startswith("search ") or "search for " in command:
        query = command.replace("search for ", "", 1).replace("search ", "", 1).strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
            speak(f"Searching for {query}.")
    elif any(greeting in command for greeting in ("hello", "hi", "hey")):
        speak("Hello! How can I help you?")
    elif "help" in command:
        speak("You can ask for the time, date, open Google or YouTube, search the web, or say exit.")
    elif any(word in command for word in ("exit", "quit", "stop", "goodbye")):
        speak("Goodbye!")
        return False
    else:
        speak("I do not know that command yet. Say help to see what I can do.")
    return True


def main() -> None:
    speak("Voice assistant started. Say help for available commands.")
    while True:
        if not handle_command(listen()):
            break


if __name__ == "__main__":
    main()
