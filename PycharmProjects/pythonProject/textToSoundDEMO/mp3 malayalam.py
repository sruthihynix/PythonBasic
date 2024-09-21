from gtts import gTTS
from playsound import playsound
import io

fp=io.open("malayalam",mode="r",encoding="utf-8")
bb1=fp.read()

ob=gTTS(bb1,lang='ml')
ob.save("m1.mp3")
playsound("m1.mp3")

#  pip install gtts --library----pip install playsound==1.2.2
#  "  "      playsound ---