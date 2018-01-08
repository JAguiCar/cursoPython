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
#------------------------
#Corrimiento de bits
#Code

def bitwise():
    """Change the value of the specific byte position of the list using logical\
    operators and right left shifts"""
    list1 = [0x0f, 0x10, 0x82, 0x02, 0xb4, 0xa7, 0x65, 0x94, 0x61, 0xab,\
            0x0f, 0x10, 0x82, 0x02, 0xb4, 0xA7, 0x65, 0x94, 0x61, 0xab]
    list2 = []   
    mask = 0x0f #mascara para corrimiento

    print("Lista Original")
    for i in list1:
        print(hex(i))
               
    #print(list1)
    #print(hex(list1[0]))
    #print(hex(list1[19])) 

    print("Lista AND")
    for i in list1:
        a = i & mask
        list2.append(a)
        print(hex(a))
    #print(list2)

    print("Lista OR")
    for i in list1:
        a= i|mask
        list2.append(a)
        print(hex(a))
    #print(list2)

    print("Lista XOR")
    for i in list1:
        a= i^mask
        list2.append(a)
        print(hex(a))
    #print(list2)

    print("Lista Corrimiento")
    for i in list1:
        maskCorr = mask<<2        
        a= i & maskCorr
        list2.append(a)
        print(hex(a))

    print("Mascara con corrimiento")
    print(hex(maskCorr))
    #print(list2)

#------------------------
#Execution
bitwise()
