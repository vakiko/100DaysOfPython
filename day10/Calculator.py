# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 23:10:32 2022

@author: victo
"""
from art import logo, title

def add(n1,n2):
    """adds the two numbers if an + operator is given"""
    return n1+n2
def sub(n1,n2):
    """subtracts the two numbers if an - operator is given"""
    return n1-n2
def mut(n1,n2):
    """multiplies the two numbers if an * operator is given"""
    return n1*n2
def div(n1,n2):
    """divides the two numbers if an / operator is given"""
    return n1/n2
UseAns = False
print(logo)
print(title)

print("Howdy! Welcome to this calculator. You will be asked to enter your first number, then the operator, then the second.")
while(True):
    status = input("Would you like to clear the screen? ")
    if status.lower() == 'y':
        print("\033[H\033[J")
    if not UseAns:
        number1 = int(input("Please enter the first number: "))
    operator = input("Please enter the operand: ")
    number2 = int(input("Please enter the second number: "))
    if operator == '+':
        ans = add(number1,number2)
        print(number1, operator, number2, '=', ans)
    if operator == '-':
        ans = sub(number1,number2)
        print(number1, operator, number2, '=', ans)
    if operator == '*':
        ans = mul(number1,number2)
        print(number1, operator, number2, '=', ans)
    if operator == '/':
        ans = div(number1,number2)
        print(number1, operator, number2, '=', ans)
    UseAns = False
    redo = input("Would you like to go again using", ans, " 'y', restart entirely 'r', or quit 'q'?")
    if redo == 'y':
        print("Using", ans, "as the first number.")
        UseAns = True
        number1 = ans
    elif redo == 'q':
        break
