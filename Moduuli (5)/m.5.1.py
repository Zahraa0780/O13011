# Kysytään käyttäjältä arpakuutioiden lukumäärä
lukumaara = int(input("Syötä arpakuutioiden lukumäärä: "))

# Alustetaan muuttuja silmälukujen summaa varten
summa = 0

# Käytetään for-silmukkaa heittämään arpakuutiot ja laskemaan silmälukujen summa
for i in range(lukumaara):
    import random
    silmaluku = random.randint(1, 6)
    summa += silmaluku

# Tulostetaan silmälukujen summa
print("Silmälukujen summa on:", summa)