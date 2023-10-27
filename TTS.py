from gtts import gTTS
import os

# Ask for user inputs
tts = input("Enter string to generate text to speech:")
filename = input("Enter desired name for this file:")

# Create a gTTS object
tts = gTTS(tts, lang='en')

# Save the generated audio to a WAV file
tts.save(f"{filename}.wav")

