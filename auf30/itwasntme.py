def fragen (frage):
    print(frage)
    antwort = input("Bitte antworte mit Ja oder Nein: ")
    return antwort.upper()
if fragen("Funktioniert das System? ") == "JA":
    print("Fummel nicht dran herum!")
    print("Alles ist gut!")
    exit()
else:
    if fragen("Bist du Schuld? ") == "JA":
        print("Du Idiot!")
        if fragen("Hat es jemand gemerkt? ") == "JA":
            print("Du bist am Arsch!")
            if fragen("Kannst du einem Anderen die Schuld zu schieben?") == "JA":
                print("Keine Sorge, jemand anderes ist am Arsch!")
                exit()
            else:
                print("Du bist wirklich am Arsch!!")
                exit()
        else:
            print("Man wird dich nie finden")
            exit()
    else:
        print("Dich trifft es nicht")
        exit()