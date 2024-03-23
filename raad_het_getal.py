# Auteur: Tyrel Schrader
# Bestand: raad_het_getal.py
# Beschrijving: Dit programma bestaat uit een eenvoudig spel waarbij de gebruiker het juiste getal moet raden
# Python versie: 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)]
# Datum laatst aangepast: 23-03-2024 20:26

import random # Random-library gebruiken

# Initialiseren
max_pogingen = 10 # Maximum aantal pogingen om het getal te raden
bovengrens = 100 # Bovengrens voor het te raden getal

# Kies een willekeurig geheel getal tussen 1 en bovengrens
antwoord = random.randint(1,bovengrens)

def raadGetal(): # Functie voor het raden van een getal
    poging_getal = int(input("Voer een getal in: ")) # Gebruiker vragen om een getal in te voeren
    return poging_getal # Het getal terug sturen naar het programma

def checkInvoer(p, a, mp, b): # Functie voor het controlleren van het ingevoerde getal
    aantal_pogingen = 1 # Aantal pogingen initialiseren op 1
    while p != a and aantal_pogingen < mp: # Zolang 'p' (poging) niet gelijk is aan 'a' (antwoord) en 'aantal_pogingen' kleiner is dan 'mp' (max_poging)
            if p > a and p < 100: # Wanneer 'p' groter is dan 'a' en 'p' kleiner is dan 'b' (bovengrens)
                print("Lager!") # Toon melding: 'Lager!'
                p = raadGetal() # Gebruiker vragen om opnieuw een getal in te voeren
                aantal_pogingen += 1 # Aantal pogingen verhogen met 1
            elif p < a: # Wanneer 'p' kleiner is dan a
                print("Hoger!") # Toon melding: 'Hoger!'
                p = raadGetal()
                aantal_pogingen += 1
            elif p >= b: # Wanneer 'p' groter is dan 'b'
                print("Getallen vanaf 100 of meer zijn niet toegestaan!") # Toon foutmelding op het scherm
                p = raadGetal()
            
    if aantal_pogingen < mp: # Wanneer 'aantal_pogingen' kleiner is dan 'mp'
        print("Goed geraden!\nEn dat in",aantal_pogingen,"pogingen.") # Toon het eind resultaat op het scherm
    else:
        print("Helaas, je hebt al 10x het getal proberen te raden zonder succes...") # Toon resultaat
    
# Vraag de gebruiker een getal in te voeren
print("Raad een getal onder de 100.")
poging_getal = raadGetal() # Functie 'raadGetal' aanroepen en 'poging_getal' vullen met het resultaat   
checkInvoer(poging_getal, antwoord, max_pogingen, bovengrens) # Functie 'checkInvoer' aanroepen met de parameters 'poging_getal', 'antwoord', 'max_pogingen' en 'bovengrens'
            