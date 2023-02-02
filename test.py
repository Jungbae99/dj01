from gtts import gTTS
text="hi, everybody"

tts=gTTS(text=text, lang='en')
tts.save('helloEN.mp3')