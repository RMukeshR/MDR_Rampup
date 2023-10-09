def load(file):
    with open(file, "r", encoding='UTF-8') as file:
        data =  file.read()
        return data

print(load("/data1/home/mukeshram/Natural_Language_Processing/NER/data/text_data/outputfile.txt"))


def Preprocessing(data):
