import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def TextRecognation():
    img = cv2.imread('test4.png')
    text = pytesseract.image_to_string(img)
    print(text)