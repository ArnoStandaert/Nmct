#Vraag een niet-decimaal getal aan de gebruiker. Bepaal of het opgegeven getal even of oneven
#is. Print een gepaste boodschap af.

NonDecimal = input("geef een niet-decimaal getal in")
result = int(NonDecimal) % 2

if result == 0:
    print("uw getal is even")
else:
    print("uw getal is oneven")
