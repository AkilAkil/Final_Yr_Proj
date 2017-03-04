from PIL import Image
import pytesseract
i=Image.open("img4.jpg")
print pytesseract.image_to_string(i)
#print i

