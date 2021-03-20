# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:31:04 2021

@author: carols1107
"""

import random

Num = random. randint(0,20)


Yes = False
while Yes == False:
    Guess = input("猜個數字:")
    
    if Num == int(Guess):
        print("猜對了")

        Yes = True
    
    else:
        print("猜錯了")
        print(Num)    

    

