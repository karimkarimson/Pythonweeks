import random
wortliste = ["ziege", "katze", "seehund", "pferd", "faultier", "lachs", "amsel", "kuckuck", "schaaf", "stier"]
#waehle Wort
wort = wortliste[random.randint(0, len(wortliste)-1)]
# erstelle liste mit Bindestrichen in Wortlaenge
guesslist = ['-'] * len(wort)
versuche = int(input("Gebe die maximale Anzahl an Versuchen ein, die Du haben moechtest: "))
# sollte der kommende Block nicht erfolgreich ausgefuehrt werden, greift der else-Block
for versuch in range(versuche):
    zeichen = input("Errate einen Buchstaben: ")
    for buchstabe in range(len(wort)):
        if zeichen.lower() == wort[buchstabe]:
            guesslist[buchstabe] = wort[buchstabe]
    # Zustand der zu erratenden Liste, join() verbindet alle Elemente zu einem String-""
    print("{} Anzahl Versuche: {} - Buchstabe: {}".format("".join(guesslist), versuch, zeichen))

    # if every x in guess not equal '-' it means that we got the word and we stop there
    if all(plaetze != "-" for plaetze in guesslist):
        print("{} Anzahl Versuche: {} - GEWONNEN !!!".format("".join(guesslist), versuch+1))
        break
else:
    print("{} Anzahl Versuche: {} - VERLOREN :(".format("".join(guesslist), versuche))
    
'''
Aufgabenblatt:
____ Anzahl Versuche: 0 - Buchstabe: a
____ Anzahl Versuche: 1 - Buchstabe: o
_o__ Anzahl Versuche: 2 - Buchstabe: e
_o_e Anzahl Versuche: 3 - Buchstabe: d
_ode Anzahl Versuche: 4 - Buchstabe: c
code Anzahl Versuche: 5 - GEWONNEN !!!
'''