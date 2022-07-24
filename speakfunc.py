import pyttsx3


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voice')
#print(voice)
engine.setProperty('voice',voice)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

