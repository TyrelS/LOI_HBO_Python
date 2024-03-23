# Vraag de gebruiker om een getal in te voeren voor het tonen van de reeks Fibonacci
n = int(input("Vul een getal in voor de reeks Fibonacci: "))

count = 1
f_1 = 0 
f_2 = 1

# Toon de getallen van Fibonacci op het scherm
if n < 1:
    print("Foutmelding: getallen kleiner dan 1 zijn niet toegestaan!")
else:
    print(f_1,end="")
    count += 1
    while count < n:
        print(",",f_2,end="")
        #Getallen doorschuiven
        f_n = f_1 + f_2
        f_1 = f_2
        f_2 = f_n
        count += 1