import json

with open("iris.json","r") as f:
    data = json.load(f)

print(data[:5])
print("\n")

print(json.dumps(data[:5],indent=4))

print("\n")

for key, value in data[0].items():
    print(key,value)

print("\n")
for i in data[:5]:
    print("sepalLength" +" = "+ str(i["sepalLength"]))

    print('petalLength' +" = "+ str(i['petalLength']))

    print("'species'" +" = "+ str(i['species']))


