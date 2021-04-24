# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:21:59 2021

@author: carols1107
"""
class Human():
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    def BMI(self):
        return self.weight / ((self.height/100)**2)
   

class Woman(Human):
    def __init__(self, name, weight, height, bust, waist, hip):
        super().__init__(name, weight, height)
        self.bust = bust
        self.waist = waist
        self.hip = hip
    def PrintBWH(self):
        print("bust = {}, waist = {}, hip = {}".format(self.bust, self.waist,self.hip))
    