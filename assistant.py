import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os 
import pyjokes
import winshell
from auto import *
engine pyttsx3.init('sapi5')
voices (engine getProperty('voices')
engine.setProperty(voice', voices [1].id)

def speak (audio):
    engine.say(audio)
    engine.runAndwait()

def wishMe():
    hour = int (datetime.datetime.now().hour)
    if hour > 0 and hour < 12: 
        speak ("Good Morning!")
    elif hour 12 and hour < 18: 
        speak ("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Sofia. Your personal Assistant Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr. Recognizer() 
    with sr. Microphone() as source:
        print("Listening...")
        r. pause_threshold = 1
        audio r.listen(source)
  
    try: 
        print("Recognizing...")
        query =  r.recognize_google(audio, language'en-in')
        print(f"User said: (query)\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    def clear(): return os.system('cls')
    clear() 
    wishMe()

    while True:
       #if 1:
       query takeCommand().lower()
       # Logic for executing tasks based on query
       if search in query and wikipedia in query: 
          speak('Searching wikipedia...) 
          query query. replace("on wikipedia", "")
          results wikipedia. rch, sentences
          webbrowser.open("https://en.wikipedia.org/wiki/" + search) 
          speak("According to wikipedia")
          print(results) 
          speak(results)

      elif'open youtube' in query: 
          webbrowser.open("youtube.com")
      elif 'open google' in query: 
          webbrowser.open("google.com")
      elif "wikipedia" in query: 
          webbrowser.open("wikipedia.com")
      elif 'play music' in query:
          music_dir r"//location
          songs os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs [0]))
      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S") 
          speak (f"sir, the time is {strTime}")
      elif 'open code' in query:
          codePath = r""//location 
          os.startfile (codePath)
      elif "where is" in query:
          query query.replace("where is", "")
          location query speak ("User asked to Locate") 
          speak (location) "https://www.google.com/maps/place/" + location + "")
          webbrowser.open(https://www.google.com/maps/place/" + location + "")
      elif 'open brave' in query:
          codePath = r""//location 
          os.startfile(codePath)
      elif 'open hello' in query:
          codePath = r""//location 
          os.startfile(codePath)
      elif ('work mode' or 'turbo mode' or 'pro mode') in query:
          codePath1 = r""//location
          codePath2r""//location
          codePath3r""//location
          codePath4r""//location
          os.startfile (codePath1)
          os.startfile (codePath2)
          os.startfile (codePath3)
          os.startfile (codePath4)
      elif 'joke' in query: 
          speak (pyjokes.get_joke())
      elif "sofia" in query: 
          speak ("How may ay I help you sir")
      elif empty recycle bin' in query:
          winshe 11. recycle bino empty(confirm False, show progress false, sound-True) 
          speak (Recycle Bin Recycled)
      elif 'play' in query and 'youtube' in qu query: 
          query.replace(on youtube, query query replace("play",**)
          assist = ytvideo()
          assist.play(query)
      elif 'google' in query:
          query = query.replace("on google", "")
          query = query.replace("search", "")
          quewebbrowser.open("https://www.google.com/search?q=" + query)
      elif 'exit' in query or stop listening' in query or 'stop' in query:
          speak (Thanks for giving me your time") 
          exit()

