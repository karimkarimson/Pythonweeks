kleiderschrank=["hose","t-shirt", "kleid"]
kommode=["schuhe", "socken", "muetzen"]
print(kleiderschrank[0])
print(kleiderschrank[1])
print(kleiderschrank[2])
lkleid=len(kleiderschrank)
lkomm=len(kommode)
for i in range(lkleid):
    print(kleiderschrank[i])
kleiderschrank.append("handschuhe")
print(kleiderschrank[3])
for i in range(lkomm):
    kleiderschrank.append(kommode[i])
lkleid=len(kleiderschrank)
for i in range(lkleid):
    print(kleiderschrank[i])