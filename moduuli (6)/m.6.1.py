import random

def heita_noppaa():
    return random.randint(1, 6)

def paaohjelma():
    silmaluku = heita_noppaa()
    while silmaluku != 6:
        print("Heitto:", silmaluku)
        silmaluku = heita_noppaa()
    print("Heitto:", silmaluku)

paaohjelma()
