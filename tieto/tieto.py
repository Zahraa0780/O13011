import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='airport',
         user='root',
         password='12345',
         autocommit=True
         )


pisteet = 0
list = []
def haeKentat():
    sql = "select name from country where isCountry = 'yes'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            #print(rivi[0])
            list.append(rivi[0])
    return

print("Tervetula, lentoasema !")
print("Valitse mihin haluaa matkustaa?")
haeKentat()
while True:
    valtset= input("Valtsen MAA: ")
    if valtset in list and pisteet < 6:
        print("Sait pisteen")
        pisteet += 1
        list.remove(valtset)
    elif pisteet == 6:
        print("Voitit!")
        break
    else:
        print("väärin valitse, yritä uudelleen.")



#print("1.ruotsi")
#print("2.saksa")
#print("3.ranska")
#print("4.norja")
#print("5.tanska")
#print("6.italia")
#print("7.espanja")
#print("8.venäjä")
#print("9.suomi")
#print("10.belgia")