numList = []
listing = True
while listing :
    value = input("Please enter a number to add to the list or q to end loading the list: ")
    if value == "q":
        listing = False
    else:
        numList.append(int(value))
numList.sort()
print("Die groesste Nummer ist: " + str(numList[-1]))
print("Die kleinste Nummer ist: " + str(numList[0]))
print("Hier sind die Nummern geordnet von der kleinsten zur groeßten: ")
print(numList)