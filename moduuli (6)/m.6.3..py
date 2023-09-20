def muunna_gallonoiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

while True:
    gallonat = float(input("Syötä bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))
    if gallonat < 0:
        break
    litrat = muunna_gallonoiksi(gallonat)
    print("Vastaaava litramäärä on:", litrat)
