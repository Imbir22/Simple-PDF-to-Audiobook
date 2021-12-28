from gtts import gTTS
import PyPDF2


# Opening PDF with PyPDF2 and getting number of pages
pdfFileObject = open(r"lorem-ipsum.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
number_of_pages = pdfReader.numPages

n = 1

# Extracting each page to text and converting it into mp3 with gTTS
for page in range(number_of_pages):
    pageObject = pdfReader.getPage(page)
    text = pageObject.extractText()
    tts = gTTS(text)
    tts.save(f'ExamplePageNr{n}.mp3')
    n+=1

# Files are saved to the same folder as the project


