import speech_recognition as sr# library to get user  voice
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
command='alexa play music'

def take_command():
    print("kk")

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            global command

            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'alexa' in command:  # first check there is a word alexa
                command = command.replace('alexa', '')

                print(command)
    except:
        pass


    return command


def run_alexa():
    command1 = take_command()
    print(command1)
    if 'play' in command1:
        song = command1.replace('play', '')
        talk('playing ' + song)# talk fun
        pywhatkit.playonyt(song)
    elif 'time' in command1:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command1:
        person = command1.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command1:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command1:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()