from gtts import gTTS
from playsound import playsound
import io

fp=io.open("Hindi",mode="r",encoding="utf-8")
h1=fp.read()

ob=gTTS(h1,lang='hi')
ob.save("h1.mp3")
playsound("h1.mp3")

#  pip install gtts --library
#  "  "      playsound ---pip install playsound==1.2.2