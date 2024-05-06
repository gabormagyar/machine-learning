from transformers import pipeline
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

nlp = pipeline(
    "document-question-answering",
    model="impira/layoutlm-document-qa",
)

print(nlp(
    "invoice.jpg",
    "What's the total amount?"
))

print(nlp(
    "invoice.jpg",
    "What's the fax number of Company Name?"
))
