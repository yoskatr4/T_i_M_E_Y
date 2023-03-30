import time
import sqlite3
import wikipedia
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import wolframalpha
import keyboard
import tkinter as tk
from tkinter import ttk

def işlemler():
    class Voice_Assistant():

        def __init__(self):
            super().__init__()
            self.i = 0
            self.first_date()

        def first_date(self):
            con = sqlite3.connect("user.db")
            cursor = con.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS USER(Name TEXT,Surname TEXT)")
            con.commit()

            cursor.execute("select * from USER")
            self.name = cursor.fetchall()
            if (len(self.name) == 0):
                self.speak(
                    "Hi. My name is Timey. I will always be here for you. What is your name sir?")
                self.response = sr.Recognizer()
                with sr.Microphone() as source:
                    print(" Listening... ")
                    audio = self.response.listen(source)
                try:
                    self.phrase = self.response.recognize_google(
                        audio, language="tr-TR")
                    self.phrase = self.phrase.lower()
                    print(self.phrase)
                except sr.UnknownValueError:
                    self.speak("Sorry, I did not get that.Please repeat")

                self.name_list = self.phrase.split(" ")

                cursor.execute("insert into USER VALUES(?,?)",
                            (self.name_list[0], self.name_list[1]))
                con.commit()

                cursor.execute("select * from USER")
                self.name = cursor.fetchall()
                self.greeting()
            else:
                self.greeting()

        def speak(self, say):
            self.engine = pyttsx3.init()
            self.engine.say(say)
            self.engine.runAndWait()

        def re_listen(self):
            self.response = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = self.response.listen(source)
            try:
                self.phrase = self.response.recognize_google(
                    audio, language="en-in")
                self.phrase = self.phrase.lower()
                print(self.phrase)
            except sr.UnknownValueError:
                self.speak("You don't say anything.")
                self.phrase = "repeat"
            return self.phrase

        def listen(self):
            self.speak("How can i help you?")
            while (1):
                self.response = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = self.response.listen(source)
                if self.i == 3:
                    self.speak(
                        "I close the program because you did not make any requests.")
                    time.sleep(1)
                    self.speak("Have a good day "+self.name[0][0])
                    break
                try:
                    self.phrase = self.response.recognize_google(
                        audio, language="en-in")
                    self.phrase = self.phrase.lower()
                    print(self.phrase)
                except sr.UnknownValueError:
                    self.speak("You don't say anything. I will close soon.")
                    self.i += 1
                    self.phrase = ""

                if (len(self.phrase) != 0):
                    self.i = 0


                if "web" in self.phrase:
                    webbrowser .open_new_tab(
                        "https://bit.ly/timmey")
                    self.speak("I am opening web site")

                
                if "spam" in self.phrase:
                    kelime = input("Lütfen kelimeyi girin: ")
                    tekrar = int(input("Kaç defa tekrar yazdırmak istersiniz? "))

                    for i in range(tekrar):
                        print(kelime)
                        time.sleep(0.2)
                        print()


                if "what" in self.phrase:
                    webbrowser .open_new_tab(
                        "https://enesaksoy1732.wixsite.com/timmey/komutlar")
                    self.speak("I am opening my code")

                if "youtube" in self.phrase:
                    webbrowser .open_new_tab(
                        "https://www.youtube.com/channel/UC8XAXRYCJ1PDR3z5kO5JHRg")
                    self.speak("I am opening youtbe change")


                if "time" in self.phrase:
                    webbrowser .open_new_tab("https://sites.google.com/view/timeytime/ana-sayfa")
                    self.speak("I am opening time")



                if "translate" in self.phrase:
                    webbrowser .open_new_tab(
                        "https://www.google.com/search?client=opera-gx&q=çeviri&sourceid=opera&ie=UTF-8&oe=UTF-8")
                    self.speak("I am opening google trenslate")


                if "open" in self.phrase:
                    list = self.phrase.split(" ")
                    a = list.index("open")
                    if ("." in list[a+1]):
                        webbrowser.open_new_tab("https://www."+list[a+1])
                    else:
                        webbrowser.open_new_tab("https://www."+list[a+1]+".com")
                    self.speak("I am opening "+list[a+1])

                elif "don't listen" in self.phrase or "stop listening" in self.phrase or "stop listen" in self.phrase:
                    self.speak("for how much second you want")
                    try:
                        a = int(self.re_listen())
                        self.speak("Okay. I am not listen to " +
                                str(a) + "second.")
                        time.sleep(a)
                        self.speak("I am back and ready for listen.")
                    except:
                        pass

                elif "what is your name" in self.phrase:
                    self.speak("My Name Is Timey")

                elif "how are you" in self.phrase:
                    self.speak("Fine thank you.")

                elif "how old are you" in self.phrase:
                    self.speak("We are at the same age. Did you forget?")

                elif "who are you" in self.phrase:
                    self.speak("I am your voice assistant created by Enes Aksoy")


                elif "timey" == self.phrase:
                    self.speak("Yes I am here " +
                            self.name[0][0] + ". I listening you.")

                elif "close" in self.phrase or "exit" in self.phrase or "stop" in self.phrase or "shut down" in self.phrase or "goodbye" in self.phrase:
                    self.speak("I am closing")
                    time.sleep(1)
                    self.speak("Have a good day "+self.name[0][0])
                    break

                elif "youtube" in self.phrase and "search" in self.phrase:
                    list = self.phrase.split(" ")
                    a = list.index("youtube")
                    search = ""
                    for i in list[a+1:]:
                        search += str(i+" ")
                    webbrowser.open_new_tab(
                        "http://www.youtube.com/results?search_query="+search)
                    self.speak("I am searching"+search+"in youtube")

                elif "who is" in self.phrase or "who's" in self.phrase:
                    list = self.phrase.split(" ")
                    a = list.index("who")
                    search = ""
                    for i in list[a+2:]:
                        search += str(i+" ")
                    try:
                        sentence = wikipedia.summary(search, sentences=2)
                        print(sentence)
                        self.speak(sentence)
                    except:
                        try:
                            client = wolframalpha.Client("YOUR API KEY")
                            res = client.query(self.phrase)
                            print(next(res.results).text)
                            self.speak(next(res.results).text)
                        except:
                            self.speak("I could not find anything about it.")

                elif "search" in self.phrase or "google" in self.phrase:
                    list = self.phrase.split(" ")
                    a = list.index("search")
                    search = ""
                    for i in list[a+1:]:
                        search += str(i+" ")
                    webbrowser.open_new_tab(
                        "https://www.google.com/search?q=+"+search)
                    if "on google" in self.phrase:
                        self.speak("I am searching "+search)
                    else:
                        self.speak("I am searching "+search+"on Google")

                elif "where is" in self.phrase:
                    list = self.phrase.split(" ")
                    a = list.index("where")
                    search = ""
                    for i in list[a+2:]:
                        search += str(i+" ")
                    webbrowser.open_new_tab(
                        "https://www.google.com/maps/place/"+search+"/&amp;")
                    self.speak("I am show you "+search+"location")

                elif "wikipedia" in self.phrase:
                    list = self.phrase.split(" ")
                    a = list.index("wikipedia")
                    search = ""
                    for i in list[a+1:]:
                        search += str(i+" ")
                    try:
                        sentence = wikipedia.summary(search, sentences=2)
                        print(sentence)
                        self.speak(sentence)
                    except:
                        self.speak("I could not find anything about it.")

                else:
                    try:
                        client = wolframalpha.Client("YOUR API KEY")
                        res = client.query(self.phrase)
                        print(next(res.results).text)
                        self.speak(next(res.results).text)
                    except:
                        self.speak("I could not find anything about it.")

        def greeting(self):
            hour = datetime.now().hour
            if (hour >= 7 and hour < 12):
                self.speak("Good Morning " + self.name[0][0])
            elif (hour >= 12 and hour < 18):
                self.speak("Good Afternoon " + self.name[0][0])
            elif (hour >= 18 and hour < 22):
                self.speak("Good Evening " + self.name[0][0])
            else:
                self.speak("Good Night " + self.name[0][0])

            self.listen()


    assistant = Voice_Assistant()

pencere1=tk.Tk() 
pencere1.geometry("350x350+50+100")


def sil():
    metin1.delete(0,tk.END) 

def sil2():
    metin2.delete(0,tk.END) 


def kaydet(): 

    düğme3=tk.Button(text="başla",command=işlemler,width=10,height=2)
    düğme3.grid(row=4,column=1)



yazi=tk.Label(pencere1,text="Giriş Yapınız",font="Times 18")
yazi.grid(row=0,column=1)


ad= tk.Label(text="Adınız",font="Times 10")
ad.grid(row=1,column=0)

soyad=tk.Label(text=" Soyadınız",font="Times 10")
soyad.grid(row=2,column=0) #konumlarını belirledik

metin1=tk.Entry()
metin1.grid(row=1,column=1)

metin2=tk.Entry()
metin2.grid(row=2,column=1)

düğme2=tk.Button(text="sil",command=sil,width=5,height=1)
düğme2.grid(row=1,column=2)

düğme3=tk.Button(text="sil",command=sil2,width=5,height=1)
düğme3.grid(row=2,column=2)


dügme5=tk.Button(text="kaydet",command=kaydet,width=10,height=2,)
dügme5.grid(row=4,column=1)



pencere1.mainloop()
