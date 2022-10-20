# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 22:12:21 2022

@author: victo
"""

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
print("Aces count as 11, unless the total exceeds 21 - in such a case, it counts as 1.")
print("The dealer will draw another card if their total is < 17.")
print("Untill then, have fun!")


def drawCard(num = 1):
    global deck
    newCards = []
    print("Drawing", num, "card(s)...")
    while num != 0:   
        newCard = random.choice(deck)
        deck.remove(newCard)
        newCards.append(newCard)
        num -=1
    return newCards

def results(hand):
    if 1 in hand and sum(hand) < 21:
        hand.remove(1)
        hand.append(11)
    return sum(hand)
    
#dealer - first card
#totdea - total of the dealer
def blackjack():
    user = []
    dealer = []
    pun = ".\n"
    gameOver = False
    
    user.extend(drawCard(2))
    dealer.extend(drawCard(2))
    
    while not gameOver:
        userTotal = results(user)
        dealerTotal = results(dealer)
        print("Your hand is", user, end = pun)
        print("The dealer's first card is", dealer[0], end = pun)
        if userTotal >= 21 or dealerTotal >= 21:
            gameOver = True
            break
            
        ans = input("Would you like to draw another card?").lower()
        if ans == 'y':
            draw = drawCard()
            print("You have drawn", draw, end = pun)
            user.extend(draw)
        else:
            gameOver = True
            
    if gameOver:
        while dealerTotal < 17:
            print("The dealer is drawing another card...")
            draw = drawCard()
            dealer.extend(draw)
            dealerTotal = results(dealer)
        
        if dealerTotal == 21 or dealerTotal >= userTotal or userTotal > 21:
            print("Sorry, you've lost!")
        else:
            print("Congratulations - you won!")   
         
    print("You had a hand of", user)
    print("The dealer had a hand of", dealer)
        
    print("You finished with a total of", userTotal, end = pun)
    print("The dealer finished with a total of", dealerTotal, end = pun)
    print("-----------------------------------------------------------")
        
    
while(True):

    print("The deck has been shuffled.")
    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
    s = input("Would you like to play blackjack? ").lower()
    if s == 'y':
        blackjack()
    if s == 'n':
        break
    