#!/usr/bin/env bash

#grep -c -i Hamlet william.sheakespeare
#grep -c -i Ophelia william.sheakespeare
#grep -c -i Macbeth william.sheakespeare
#grep -c -i Lady william.sheakespeare
#grep -c -i "Lady Macbeth" william.sheakespeare
#grep -c -i Henry william.sheakespeare

#deginijuemy liste imion
text=william.sheakespeare

#definiujemy liste imion
names="Hamlet Ophelia Macbeth Henr Lady and"


#robimy petle po kolejnych imionach
for name in $names
#zawartosc petli pod spodem
do
	#wyswietlamy nazwe zmiennej
	echo -n  $name ": "
	#sprawdzamy ile razy zmienna wystepuje w pliku
	grep -c -i  $name $text
	grep -c -i -w $name $text
done

echo $text

text="Praca skończona"

echo $text