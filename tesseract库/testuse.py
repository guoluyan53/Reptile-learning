# import pytesseract
import
from PIL import Image

#指定tesseract.exe所在的路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'

#打开图片
image = Image.open("a.png")
text = pytesseract.image_to_string(image)
print(text)
