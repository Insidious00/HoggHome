import speech_recognition as sr
import os

#for i in range(0,9999999999999):
#    r = sr.Recognizer()
#    with sr.Microphone() as source:
#        print("Say something!")
#        audio = r.listen(source,timeout=3,phrase_time_limit=3)
#    try:
#        print("Transcription: " + r.recognize_google(audio))
#        vAudio = r.recognize_google(audio)
#    except sr.UnknownValueError:
#        print("Audio is unintelligable")
#    except sr.RequestError as e:
#        print("cannot obtain results; [0]", format(e))
#
#    if vAudio.upper() == "OKAY HOMEWORK" or "OK HOMEWORK":
#        print(vAudio)
#        filepath = 'textfile.txt'
#        os.startfile("F:\Python\HoggHome.py")
#        valid = True
#        break
#    break


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source,timeout=3,phrase_time_limit=5)
    
    try:
        print("Transcription: " + r.recognize_google(audio))
        vAudio = r.recognize_google(audio)
        if vAudio.upper() == "OKAY HOMEWORK" or "OK HOMEWORK":
            os.startfile("F:\Python\HoggHome.py")
        else:
            v1=1
        
    except sr.UnknownValueError:
            print("Audio is unintelligable")
            
    except sr.RequestError as e:
        print("cannot obtain results; [0]", format(e))
    
