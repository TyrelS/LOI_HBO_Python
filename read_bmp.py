# Auteur: Tyrel Schrader
# Bestand: read_bmp.py
# Beschrijving: Dit programma bezit een Python-functie die als argument de naam van een bestand heeft en een tuple teruggeeft met daarin de breedte en hoogte van de afbeelding in een aantal pixels
# Python versie: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Datum laatst aangepast: 02-04-2024 13:11

import struct

def read_bmp_height_width(filename):
    # Open bmp voor lezen
    f = open(filename, 'rb')
    
    # Controleer of het bestand een geldig BMP bestand is
    signature = f.read(2)
    
    if signature != b'BM':
        raise RuntimeError("Bestand heeft geen geldige BMP-indeling")

    # Ophalen breedte en hoogte uit het bestand
    f.seek(44) # bestandspointer verplaatsen naar InfoHeader width
    width = f.read(4)
    f.seek(4,1)
    height = f.read(4)    
    
    # Converteren van Little-Endian (4 byte formaat) naar long int
    converted_width = struct.unpack('<L',width)[0]
    converted_height = struct.unpack('<L',height)[0]
    
    # Breedte en hoogte stoppen in tpl_hoogte_breedte
    tpl_hoogte_breedte = (converted_width, converted_height)
    
    # Bestand ook weer netjes afsluiten
    f.close()
    
    return tpl_hoogte_breedte
    
test_file = 'loi_logo.bmp'
print(read_bmp_height_width(test_file))