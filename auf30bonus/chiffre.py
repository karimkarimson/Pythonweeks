# verschluesseln
def verschluessel(inhalt, key):
    geheimtext = ""
    # nun gehe jedes Zeichen in Inhalt durch
    for zeichen in inhalt:
        print(zeichen, end = " ") # ist das Zeichen lesbar?
        # mit Buchstaben arbeiten
        if not zeichen.isalpha(): 
            geheimtext += zeichen
            continue
        else:
            if zeichen.islower():
                geheimtext += chr((ord(zeichen) - ord("a") + key) % 26 + ord("a"))
            if zeichen.isupper():
                geheimtext += chr((ord(zeichen) - ord("A") + key) % 26 + ord("A"))
    return geheimtext

# entschluesseln, umgekehrt herum
def entschluessel(inhalt, key):
    klartext = ""
    for zeichen in inhalt:
        print(zeichen, end = " ") # wieder sichergehen ob das Zeichen lesbar ist
        if not zeichen.isalpha():
            klartext += zeichen
            continue
        else:
            if zeichen.islower():
                klartext += chr((ord(zeichen) - ord("a") - key + 26) % 26 + ord("a"))
            if zeichen.isupper():
                klartext += chr((ord(zeichen) - ord("A") - key + 26) % 26 + ord("A"))
    return klartext

dateiname = input("Gib den Dateinamen oder Pfad bis inkl. Dateinamen an: ")
dateiraus = input("Gib den Namen der Datei die geschrieben werden soll an: ")
output_file = open(dateiraus, "w+") # öffne bzw erstelle Datei zum Lesen und Schreiben

try:
    with open(dateiname, "r") as datei:
        inhalt = datei.read()
        print("Inhalt der Datei: ", inhalt)
        option = int(input("Waehle eine Option: \n1.Verschluessel\n2.Entschluessel\n0.Ende\n"))
        if option == 1:
            key = int(input("Gib die Schluessel-Zahl zum Verschluesseln ein: "))
            versch = verschluessel(inhalt, key)
            output_file.write(versch)
        if option == 2:
            key = int(input("Gib die Schluessel-Zahl zum entschluesseln ein: : "))
            klart = entschluessel(inhalt, key)
            output_file.write(klart)
        if option == 0:
            exit()
except:
    print("Datei existiert nicht: ", dateiname)

output_file.close()

'''                   Encryption            |           Decryption             '''
''' Lowercase:	(ch - 'a' + key) % 26 + 'a' | (ch - 'a' - key + 26) % 26 + 'a' '''
''' Uppercase:	(ch - 'A' + key) % 26 + 'A' | (ch - 'A' - key + 26) % 26 + 'A' '''
'''
    https://en.wikipedia.org/wiki/List_of_Unicode_characters
Beispiel:
    verschluessel 'abcd' mit key = 7
a = 97 als Unicode-Wert
a -> (97 - 97 + 7) % 26 + 97 => 7 + 97 = 104 -> h
b -> (98 - 97 + 7) % 26 + 97 => 8 + 97 = 105 -> i
c -> (99 - 97 + 7) % 26 + 97 => 9 + 97 = 106 -> j
d -> (100 - 97 + 7) % 26 + 97 => 10 + 97 = 107 -> k
                    
    'abcd' -> 'hijk'

'xyz' mit key = 12
x -> (120 - 97 + 12) % 26 + 97 => 9 + 97 = 106 -> j
y -> (121 - 97 + 12) % 26 + 97 => 10 + 97 = 107 -> k
z -> (122 - 97 + 12) % 26 + 97 => 11 + 97 = 108 -> l
'''