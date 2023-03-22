gimmenumber = input("bitte gebe eine natuerliche Zahl ein, deren Fakultaet du haben moechtest: ")
buffer = 1
counter = 0
result = 1
while counter < int(gimmenumber):
    buffer *= result
    result += 1
    counter += 1
print(buffer)