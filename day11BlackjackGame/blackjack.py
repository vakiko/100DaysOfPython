# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 00:07:29 2022

@author: victo
"""

import random
from art import logo

print(logo)
print("Howdy! Welcome to Blackjack.")
print("Unlike Angela Yu's house rules, this will have a 52-card deck.")
print("Aces count as 1.")
print("The dealer will draw another card if their total is < 17.")
print("Untill then, have fun!")


def drawCard():
    print("Drawing card...")
    global deck
    
    newCard = random.choice(deck)
    deck.remove(newCard)
    
    return newCard
    
#dealer - first card
#totdea - total of the dealer
def blackjack():
    hand = []
    dealer = []
    pun = ".\n"
    
    hand.append(drawCard())
    hand.append(drawCard())
    dealer.append(drawCard())
    dealer.append(drawCard())
    
    status = False
    total = 0
    totdea = 0
    
    total = sum(hand)
    totdea = sum(dealer)
    
    print("Your current hand is", hand, end = pun)
    print("Your total is", total, end = pun)
    print("Your dealer's first card is", dealer[0], end = pun)
    
    if total > 21:
        print("Ohhh, you busted on draw - unlucky! Better luck next time.")
        return
    if total == 21:
        print("Woah, lucky! Congratulations, you won.")
        return
    
    redo = input("Draw again (Y/N): ").lower()
    
    if redo == 'y': status = True
    
    while status:

        draw = drawCard()
        print("You have drawn", draw, end = pun)
        total += draw
        hand.append(draw)

        print("Your current hand is", hand, end = pun)
        print("Your total is", total, end = pun)
        if total >= 21:
            break
        else:
            redo = input("Draw again (Y/N): ").lower()
            if redo == 'n':
                break
    

    print("The dealer has a total of", totdea, end = pun)
    print("Their hand is", dealer, end = pun)
    
    if total > 21:
        print("Sorry, it's a bust. Better luck next time!")
        return
    
    if totdea < 17:
        print("The dealer has to draw another card - their total is less than 17.")
        draw = drawCard()
        totdea += draw
        dealer.append(draw)
        print("The dealer drew", draw, end = pun)
        print("Their hand is", dealer, end = pun)
        print("The dealer has a total of", totdea, end = pun)
        
    if totdea >= 21:
        print("The dealer busted! You won.")
        return
    
    if total == 21:
        print("Congratulations! You've won.")
        return 
    if totdea == total:
        print("It's a tie. Better luck next time!")
        return
    elif totdea < total:
        print("Congratulations! You've won.")
        return
    else:
        print("Sorry, you've lost. Better luck next time!")
        return


    
while(True):

    print("The deck has been shuffled.")
    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
    s = input("Would you like to play blackjack? ").lower()
    if s == 'y':
        blackjack()
    if s == 'n':
        break
    