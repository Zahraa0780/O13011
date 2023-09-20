def karsi_parittomat(lista):
    karsittu_lista = [luku for luku in lista if luku % 2 == 0]
    return karsittu_lista

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu = karsi_parittomat(lista)
    print("Alkuperäinen lista:", lista)
    print("Karsittu lista:", karsittu)

main()
