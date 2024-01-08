from PIL import Image

import pytesseract

image = Image.open('/Users/boss/Desktop/ocr.png')

text = pytesseract.image_to_string(image)

text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')

print(text)



