sec = int(input("Geef het aantal seconden in:\n"))

dagen = int(sec / 86400)
sec -= dagen * 86400
uren = int(sec / 3600)
sec -= uren * 3600
minuten = int(sec / 60)
sec -= minuten * 60
seconden = int(sec % 60)


print("d:h:m:s -> {0}:{1}:{2}:{3}".format(dagen, uren, minuten, seconden))