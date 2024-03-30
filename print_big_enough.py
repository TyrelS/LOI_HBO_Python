# Auteur: Tyrel Schrader
# Bestand: print_big_enough.py
# Beschrijving: Dit programma toont alle nummers uit een random lijst die groot genoeg zijn om vertoond te worden op het scherm
# Python versie: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Datum laatst aangepast: 30-03-2024 17:57

import random

# Deze functie print alle items uit de lijst die groot genoeg zijn
def print_big_enough(lst, n):
    lst_groot_genoeg = []
    
    for nummer in lst:
        if nummer >= n:
            lst_groot_genoeg.append(nummer)
    print(lst_groot_genoeg)

random_list = [] # Lijst aanmaken
min_grootte = 200 # Min grootte initiëren

# Vul de lijst met 20 willekeurige getallen tussen 0 en 2000
for i in range(20):
    willekeurig_getal = random.randint(0, 2000)
    random_list.append(willekeurig_getal)

print_big_enough(random_list, min_grootte)