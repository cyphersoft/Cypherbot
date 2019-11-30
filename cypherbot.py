import speech_recognition as sr
import os
import time
import serial
import datetime
import pyttsx3
import random
import wikipedia

engine = pyttsx3.init()
now = datetime.datetime.now()
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
command = str.encode('1')
command2 = str.encode('2')
command3 = str.encode('3')
command4 = str.encode('4')
command5 = str.encode('5')
sr.Microphone(device_index=1)
now = datetime.datetime.now()
r = sr.Recognizer()
r.energy_threshold = 2000

var1 = ['hi', 'hello']
var2 = ['who created you', 'who is your inventor', 'who has made you']
var3 = ['move forward', 'move ahead', 'move', 'go ahead','come ahead', 'moon', 'new', 'go', 'forward']
var4 = ['move backward', 'come back', 'turn vertically', 'back', 'backward']
var5 = ['stop', 'stop moving', 'top', 'top moving']
var6 = ['move left', 'turn left', 'left']
var7 = ['turn right', 'move right', 'right']


with sr.Microphone() as source:
    print("Speak!")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language="en-in")
        print("You said : {}".format(text))
        if text in var1:
           os.system('espeak "hi bro"')
           time.sleep(0.01)
           os.system("python3 cypherbot.py")
        elif 'how are you' in text:
           os.system('espeak "i am fine bro"')
           time.sleep(0.01)
           os.system("python3 cypherbot.py")
        elif 'what can you do' in text:
           os.system('espeak "anything you command"')
           time.sleep(0.01)
           os.system("python3 cypherbot.py")
        elif 'turn on led' in text :
           ser.write(command)
           os.system('espeak "bro" ')
           time.sleep(0.01)
           os.system("python3 cypherbot.py")
        elif 'in which language you were programmed' in text:
           os.system('espeak "i was progarmmed in python"')
           time.sleep(0.01)
           os.system("python3 cypherbot.py")
        elif 'can you walk' in text:
           os.system('"espeak "yes bro"') 
           ser.write(command)
           time.sleep(0.01)
           os.system("python3 cypherbot.py")
        elif 'on which os do you run' in text :       
           os.system('espeak "i run on linux ditribution named raspbian"')
           time.sleep(0.01)
           os.system("python3 cypherbot.py")
        elif text in var2 :
            os.system('espeak "i was created at cyphersoft by two engineers"')
            time.sleep(0.01)
            os.system("python3 cypherbot.py")
        elif text in var3:
            os.system('espeak "ok"')
            ser.write(command)
            time.sleep(0.01)
            os.system("python3 cypherbot.py")
        elif text in var4:
            os.system('espeak "ok"')
            ser.write(command2)
            time.sleep(0.01)
            os.system("python3 cypherbot.py")
        elif text in var5:
             os.system('espeak "ok"')
             ser.write(command3)
             time.sleep(0.01)
             os.system("python3 cypherbot.py")
        elif text in var6:
            os.system('espeak "ok"')
            ser.write(command4)
            time.sleep(0.01)
            os.system("python3 cypherbot.py")
        elif text in var7:
            os.system('espeak "ok"')
            ser.write(command5)
            time.sleep(0.01)
            os.system("python3 cypherbot.py")
       
        else:
           os.system('python3 cypherbot.py')
          
    except:  
        print("Can't recognize")
        os.system('python3 cypherbot.py')
