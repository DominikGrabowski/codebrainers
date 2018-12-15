#!/usr/bin/env python
"""Program losuje liczbe calowita z zakresu 1 do 100.
Użytkowanik ma 7 prób na zgadnięcie tej liczby."""

from random import randint

zagadka = randint(1,100)

liczba = "0"
proba = 0
maksymalna_proba = 7

while(liczba != zagadka):
    print("Podaj liczbę:")
    liczba = int(input())
    proba += 1

    if liczba == zagadka:
        print("Sukces, w {1} próbie zgadłeś wylosowaną liczbę, która jest {0}.".format(zagadka, proba))
    else:
        if liczba > zagadka:
             print("Wybierz mniejszą liczbę.")
        else:
            print("Wybierz większą liczbę.")
    
        if proba >= maksymalna_proba:
            print("Niestety nie udało się w {1}. Wylosowano liczbe {0}. ".format(zagadka, proba))
            break