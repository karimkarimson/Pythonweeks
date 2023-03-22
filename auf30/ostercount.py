import datetime
import time
def platzmacher(i):
    j = 0
    while j < i:
        print()
        j += 1
osterferien = datetime.datetime(2023, 4, 7, 0, 0, 0)
print("Die Osterferien fangen am {} an.".format(osterferien.strftime("%c")))
platzmacher(3)
print("Bitte warte 5 Sekunden")
print(" BEENDE DAS PROGRAMM DURCH DRUECKEN VON    strg + c   ")
time.sleep(1)
while True: 
        platzmacher(2)
        jetzt = datetime.datetime.now()
        zeitbisfrei = osterferien - jetzt
        # alle Sekunden bis Ostern geteilt durch SekProTag
        rtage = zeitbisfrei.total_seconds() / (60 * 60 * 24)
        # Uebrige Sekunden bis Ostern errechnen
        restSekifuerStunden = zeitbisfrei.total_seconds() % (60 * 60 * 24)
        # RestSekunden durch Stunden
        zeitinstunden = restSekifuerStunden / (60 * 60)
        # RestSekunden fuer Minuten errechnen
        restSekfuerMinuten = restSekifuerStunden % (60 * 60)
        # Restsekunden in Minuten
        zeitinminuten = restSekfuerMinuten / 60
        # Restsekunden fuer Sekunden
        zeitinsekunden = restSekfuerMinuten % 60
        print("Nur noch {} Tage und {} Stunden und {} Minuten und {} Sekunden bis zu den Osterferien!".format(int(rtage), int(zeitinstunden), int(zeitinminuten), int(zeitinsekunden)))
        time.sleep(1)