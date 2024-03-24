# Auteur: Tyrel Schrader
# Bestand: turtle_figuren.py
# Beschrijving: Dit programma toont figuren op het scherm 
# Python versie: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Datum laatst aangepast: 24-03-2024 22:16

import turtle
import time

# Teken een driehoek
hoek = 120
afstand = 400

turtle.pencolor( 'red' )
turtle.penup()
turtle.setposition(-200, -120)
turtle.pendown()
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)

# Pauzeer programma voor 2 seconden
time.sleep(2)

# Scherm leegmaken
turtle.clear()

#-----------------------------------------------

# Teken een ster
hoek = 144
afstand = 400

turtle.pencolor( 'red' )
turtle.penup()
turtle.setposition(0, 220)
turtle.pendown()

turtle.left(12)
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)

# Pauzeer programma voor 2 seconden
time.sleep(2)

# Scherm leegmaken
turtle.clear()

#-----------------------------------------------

# Teken een consolidatie grafiek
hoek = 144
afstand = 200

turtle.pencolor( 'red' )
turtle.penup()
turtle.setposition(-250, 120)
turtle.pendown()

turtle.right(180)
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)
turtle.right(hoek)
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)
turtle.right(hoek)
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)
turtle.right(hoek)
turtle.forward(afstand)
turtle.left(hoek)
turtle.forward(afstand)

# Pauzeer programma voor 2 seconden
time.sleep(2)

# Scherm leegmaken
turtle.clear()

#-----------------------------------------------

# Teken vierkant met 25 vierkanten er in
turtle.pencolor( 'red' )
turtle.penup()
turtle.setposition(-140, 150)
turtle.pendown()
turtle.right(72)

# Functie om een enkel vierkant te tekenen
def teken_vierkant():
    for i in range(4):
        turtle.forward(50)  # Lengte van elke zijde van het vierkant
        turtle.right(90)

# Functie om 25 vierkanten te tekenen
def teken_raster():
    for i in range(5):
        for i in range(5):
            teken_vierkant()
            turtle.forward(50)  # Ruimte tussen de vierkanten in een rij
        turtle.backward(250)  # Terugkeren naar de startpositie
        turtle.right(90)      # Draaien voor de volgende rij
        turtle.forward(50)    # Naar de volgende rij
        turtle.left(90)       # Terugdraaien naar de oorspronkelijke richting

# Tekenen van het raster
teken_raster()

# Pauzeer programma voor 2 seconden
time.sleep(2)

# Scherm leegmaken
turtle.clear()

#-----------------------------------------------

# Teken een cirkel
turtle.pencolor( 'red' )
turtle.penup()
turtle.setposition(0, -140)
turtle.pendown()

# Functie om een enkele cirkel te tekenen
def teken_cirkel():
    turtle.circle(150)  # Radius van de cirkel


# Tekenen van een enkele cirkel
teken_cirkel()

# Pauzeer programma voor 2 seconden
time.sleep(2)

# Scherm leegmaken
turtle.clear()

#-----------------------------------------------

# Teken een cirkel met daarin diagnonale lijnen en met vierkanten eromheen
turtle.pencolor( 'red' )
turtle.penup()
turtle.setposition(0, -140)
turtle.pendown()

# Functie om een enkele cirkel te tekenen
def teken_cirkel():
    turtle.circle(150)  # Radius van de cirkel


# Tekenen van een enkele cirkel
teken_cirkel()

# Functie om diagonale lijnen te tekenen
def teken_diagonale_lijnen():
    for i in range(24):
        turtle.penup()
        turtle.setposition(0, 10)
        turtle.pendown()
        turtle.forward(152)
        turtle.left(15)


# Tekenen van de diagonale lijnen
teken_diagonale_lijnen()

# Functie om vierkanten te tekenen
def teken_vierkanten():
    turtle.speed(10)
    turtle.penup()
    turtle.setposition(0, 10)
    turtle.pendown()
    
    for i in range(24):
        for i in range(4):
            turtle.forward(152)  # Lengte van elke zijde van het vierkant
            turtle.right(90)        
        turtle.left(15)


# Tekenen van de vierkanten
teken_vierkanten()

# Pauzeer programma voor 2 seconden
time.sleep(2)

# Scherm leegmaken
turtle.clear()

# Turtle verbergen en optie om af te sluiten aanbieden
turtle.hideturtle()
turtle.exitonclick()