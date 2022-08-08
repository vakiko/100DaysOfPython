# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 22:43:36 2022

@author: victo
"""
import random
word_list = ["dog", "cat", "aardvark", "rhino"]
print("howdy, and welcome to...")
print(r"""                                                                           
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/               or woman!""")
print("note: over 200 words are taken from hangmanwords.com")
dead = False
won = False
invalid = False
missed_letters = 0
pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 


word = random.choice(open("hardwords.txt").readlines()).rstrip()
blanks = '_' * len(word)
guessed_letters = ''
list1 = list(blanks)

def hangman():
    print(pics[missed_letters])
    print(' '.join(list1))
while(True):
    if not invalid:
        hangman()
        letter = input('Guess any letter: ').lower()
    #print the hangman pics
    #prompts the user to guess
    #find if guess is correct -> change blanks -> picture -> print blanks
    if letter in guessed_letters and not invalid:
        print("You have already guessed this word. Try again.")
    elif letter in word and not invalid:
        position = 0
        for i in word:
            if letter == i:
                list1[position] = letter
            position += 1
        guessed_letters += letter
        if '_' not in list1:
            won = True
    elif letter not in word and not invalid:
        print('Sorry, that is not part of the word.')
        missed_letters += 1
        guessed_letters += letter
        if missed_letters == len(pics)-1:
            hangman()
            print('Sorry, your stickman is dead! The word was', word)
            dead = True
    elif letter in '0123456789' and not invalid:
        print("Please, no numbers. Try again.")
    else:
        if not invalid:
            print("Invalid input. Try again.")
    if dead or won:
        if won:
            print("Congratulations!", end = ' ')
        print("You have reached the end of the game.")
        status = input('Would you like to play again? ').lower()
        if status == 'y':
            print('Restarting game...')
            dead = False
            won = False
            missed_letters = 0
            word = random.choice(open("hardwords.txt").readlines()).rstrip()
            blanks = '_' * len(word)
            guessed_letters = ''
            list1 = list(blanks)
            invalid = False
        elif status == 'n':
            print('Ending game.')
            break
        else:
            print("Invalid input. Please try again.")
            invalid = True

        
