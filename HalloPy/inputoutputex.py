wordList = []
listing = True
while listing :
    value = input("Please enter a word to add to the list or 99 to end loading the list: ")
    if value == "99":
        listing = False
    else:
        wordList.append(str(value))
# sorted(wordList)
swordList = sorted(wordList)
swordList.reverse()
print(swordList)