#!/usr/bin/env python

lista1 = [x**2 for x in range(1,100)]
lista2 = [x**3 for x in range(1,50)]

print(lista1, lista2)

#informujemy o dlugosci listy
print("dlugosc listy pierwszej to {}, a drugiej to {}".format(len(lista1),len(lista2)))

wspolne = []

#to jest petla po elementach listy lista1
for el in lista1:
    if el in lista2:   
        wspolne.append[el]
        print(el)
print(wspolne, len(wspolne))