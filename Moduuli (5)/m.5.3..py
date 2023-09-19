# Funktio tarkistamaan, onko luku alkuluku
def on_alkuluku(luku):
    if luku <= 1:
        return False
    for i in range(2, luku):
        if luku % i == 0:
            return False
    return True

# Kysytään käyttäjältä luku
luku = int(input("Syötä kokonaisluku: "))

# Tarkistetaan, onko luku alkuluku ja tulostetaan vastaus
if on_alkuluku(luku):
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")