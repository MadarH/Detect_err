#!/usr/bin/env python3

mot=input("Entrez un mot : ")
print("Lettre Valeur csum1  csum2")
cs1=0
cs2=0
for i in range(len(mot)):   
    cs1 = cs1 + ord(mot[i])
    cs2 = cs2 + cs1
    print("   "+mot[i]+"     "+str(ord(mot[i]))+ "    "+str(cs1)+"    "+str(cs2) )   
