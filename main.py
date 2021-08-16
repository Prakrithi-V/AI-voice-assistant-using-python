import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser
import os
import pyautogui
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
newVoiceRate = 198
engine.setProperty("rate", newVoiceRate)
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    speak("Current time is")
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back sir/madam!")
    hour = (datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    else:
        speak("Good night")
    speak("Praku, at your service,How can I help you?")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en=in')
        print("query")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query
def sendmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com" , 587)
    server.ehlo()
    server.starttls()
    server.login("email" ,"password" )
    server.sendmail("sender's email @gmail.com" , to , content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    img.save("E:/self learning/python/ss.png")



if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=5)
            speak(result)
        elif "send email" in query:
            try:
                speak("What is the content of the email?")
                content=takecommand()
                to="prakrithiholla123@gmail.com"
                sendmail(to,content)
                speak("The mail was sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to send email")
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takecommand().lower()
            webbrowser.get(chromepath).open_new_tab(search +".com")
        elif "logout" in query:
            os.system("shutdown-l")
        elif "play song" in query:
            songs_dir="C:/Users/Prakrithi V/Music/music"    #Change it according to your system
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif "remember that" in query:
            speak("What should I remember?")
            data=takecommand()
            remember=open("data.txt" , "w")             #Change it according to your system
            remember.write(data)
            remember.close()
        elif "what did i ask u to remember" in query :
            remember=open("data.txt", "r")
            speak("You told me to remember that " + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("screenshot taken")


