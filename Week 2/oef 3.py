#Vraag aan de gebruiker wat zijn geboortejaar is. Indien hij nog geen 18 is, print dan ook een
#gepaste melding af.

geboortejaar = input("Hoe oud ben je \n")

if int(geboortejaar) < 18:
    print("klein kind")
