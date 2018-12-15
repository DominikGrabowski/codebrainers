#!/usr/bin/env/ bash

# Tworzymy katalog 2018.12.15.cwieczenia, flaga -p zapewnia, ze nie bedzie bledu jezeli istnieje
mkdir -p 2018.12.15.cwiczenia
cd 2018.12.15.cwiczenia

echo "TO jest nasz skrypt"

# By zapisać do pliku używamy przekierowania > gdy nadpisujemy lub >> gdy dodajemy do konca
echo "A to zostanie zapisane w pliku stdout.txt o godzinie " $(date)  >> stdout.txt

echo "sprawdzmy czy rzeczywiscie plik stdout.txt zawiera nasz napis"

date 

more stdout.txt