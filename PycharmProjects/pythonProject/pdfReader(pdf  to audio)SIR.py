import PyPDF2
import pytt

# path of the PDF file//
# p="file:C:/Users/HP/PycharmProjects/pythonProject/AR.pdf"
path = open('AR.pdf','r')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader('AR.pdf')

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(1)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()





