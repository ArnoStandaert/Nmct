#Maak een Python programma dat de leeftijd van een hond vertaalt naar een overeenkomstige
#leeftijd van een mens. Vraag eerst aan de gebruiker de leeftijd van zijn hond. Nadien print je
#een correcte boodschap af waarbij:

LeeftijdHond = input("Hoe oud je hond? \n")

if int(LeeftijdHond) < 0 :
    print("dit kan helemaal niet")

elif int(LeeftijdHond) ==1:
        print("uw hond is 14 mensenjaren oud")

elif int(LeeftijdHond) ==2:
        print("uw hond is 22 mensenjaren oud")

elif int(LeeftijdHond) >2:
        result = 22 + (int(LeeftijdHond) -2) *5
        print("uw hond is {0} jaren oud".format(result))