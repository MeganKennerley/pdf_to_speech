from PyPDF2 import PdfReader
import pyttsx3

reader = PdfReader('Test.pdf')
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
paragraph_text = text.strip().replace("\n", " ")

engine = pyttsx3.init(debug=True)
rate = engine.getProperty('rate')
engine.setProperty('rate', int(rate) - 100)
engine.say(paragraph_text)
engine.runAndWait()

