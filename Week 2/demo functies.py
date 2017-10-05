#demo functies
#hergebruiken code
#structuur in code

# naam = input("geef uw naam :")
# print("Welkom {0}".format(naam))
#
# nogEenNaam = input("geef uw naam : ")
# print("Welkom {0}".format(nogEenNaam))
#
#
# #code wordt herhaald -> functie nodig
#
# #functie in python
# def printNaam():
#     print("pol")
#     print("an")
#     print("miet")
#
# printNaam()

#best practice alle methoden samen definieren
#met parameters
# def printNaam(naam, richting="howest"):
#     print("Welcom {0} in de richting {1}".format(naam,richting))
#     print(naam)
#     toonWelkomsscherm(naam)
#
# def toonWelkomsscherm(naam):
#     print("welkom {0}".format(naam))
#
#
# printNaam("Henk", "nmct")
# printNaam(richting="energie",naam="rik")

# def vraagGegevensRechthoek():
#     lengte = int(input("geef lengte van de rechthoek :"))
#     breedte = int(input("geef breedte van de rechthoek"))

def berekenOppervlakteRechthoek():
    lengte = int(input("geef lengte van de rechthoek :"))
    breedte = int(input("geef breedte van de rechthoek"))
    oppervlakte = lengte * breedte
    return oppervlakte


berekenOppervlakteRechthoek()

print(berekenOppervlakteRechthoek.oppervlakte)
