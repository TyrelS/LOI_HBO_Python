# Auteur: Tyrel Schrader
# Bestand: bubble_sort_v2.py
# Beschrijving: Met dit programma wordt een lijst via de bubble_sortmethode gesorteerd en het resultaat opgeslagen in een nieuwe lijst
# Python versie: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Datum laatst aangepast: 02-04-2024 19:58

def bubble_sort(oude_lijst):
    nieuwe_lijst = oude_lijst[:]    # Maak een kopie van de oude lijst om de originele lijst niet te wijzigen
    n = len(nieuwe_lijst)           # Totaal aantal nummers opslaan in een variabele
    
    # Voor elke nummer in de lijst kijken of het nummer groter is dan zijn opvolger
    for i in range(n):              # Deze lus wordt gebruikt om de gehele lijst te doorlopen
        blnVerwisseld = False       # Boolean om bij te houden of er tijdens deze passage een wisseling heeft plaatsgevonden
        # De tweede lus wordt gebruikt om een paar elementen in de lijst met elkaar te vergelijken en van plaats te wisselen
        for j in range(n-i-1):      # Het doel van het gebruik van n-i-1 is om ervoor te zorgen dat er niet opnieuw door de hele lijst gelopen hoeft te worden
            if nieuwe_lijst[j] > nieuwe_lijst[j+1]:                                         # Wanneer een nummer groter is dan zijn opvolger
                nieuwe_lijst[j], nieuwe_lijst[j+1] = nieuwe_lijst[j+1], nieuwe_lijst[j]     # Wissel de plaatsen om
                blnVerwisseld = True    # Zet de boolean op True omdat er een wisseling heeft plaatsgevonden
        if not blnVerwisseld:           # Als er tijdens deze passage geen wisselingen zijn geweest
            break                       # Stop het sorteren, omdat de lijst al gesorteerd is

    return nieuwe_lijst

# Test de bubble_sort-functie
oude_lijst = [100, 12, 8, 55, 3, 2, 107, 9, 34]
nieuwe_lijst = bubble_sort(oude_lijst)

print("Oude lijst: ", oude_lijst)
print("Nieuwe lijst: ", nieuwe_lijst)