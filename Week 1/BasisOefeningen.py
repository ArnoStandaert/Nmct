x = 3
print(x)

x = 3   #integer
y = 3.0 #float
z = "3" #string

print(type(x))





#Vraag aan de gebruiker de basis en de hoogte van een driehoek op. Bereken nadien de oppervlakte en print deze nadien af.

basis = input("geef de basis van de driehoek op: ")
hoogte = input("geef de hoogte va de driehoek op: ")
oppervlakte = int(basis) * int(hoogte) / 2
print("de oppervlakte van de driehoek is " + oppervlakte)
