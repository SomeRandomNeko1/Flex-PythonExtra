bestand=open("klasgenoten.txt", "r")

for line in bestand.readlines():
    print(line.rstrip())