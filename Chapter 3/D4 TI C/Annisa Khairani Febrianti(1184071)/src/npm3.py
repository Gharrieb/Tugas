# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:20:52 2019

@author: NISA
"""

def npm3(npm):
    for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])):
        print("Hallo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")

i=0
npm=input("Masukan NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1
npm3(npm)