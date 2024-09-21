from gtts import gTTS
from playsound import playsound
import io

f=io.open("book1",mode="r",encoding="utf-8") #utft-> standard reading format
b=f.read()

ob=gTTS(b,lang='en')
ob.save("e1.mp3")
playsound("e1.mp3")

#  pip install gtts --library
#  "  "      playsound --- pip install playsound==1.2.2