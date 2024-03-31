# Auteur: Tyrel Schrader
# Bestand: check_winner_tic_tac_toe.py
# Beschrijving: Dit programma controleert welke speler de winner is van een potje boter, kaas en eieren.
# Python versie: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Datum laatst aangepast: 01-04-2024 01:57

def check_winner(m):
    # Controleer horizontale rijen
    for row in m:
        if len(set(row)) == 1 and row[0] != ' ': # Controleer of alle elementen in de rij hetzelfde zijn door een set van de rij te maken.
            return row[0]                        # Als alle elementen hetzelfde zijn, zal de set slechts één element bevatten, omdat sets geen duplicaten bevatten.
                                                 # Dus als de lengte van de set gelijk is aan 1, betekent dit dat alle elementen in de rij hetzelfde zijn.
                                                 # Dit deel controleert of het eerste element van de rij niet leeg is. Als het eerste element niet leeg is, betekent dit dat de rij niet alleen uit lege cellen bestaat.                                               
    # Controleer verticale kolommen
    for col in range(3):
        if len(set(m[row][col] for row in range(3))) == 1 and m[0][col] != ' ': # Dit deel maakt een set van alle elementen in de opgegeven kolom
            return m[0][col]                                                    # De generator expressie (m[row][col] for row in range(3)) levert alle elementen op van de kolom met index 'col'
                                                                                # Wanneer de lengte van de set weer gelijk is aan 1, betekent dit dat alle elementen in de rij hetzelfde zijn.
    # Controleer diagonale lijnen
    if m[0][0] == m[1][1] == m[2][2] != ' ': # Controleer of de diagnale lijnen gelijk staan aan 3x 'X' of 3x 'O'
        return m[0][0]
    if m[0][2] == m[1][1] == m[2][0] != ' ':
        return m[0][2]

    return None

# Vraag de gebruiker naar invoer
print("Om de winner te achterhalen vul hieronder de rijen in. Scheidt de invoer met komma's. Bijvoorbeeld: 'X, O, X'")    
rij1 = str(input("Vul de eerste rij in: ")).upper()
rij2 = str(input("Vul de tweede rij in: ")).upper()
rij3 = str(input("Vul de derde rij in: ")).upper()

# Controleer of elke rij drie letters bevat
if len(rij1.replace(",", "").replace(" ", "")) != 3 or len(rij2.replace(",", "").replace(" ", "")) != 3 or len(rij3.replace(",", "").replace(" ", "")) != 3:
    print("Fout: Elke rij moet precies drie letters bevatten, gescheiden door komma's en spaties als in het voorbeeld.")
    exit()
if "X" not in rij1 and "O" not in rij1 or "X" not in rij2 and "O" not in rij2 or "X" not in rij3 and "O" not in rij3:
    print("Fout: Elke rij moet de letter 'X' of 'O' bevatten.")
    exit()
    
# Splits de strings op komma's en verwijder eventuele spaties
rij1_list = rij1.split(',')
rij2_list = rij2.split(',')
rij3_list = rij3.split(',')

# Strip eventuele spaties aan het begin en einde van elk element
rij1_list = [element.strip() for element in rij1_list]
rij2_list = [element.strip() for element in rij2_list]
rij3_list = [element.strip() for element in rij3_list]

# Matrix voor het bord aanmaken
bord = [rij1_list, rij2_list, rij3_list]

winner = check_winner(bord)
if winner:
    print(f"De winnaar is {winner}!")
else:
    print("Het is gelijkspel.")