dagen = int(input("Geef hier het aantal dagen op:\n"))
uren = int(input("Geef het aantal uren op:\n"))
minuten = int(input("Geef het aantal minuten op:\n"))
seconden = int(input("Geef het aantal seconden op:\n"))

sec = (dagen * 24*60*60)+(uren*60*60)+(minuten*60)+seconden
print("Het aantal seconden bedraagt: {0}".format(sec))

