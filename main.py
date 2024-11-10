import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

def record_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Recording", "Recording... Please speak into the microphone.")
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data)
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand the audio")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results; check your network connection")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text_box.get(1.0, tk.END))
    messagebox.showinfo("Copied", "Text copied to clipboard")

# Set up the GUI
root = tk.Tk()
root.title("Voice to Text")

record_button = tk.Button(root, text="Record", command=record_and_transcribe)
record_button.pack(pady=10)

text_box = tk.Text(root, wrap='word', height=10, width=50)
text_box.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()
