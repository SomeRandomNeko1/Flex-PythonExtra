import os
nieuwe_naam = input("Nieuwe bestandsnaam: ")

if len(nieuwe_naam) > 0:
    bestandsnaam = "demobestand.txt"
    huidige_map = os.getcwd()
    volledige_pad = os.path.join(huidige_map, bestandsnaam)
    nieuwe_volledige_pad = os.path.join(huidige_map, nieuwe_naam)
    print("Bestand wordt hernoemd naar: " + nieuwe_volledige_pad)
    os.rename(volledige_pad, nieuwe_volledige_pad)
    print("Bestand hernoemd")
else:
    print("Sorry, geen geldige invoer, einde programma")