from gtts import gTTS
import os
f=open('TextToSpeech.txt')
x=f.read()
language='en'
audio=gTTS(text=x,lang=language,slow=False)
audio.save("TextToSpeech.wav")
os.system("TextToSpeech.wav")
