# Auteur: Tyrel Schrader
# Bestand: annuiteit.py
# Beschrijving: Dit programma berekent de annuïteit van een annuïteitenlening
# Python versie: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Datum laatst aangepast: 01-04-2024 14:40

def bereken_annuiteit(**kwargs): # Functie maakt gebruik van keyword arguments
    bedrag = kwargs['bedrag']
    interest = kwargs['interest']
    aantal_term = kwargs['aantal_term']
    
    # Berekening annuïteit
    rentevoet = interest/100
    bedrag_van_de_annuïteit = (rentevoet / (1 - (1 + rentevoet) ** -aantal_term)) * bedrag
    
    return round(bedrag_van_de_annuïteit, 2) # Het resultaat afronden naar 2 decimalen en terugsturen naar de client
    
    
    
bedrag = float(input("Geleend bedrag: "))
interest = float(input("Percentage maandelijkse rente: "))
aantal_term = int(input("Aantal maandelijkse termijnen: "))

print(bereken_annuiteit(bedrag=bedrag, interest=interest, aantal_term=aantal_term))