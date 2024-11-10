import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import numpy as np
import tempfile
import os

# Function to record audio
def record_audio(filename, duration=10, rate=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * rate), samplerate=rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    write(filename, rate, audio_data)  # Save as WAV file
    print("Finished recording.")

# Function to transcribe audio with handling for pauses
def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)
        try:
            # Use recognize_google to transcribe the audio
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio"
        except sr.RequestError:
            return "Could not request results; check your network connection"

# Main function
def main():
    audio_filename = "recorded_audio.wav"
    record_audio(audio_filename, duration=10)  # Record for 10 seconds
    transcription = transcribe_audio(audio_filename)
    print("Transcription:")
    print(transcription)

if __name__ == "__main__":
    main()
