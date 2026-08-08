# AI Voice Assistant

## Description

This project is an AI Voice Assistant built using Python.

The assistant allows the user to speak through a microphone, converts the speech into text, sends the text to the Cohere Large Language Model (LLM) to generate a response, and then converts the response into speech and plays it automatically.

## Features

* Voice input through the microphone
* Speech-to-Text conversion
* AI response generation using Cohere
* Text-to-Speech conversion
* Automatic playback of the AI response
* Supports English voice input and output

## Technologies Used

* Python
* SpeechRecognition
* Google Speech Recognition
* Cohere API
* Edge-TTS
* PyAudio
* Playsound

## Project Structure

```text
AI-Voice-Assistant/
│
├── main.py
├── speech_to_text.py
├── text_to_speech.py
├── requirements.txt
├── .gitignore
├── README.md
└── Video Project.mp4
```

## Installation

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

## API Key

This project uses the Cohere API to generate AI responses.

For security reasons, the API key should not be uploaded to GitHub.

## How to Run

Open the project folder in the terminal and run:

```bash
python main.py
```

Then speak into the microphone when the program asks you to.

## How It Works

### 1. Speech-to-Text

The user speaks through the microphone.

The SpeechRecognition library receives the audio and converts the speech into text.

### 2. LLM Processing

The converted text is sent to the Cohere Large Language Model.

Cohere processes the user's question and generates an AI response.

### 3. Text-to-Speech

The generated response is converted into an audio file using Edge-TTS.

The audio is then played automatically using Playsound.

## 🔗 Complete Process

```text
🎤 Voice Input
      ↓
📝 Speech-to-Text
      ↓
🤖 Cohere LLM
      ↓
📝 AI Response
      ↓
🔊 Text-to-Speech
      ↓
▶️ Automatic Audio Playback
```




## 🎥 Demo Video

▶️ [Watch the Demo Video](https://github.com/JoudFiasalAlamoudi/AI-Voice-Assistant/blob/main/Video%20Project.mp4)

📁 Video Project.mp4

The demonstration shows:

* Speaking through the microphone
* Converting speech into text
* Generating a response using Cohere
* Converting the response into speech
* Playing the generated voice automatically

## Example

**User:**

> What is robotics engineering?

**AI Assistant:**

The assistant processes the question using Cohere, generates a response about robotics engineering, and converts the response into speech.

## Task Requirements

This project fulfills the required three steps:

1. Convert audio input to text.
2. Generate a response using an LLM (Cohere).
3. Convert the response to audio.

All project files and documentation are included in this GitHub repository.

