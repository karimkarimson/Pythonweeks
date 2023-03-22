import datetime
def zvokale(text):
    charzahl = 0
    for chars in text:
        if chars == "a" or chars == "e" or chars == "i" or chars == "o" or chars == "u":
            charzahl += 1
        else:
            continue
    print("In deiner Eingabe gab es {} Vokale".format(str(charzahl)))
    datum = datetime.datetime.now()
    with open("Anzahl_Vokale.txt", "a") as datei:
        datei.write("\nEingabe am: " + str(datum))
        datei.write("\nIn dieser Eingabe gab es {} Vokale".format(str(charzahl)))
eingabe = input("Hallo, bitte gebe eine Zeichenkette ein und ich zähle die Vokale: ")
zvokale(eingabe)