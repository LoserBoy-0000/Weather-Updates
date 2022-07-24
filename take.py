import speech_recognition as sr
import speakfunc
def takecommand():
    # It takes microphone input from user to collect data and make it to a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        r.energy_threshold = 900
        audio = r.listen(source,0,4)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        speakfunc.say("Say that again please")
        return "none"
    return query
def query():
    q = takecommand().lower
    print (q)



