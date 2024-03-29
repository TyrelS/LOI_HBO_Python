# Auteur: Tyrel Schrader
# Bestand: benader_integraal.py
# Beschrijving: Dit programma berekent voor elke mogelijke functie f een benadering van de integraal op het interval [a,b], verdeeld in n partjes.
# Python versie: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Datum laatst aangepast: 29-03-2024 20:27

def riemann_som(functie, a, b, n):
    breedte_subinterval = (b - a) / n  # Bereken de breedte van elk subinterval

    riemannsom = 0
    for i in range(n):
        middelpunt_subinterval = a + (i + 0.5) * breedte_subinterval  # Middelpunt van het subinterval
        hoogte_subinterval = functie(middelpunt_subinterval)
        oppervlakte_rechthoek = hoogte_subinterval * breedte_subinterval
        riemannsom += oppervlakte_rechthoek

    return riemannsom

# Functie om te integreren
def f(x):
    return x**2

# Gebruiker invoer
a = float(input("Voer de ondergrens a in: "))
b = float(input("Voer de bovengrens b in: "))
n = int(input("Voer het aantal subintervallen n in: "))

resultaat = riemann_som(f, a, b, n)
print("De Riemannsom is:", resultaat)

# Testen met een lambda-functie
resultaat2 = riemann_som(lambda x: x**2, -3, 3, 300)
print("De Riemannsom (uit test met een lambda functie) is:", resultaat2)