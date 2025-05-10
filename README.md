# noise-robust
This is a simple Python-based speech recognition program that uses the speech_recognition library to capture audio through a microphone, convert it to text using Google's Speech Recognition API, and optionally save the transcript to a file.

📌 Features
Real-time speech-to-text conversion using a microphone

Background noise adjustment for more accurate recognition

Option to save transcribed text to a file (transcript.txt)

Simple text-based interface with the ability to continue or exit

Handles common errors like unclear speech or API issues

🛠️ Requirements
Before running the program, make sure you have the following installed:

bash
Copy
Edit
pip install SpeechRecognition
pip install PyAudio
Note: On some systems, installing PyAudio may require additional setup:

Windows: Use pip install pipwin && pipwin install pyaudio

Linux: sudo apt-get install portaudio19-dev python3-pyaudio

macOS: brew install portaudio then pip install pyaudio

🚀 How to Run
Clone or download this repository.

Open a terminal in the project directory.

Run the script:

bash
Copy
Edit
python speech_recognition_program.py
Follow the on-screen instructions:

Speak clearly into your microphone.

Choose whether to save the transcript.

Decide if you'd like to continue or exit.

📂 Output
If you choose to save your speech transcript, it will be appended to a file called:

Copy
Edit
transcript.txt
Each speech entry will be saved on a new line.
