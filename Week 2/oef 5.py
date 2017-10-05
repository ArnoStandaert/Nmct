# Vraag de decimale score van een module aan de gebruiker. Print nadien af of hij/zij geslaagd is.
# Zorg ervoor dat de score correct afgerond wordt: indien het decimale gedeelte kleiner is dan 0,5
# wordt er naar beneden afgerond. In het andere geval wordt er naar boven afgerond. Print ook
# de afgeronde score af

score = input("geef uw score in ")

result = round(float(score),0)

if float(result) < 10:
    print("helaas, better luck next time")

else:
    print("great succ")