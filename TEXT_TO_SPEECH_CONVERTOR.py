from gtts import gTTS
import os
from tkinter import *
root = Tk()
canvas=Canvas(root,width=400, height=300)
canvas.pack()

def texttospeech():
    text=entry.get()
    language='en'
    text_to_audio=gTTS(text=text,lang=language,slow=False)
    text_to_audio.save('text_to_audio.mp3')
    os.system("start text_to_audio.mp3")


entry=Entry(root)
canvas.create_window(200,180,window=entry)

button= Button(text="Start",command=texttospeech)
canvas.create_window(200,230,window=button)
root.mainloop()
