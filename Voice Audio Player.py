from playsound import playsound
import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()
engine = pyttsx3.init()
a = "repeat"
with sr.Microphone() as source :
        while (a=="repeat") :
                engine.say("Please say the song name so I can play that song for you")
                engine.runAndWait()
                engine.say("now say")
                print("Listening...")
                engine.runAndWait()
                audio = r.listen(source)
                choice = r.recognize_google(audio)
                print(f"You Said '{choice}'")
                playsound("c:\\users\\prithbiraj\\music\\downloaded songs\\"+choice+".mp3")
                engine.say("Do you want to listen more songs than please say repeat otherewise say stop")
                engine.runAndWait()                
                engine.say("now say")                
                print("Listening...")
                engine.runAndWait() 
                audio = r.listen(source)
                a = r.recognize_google(audio)
                

engine.say("All right")
engine.runAndWait()
print("See You Again My Friend :)")