import tkinter as tk
from gtts import gTTS
from PIL import Image, ImageSequence, ImageTk

# Create the main application window
app = tk.Tk()
app.title("Text-to-Speech Converter")

# Function to convert text to speech and save it with the provided filename
def convert_to_speech():
    text = text_entry.get()
    filename = filename_entry.get()

    if text and filename:
        tts = gTTS(text, lang='en')
        filename = filename + ".mp3"  # Append the file extension if not provided

        tts.save(filename)
        message_label.config(text=f"Conversion complete. File saved as {filename}", fg='red')


# Create and configure widgets
text_label = tk.Label(app, text="Enter Text to Generate Speech Audio:")
text_entry = tk.Entry(app, width=40)

filename_label = tk.Label(app, text="Enter Filename (without extension):")
filename_entry = tk.Entry(app, width=40)
convert_button = tk.Button(app, text="Convert to Speech", command=convert_to_speech, bg ='brown', fg='white')

message_label = tk.Label(app, text="")
message_label.pack()  # Add the message label to the GUI

 ## GUI - Picture
logo = Image.open('gsd2.png')
logo = logo.resize((75, 75))  # resizing the photo since it was massive.
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.pack()

# Pack widgets
text_label.pack()
text_entry.pack()

filename_label.pack()
filename_entry.pack()

convert_button.pack()

# Start the tkinter main loop
app.mainloop()
