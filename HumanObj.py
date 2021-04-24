# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:21:59 2021

@author: carols1107
"""
import HumanClass

David = HumanClass.Human("David",50,162)

print(David.name,"BMI:", David.BMI())





Jenny = HumanClass.Woman("Jenny",40, 180, 40, 20, 30)

print(Jenny.name,"BMI:", Jenny.BMI())
Jenny.PrintBWH()
