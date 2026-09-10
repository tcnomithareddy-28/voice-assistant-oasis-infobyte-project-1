# 🎙️ Voice Assistant Python

A beginner-friendly **Python voice assistant** that listens to spoken commands, converts speech to text, performs useful actions, and responds using text-to-speech.

## 🎯 Project Overview

This project demonstrates how Python can combine **speech recognition, audio processing, text-to-speech, and web automation** to build an interactive desktop voice assistant.

## ✨ Features

- 🎤 Capture voice commands through the microphone
- 📝 Convert speech to text using Google Speech Recognition
- 🔊 Respond with text-to-speech using `pyttsx3`
- 🕐 Tell the current time and date
- 🔎 Perform web searches
- ▶️ Open YouTube and Google
- 💬 Handle basic conversational commands
- ❌ Exit safely on command
- ⚠️ Handle common speech-recognition and service errors

## 🧠 How It Works

```text
User Voice
    ↓
Microphone Audio
    ↓
Speech Recognition
    ↓
Command Processing
    ↓
Action / Response
    ↓
Text-to-Speech
```

## 🛠️ Tech Stack

- **Python**
- **SpeechRecognition** — speech-to-text
- **pyttsx3** — text-to-speech
- **SoundDevice** — audio recording
- **SoundFile** — WAV audio handling
- **NumPy** — audio data processing

## 📚 Skills Demonstrated

- Python programming
- Speech recognition integration
- Audio recording and processing
- Text-to-speech systems
- API/service integration
- Exception handling
- User input and command processing

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/tcnomithareddy28-cloud/voice-assistant-python.git
cd voice-assistant-python
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install SpeechRecognition pyttsx3 sounddevice soundfile numpy
```

### 4. Run the assistant

```bash
python voice_assistant.py
```

> **Note:** A working microphone and internet connection are required for speech recognition and web-based features.

## 📂 Project Structure

```text
voice-assistant-python/
├── voice_assistant.py
└── README.md
```

## 🎓 Internship Project

This project was developed as part of a **Python internship**, with a focus on applying Python programming concepts to a practical voice-based application.

## 👩‍💻 Author

**Nomitha Reddy**

Python | AI & Machine Learning | Data Science
