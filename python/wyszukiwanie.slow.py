#!/usr/bin/env python

imiona = ["Hamlet", "Macbeth", "Ophelia", "Henry"]

for imie in imiona:
    print("Panie i Panowie! Przed Pańśtwem... {}!".format(imie))

sonet42 = """That thou hast her it is not all my grief,
And yet it may be said I loved her dearly,
That she hath thee is of my wailing chief,
A loss in love that touches me more nearly.
Loving offenders thus I will excuse ye,
Thou dost love her, because thou know’st I love her,
And for my sake even so doth she abuse me,
Suff’ring my friend for my sake to approve her.
If I lose thee, my loss is my love’s gain,
And losing her, my friend hath found that loss,
Both find each other, and I lose both twain,
And both for my sake lay on me this cross,
  But here’s the joy, my friend and I are one,
  Sweet flattery, then she loves but me alone."""

#for i in sonet42:
#   print(i, en d="")
#print("",end='\n')     

#for line in sonet42.splitlines():
    #for word in line.split() :
        #sprawdzamy czy word jest rowne love
        #if word == 'love':
            #print(word, line)
        #sprawdzamy czy slowo "love" zawiera sie w wyrazie word    
        #if 'love' in word:
            #print(word, line)  
  

print("Podaj słowo, które chcesz wyszukać:")
slowo = input ()

for line in sonet42.splitlines():
    for word in line.split():
        if slowo in word:
            print(word, line)   