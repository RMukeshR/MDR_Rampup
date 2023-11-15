import easyocr
import pandas as pd
reader = easyocr.Reader(['en']) 

import os
image_path = "/data1/home/mukeshram/MDR_Rampup/OCR/25-1.jpeg"

results = reader.readtext(image_path)
data = []
for detection in results:
    text = detection[1]
    data.append(text)
print(data)




