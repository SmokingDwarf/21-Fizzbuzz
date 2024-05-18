# Vraag de gebruiker om een getal in te voeren
# Zorg ervoor dat je dit ook echt als getal kunt gebruiken
getalInvoer = float(input('Voer een getal in: '))
# Als het getal deelbaar is door 3:     print fizz
# Als het getal deelbaar is door 5:     print buzz
# Als het getal deelbaar is door 3 & 5: print fizz én buzz
# Anders print je het getal
if getalInvoer % 3 == 0 and getalInvoer % 5 == 0:
    print('fizz én buzz')
elif getalInvoer % 3 == 0:
    print('fizz')
elif getalInvoer % 5 == 0:
    print('buzz')

else:
    print(getalInvoer)
# Voorbeeld:
# Gebruiker geeft het getal 12 in
# 12 is deelbaar door 3 (12/3 = 4), dus 'fizz' wordt geprint
# 12 is niet deelbaar door 5 (12/5 = 2.4), dus 'buzz' wordt niet geprint
# Omdat 12 deelbaar is door 3 hoeft het getal zelf niet geprint te worden.

# Voor de getallen 1 t/m 5:
# 1 -> 1
# 2 -> 2
# 3 -> 'fizz'
# 4 -> 4
# 5 -> 'buzz'