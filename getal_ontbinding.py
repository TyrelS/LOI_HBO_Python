# Auteur: Tyrel Schrader
# Bestand: getal_ontbinding.py
# Beschrijving: Dit programma stelt de gebruiker in staat om een getal in te voeren. 
# Het getal wordt vervolgens ontbonden tot een product van priemgetallen.
# Python versie:3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)]
# Datum laatst aangepast: 23-03-2024 18:52

def getalOntbinden(n): # Hier wordt een functie aangemaakt voor de ontbinding van het getal
    factoren = [] # Vervolgens wordt er een lijst aangemaakt voor de priemfactoren
    deler = 2 # Er wordt een variabele aangemaakt voor de 'deler' en toegewezen met 2

    while n > 1: # Met een while loop wordt gekeken of het nummer groter is dan 1
        while n % deler == 0: # Vervolgens wordt met de tweede while loop gekeken of de rest na deling van het getal 'n' gelijk is aan 0
            factoren.append(deler) # de 'deler' wordt toegevoegd aan de lijst 'factoren'
            n = n // deler # Het resultaat van de gehele deling (integer division) (van 'n' door de 'deler') wordt aan 'n' toegewezen
        deler += 1 # De 'deler' wordt verhoogd met 1

    return factoren # De waarde van de functie 'factoren' wordt terug gegeven aan het programma

num = int(input("Vul een getal: ")) # Vraag de gebruiker om een getal in te voeren
factoren = getalOntbinden(num) # Lijst factoren wordt gevuld en berekend met de functie 'getalOntbinden' door middel van het ingevoerde getal 'num'
print("De priemfactoren van", num, "zijn:", factoren) # Het resultaat wordt op het scherm getoond