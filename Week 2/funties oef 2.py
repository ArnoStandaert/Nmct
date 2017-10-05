# Schrijf een functie ‘printWelkom’ die twee strings als parameters heeft: naam en groep. Zorg
# ervoor dat de parameter groep een defaultwaarde ‘1NMCT1’ krijgt. Print een welkomstbericht af
# waarin naam & groep vermeld staan.
# Test de functie voldoende (zowel met 1 als 2 argumenten)


def printWelkom(naam, richting="1NMCT1"):
    print("welkom {0} in de richting {1}".format(naam,richting))

printWelkom("gary")

