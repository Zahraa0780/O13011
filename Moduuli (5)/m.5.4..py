# Alustetaan tyhjä lista kaupungeille
kaupungit = []

# Kysytään käyttäjältä viiden kaupungin nimet
for i in range(5):
    kaupunki = input(f"Syötä kaupunki {i+1}: ")
    kaupungit.append(kaupunki)

# Tulostetaan kaupunkien nimet allekkain
print("Kaupunkien nimet:")
for kaupunki in kaupungit:
    print(kaupunki)