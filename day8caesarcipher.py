# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 13:25:55 2022

@author: victo
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    #iterates through each letter in the phrase, num is for its index
    num = 0
    for i in text:
        #wants to find alphabet matching letter
        index = 0
        for letter in alphabet:
          if letter == i:
              list1[num] = alphabet[index+shift]
              break
          index += 1
        num += 1
def decrypt(text,shift):
    #iterates through each letter in the phrase, num is for its index
    num = 0
    for i in text:
        #wants to find alphabet matching letter
        index = 0
        for letter in alphabet:
          if letter == i:
              list1[num] = alphabet[index-shift]
              break
          index += 1
        num += 1
print(r"""                                                   .__       .__                  
  ____ _____    ____   ___________ _______    ____ |__|_____ |  |__   ___________ 
_/ ___\\__  \ _/ __ \ /  ___/\__  \\_  __ \ _/ ___\|  \____ \|  |  \_/ __ \_  __ \
\  \___ / __ \\  ___/ \___ \  / __ \|  | \/ \  \___|  |  |_> >   Y  \  ___/|  | \/
 \___  >____  /\___  >____  >(____  /__|     \___  >__|   __/|___|  /\___  >__|   
     \/     \/     \/     \/      \/             \/   |__|        \/     \/       """)
while(True):
    print("Howdy! Would you like to encrypt your message or decrypt it?")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    list1 = list(text)
    shift = shift%26
    if direction.lower() == 'encode':
        encrypt(text,shift)
        print("Your encoded message is ", end='')
        print(''.join(list1), end = '.')
    elif direction.lower() == 'decode':
        decrypt(text,shift)
        print("Your decoded message is ", end='')
        print(''.join(list1), end = '.')
    status = input("Type 'n' to quit, or any other letter to continue.")
    if status.lower() == 'n':
        break
    print('')
    