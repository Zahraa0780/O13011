import random


def heittele_noppaa(tahkojen_maara):
    maksimisilmaluku = int(input("Syötä nopan maksimisilmäluku: "))

    while True:
        silmaluku = random.randint(1, tahkojen_maara)
        print("Heitit noppaa ja sait silmäluvun:", silmaluku)
        if silmaluku == maksimisilmaluku:
            break


heittele_noppaa(21)
