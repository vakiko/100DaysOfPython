import pandas

alphabet = open("nato_phonetic_alphabet.csv")
alphabet_list = alphabet.readlines()
alphabet_list = alphabet_list[1:]
alphabet_dict = {}
for line in alphabet_list:
    alphabet_dict[line[0]] = line[2:].strip()

pandas_dict={'letter':[],'code':[]}
 
for key,value in alphabet_dict.items():
    pandas_dict['letter'].append(key)
    pandas_dict['code'].append(value)


#TODO 1. Create a dictionary in this format:
nato_alphabet = pandas.DataFrame(pandas_dict)
user_input = input("Please enter what you would like converted into the NATO Alphabet: ")
output = []
for i in user_input:
    print(i)
    for (index,row) in nato_alphabet.iterrows():
        if row[0] == i.upper():
            output.append(row[1])
print(output)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

