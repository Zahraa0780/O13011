# Alustetaan tyhjä lista luvuille
luvut = []

# Kysytään käyttäjältä lukuja, kunnes tyhjä merkkijono syötetään
while True:
    syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")
    if syote == "":
        break
    luku = int(syote)
    luvut.append(luku)

# Lajitellaan luvut suuruusjärjestykseen käänteisesti
luvut.sort(reverse=True)

# Tulostetaan viisi suurinta lukua
print("Viisi suurinta lukua:")
for i in range(5):
    if i < len(luvut):
        print(luvut[i])