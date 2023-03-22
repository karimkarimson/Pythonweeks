import random
randzahl=random.randint(0, 9)
trycount=1
def zraten(guess):
    if int(guess) == randzahl:
        print("WoW Treffer! & Du hast nur {} versuche gebraucht!".format(str(trycount)))
        exit()
    elif int(guess) < randzahl:
        print("Knapp vorbei, vielleicht nochmal hoeher schätzen")
    else:
        print("Knapp vorbei, vielleicht nochmal niedriger schätzen")
while True:
    print("Versuch Nummer: " + str(trycount))
    rzahl = input("Errate die Zahl zwischen 0 und 9: ")
    zraten(rzahl)
    trycount += 1