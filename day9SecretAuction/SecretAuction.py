# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 18:51:53 2022

@author: victo
"""


from art import logo, endlogo


print(logo)
print("Howdy! Welcome to the secret auction. Here, you can anonymously bid. Please hand the program to the first anonymous bidder.")
bidders = {}
while(True):
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: "))
    bidders[name] = bid
    
    print("Your bid has been collected. Are there any other bidders?")
    status = input("Please enter 'y' or 'n': ").lower()
    
    #clears the screen on spyder to keep it anonymized
    print("\033[H\033[J") 

    if status == 'n':
        print(endlogo)
        print("And that concludes the secret auction!")
        break
#tabulates the highest bid
highest = 0
for key in bidders:
    if bidders[key] > highest:
        highest = bidders[key]
        winner = key
print("And the winner is...", winner, "with a winning bid of $" + str(highest), end = '!')