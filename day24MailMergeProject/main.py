import string

nameFile = open("./input/names/invited_names.txt")
names = nameFile.readlines()
letterFile = open("./input/letters/starting_letter.txt")
letter = letterFile.readlines()
firstLine = letter[0].strip("[name],\n")
for name in names:
    name = name.strip('\n')
    letter[0] = firstLine + name + ',\n'
    f = open(f"./output/readytosend/letter_{name}.txt", "a")
    f.writelines(letter)
