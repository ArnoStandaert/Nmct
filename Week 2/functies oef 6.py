def geef_celcius(x):
    result = (x - 32) *5 /9
    print(result)

def geef_fahrenheit(x):
    result = (x * 9 /5) + 32
    print(result)

eenheid = input("welke eenheid gebruikt u? ")
temperatuur = input("geef temperatuur op ")

if eenheid == "c":
    geef_celcius(int(temperatuur))

else:
    geef_fahrenheit(int(temperatuur))
