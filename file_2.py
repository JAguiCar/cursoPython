#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------
__author__ = "Jaqueline Aguilar"
__copyright__ = "Copyright 2018, ST Project"
__credits__ = ["Jaqueline Aguilar"]
__license__ = "GPL 2"
__mainteiner__ = "JAC"
__email__ = "jaguilar@stengineeringsolutions.com"
__status__ = "Debug"
__execution__ = "python codel.py"
#------------------------
#Library
import random

#------------------------
#Listas
#RANDOM Genera números aleatorios entre 1 y 10
#APPEND para llenar la lista
#SHUFFLE retorna una mezcla de elementos de una secuencia

#Code
class myFirstClass():
    """Docstring for class"""
    def __init__(self):
        self.list1 = [1,2,3,4,5,6,7,8,9,10]
        self.list2 = []
        self.a = 5
    
        self.b = random.randint(1,10)

    def funct1(self):
        if(self.a == self.b):
            print("numero iguales")
            print(self.b)
        else:
            print("numero diferentes")
            print(self.b)


    def funct2(self):
        for i in self.list1:
            self.list2.append(i)
            print(i)

        random.shuffle(self.list2)
        if(self.list2[5]==6):
            print("Correct")
        else:
            print("Fail")


#------------------------
#Execution
if __name__ == "__main__":
    t = myFirstClass()
    t.funct1()
    t.funct2()
