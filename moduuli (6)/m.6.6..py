def laske_yksikkohinta(halkaisija, hinta):
    pinta_ala = 3.14159 * (halkaisija / 2) ** 2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

def main():
    halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Syötä ensimmäisen pizzan hinta (€): "))
    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)

    halkaisija2 = float(input("Syötä toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä toisen pizzan hinta (€): "))
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    print("Ensimmäisen pizzan yksikköhinta: {:.2f} €/m²".format(yksikkohinta1))
    print("Toisen pizzan yksikköhinta: {:.2f} €/m²".format(yksikkohinta2))

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat antavat samanlaisen vastineen rahalle.")

main()
