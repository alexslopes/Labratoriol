#!/usr/env python
#-*- enconding: UTF-8-*-

inteiro = list(range(5))
cont = 9
for i in range(5):
    inteiro[i] = cont
    cont+=1
    
for i in range(len(inteiro)):
    print(inteiro[i])
    
print("\n")
    
nomes = ["Zé", "João","Tonho"]

for i in range(len(nomes)):
    print(nomes[i])
    
print("\n")
    
nomes[0] = "Maria"

for i in range(len(nomes)):
    print(nomes[i])
