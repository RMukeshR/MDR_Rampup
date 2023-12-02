def load(file):
    with open(file, "r", encoding='UTF-8') as file:
        data =  file.read()
        return data

raw_text = load("/home/mukesh/Tensorflow/MDR_Rampup/NER/data/text_data/outputfile.txt")

titles = ["Dr","MD", "Mr", "Mrs", "Ms", "Miss", "Mr and Mrs"]

text = raw_text.strip()
text = text.split("\n")
text

Doc = []
patient =[]
per =[]

import string
for i in text:
    translator = str.maketrans('', '', string.punctuation)
    text_no_punctuation = i.translate(translator)
    k = text_no_punctuation.split(" ")

    for j in k:
        if j in titles:
            per.append(i)

for i in per:
    if "Dr" in i:
        Doc.append(i)
    else:
        patient.append(i)

print("Doctor - ", Doc)
print("patient - ", patient)

