#opening a file and assigning it to a variable
file = open("fruits.txt", "r")
#Assisgning file varianle into anothe variable
content = file.readlines()
file.close()
for i in content:
    print(len(i.strip()))
