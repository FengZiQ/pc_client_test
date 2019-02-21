# coding=utf-8
from PIL import Image
import pytesseract

# cn = pytesseract.image_to_string(
#     Image.open('cn.png'),
#     lang='chi_sim'
# )
# print(cn)

en = pytesseract.image_to_string(Image.open('en.png'), lang='eng')
print(en)