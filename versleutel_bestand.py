# Auteur: Tyrel Schrader
# Bestand: versleutel_bestand.py
# Beschrijving: Dit programma bezit een functie voor het op een zeer primitieve manier van versleutelen van een bestand: het omdraaien van alle bits (dus een 0 wordt 1, en andersom)
# Python versie: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Datum laatst aangepast: 02-04-2024 13:52

def encrypt_file(filename, encryptedfilename):
    # Open bestand met with as functie
    with open(filename, 'rb') as f, open(encryptedfilename, "wb") as ef:
    
        # Controleer of het bestand een geldig BMP bestand is
        signature = f.read(2)
        
        if signature != b'BM':
            raise RuntimeError("Bestand heeft geen geldige BMP-indeling")
    
        # Ophalen breedte en hoogte uit het bestand
        content = f.read()
        
        # Versleutelen van de inhoud met flip_bits() methode
        versleutelde_content = flip_bits(content)
        
        # Wegschrijven van versleutelde content in encryptedfilename
        ef.write(versleutelde_content)     
    
def flip_bits(a):
    b = b'\xFF'
    c = int.from_bytes(a, 'big') ^ int.from_bytes(b, 'big')
    return c.to_bytes(len(a), 'big')
    
# String aanmaken voor title versleutelde bestand
test_file = 'loi_logo.bmp'
insert_string = '_versleuteld'

# Voeg '_versleuteld' toe tussen test_file en .bestandsnaam
filename_parts = test_file.split('.')
encrypted_filename = filename_parts[0] + insert_string + '.' + filename_parts[1]

encrypt_file(test_file, encrypted_filename)