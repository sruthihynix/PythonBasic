from gtts import gTTS
from playsound import playsound

token=input("input a number")
txt="Token number "+token
ob=gTTS(txt,lang='en')  # add to variable ob using gtts()

ob.save("tokenNo.mp3")  # saving the  audio with save(' name.mp3') in mp3 format
playsound("tokenNo.mp3")# playsound() to paly sound-> playsound('filename.mp3')


#  pip install gtts --library
#  "  "      playsound ---