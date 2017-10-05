# Schrijf een functie met 4 parameters (a,b,c,d) die getallen voorstellen. De laatste 2 parameters
# hebben 0 als default-waarde. De functie geeft het resultaat van volgende berekening terug:
# a – b + c – d.

def rekenen(a,b,c=0,d=0):
    result = a - b + c - d
    print(result)

rekenen(1,2, 3, 4)

rekenen(b=2,a=1,d=4,c=3)

rekenen(1,2)