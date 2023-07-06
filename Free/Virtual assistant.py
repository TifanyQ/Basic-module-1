#https://www.youtube.com/watch?v=PyDn2gU9DJo&t=207s&ab_channel=Simplilearn
"Paquete de reconociemiento de voz"
#import speech_recognition as aa
#Se le incorpora el alias aa, para usar las funcionalidades del paquete usando solo "aa"

import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

#Permite utilizar las funcionalidades del módulo
listener = aa.Recognizer()

machine = pyttsx3.init()
def talk(text):
    machine.say(text)
    machine.runAndWait()
def input_instruction():
    global instruction
    #Manejar excepciones. El bloque try permite ejecutar el fragmento del código
    #donde se espera que ocurra una excepción y "except" dice como manejar esa excepción
    try:
    #Abre el micrófono 0
        with aa.Microphone() as origin:
            instruction = listener.listen(origin)
            print("listening ...")
    #Escucha el audio de origin y lo guarda en speech
            speech = listener.listen(origin)
        #Reconocer el audio usando el servicio de reconocimiento de voz de google
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "Jarvis" in instruction:
                instruction = instruction.replace('jarvis', '')
                print(instruction)

    except:
        pass
    return  instruction
def play_Jarvis():

    instruction = input_instruction
    print(instruction)
    if 'play' in str(instruction):
        song = instruction.replace('play',"")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in str(instruction):
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time'+ time)

    elif 'date' in str(instruction):
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date"+ date)

    elif 'how are you' in str(instruction):
        talk('I am fine, how about you')

    elif 'What is your name' in str(instruction):
        talk('I am Jarvis, what ca I do for you?')

    elif 'who is' in str(instruction):
        human = instruction.replace('who is'," ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    else:
        talk('Please repeat')

play_Jarvis()