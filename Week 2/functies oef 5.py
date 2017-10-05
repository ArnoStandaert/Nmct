# Schrijf een functie die een maandnummer binnenkrijgt. Controleer of het getal tussen 1 en 12
# ligt. Geef de corresponderende maand terug. Indien buiten het interval, geef je een
# foutboodschap terug. Test de functie met meerdere maandnummers
import datetime

def Maand(x="0"):
    month = datetime.date(1900, x, 1).strftime('%B')
    print(month)

Maand(5)
