import math
import time
n = int(input("Bitte gebe an bis zu welcher Zahl die Primzahlen gesucht werden sollen: "))
# benchmark
start = time.time()
# liste der laenge n, in der alle Werte erstmal als False anzunehmen sind. 
# n+1 da der Index bei 0 anfaengt
# uns interessieren ab jetzt die Indexe und nicht deren Inhalt!
prim = [0] * (n+1)
# nun werden wir Primzahlen als True umaendern
# 0 und 1 sind Primzahlen und werden hier schon als True gesetzt
prim[0] = 1
prim[1] = 1
# Die hoechste anzunehmende Zahl ist ca die Wurzel n, alles was groesser als Wurzel n wird außerhalb unseres Rahmens n liegen.
for zahl in range(2, int(math.sqrt(n))+1):
    # ist die zahl eine Primzahl?
    if prim[zahl] == 0:
        # Wenn ja, dann bilde vielfache dieser Zahl mit Zahlen im Rahmen n/i da wir nicht unnötig große Zahlen nehmen müssen / im Rahmen bleiben wollen.
        for kleinereprimzahlen in range(2, int(n/zahl)+1):
            prim[zahl * kleinereprimzahlen] = 1

# und nun hole alle True Primzahlen aus der Liste
for zahl in range(2, n+1):
    if prim[zahl] == 0:
        print(zahl, end = ", ")

end = time.time()
print("\n Benchmark: ", end - start, " sekunden")


''' 
Pseudocode:
algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
                set A[j] := false

    return all i such that A[i] is true.
'''