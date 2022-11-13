import random
comp = random.randint(0, 100)
sayac = 0
tutulansayi = -1
while tutulansayi != comp:
    tutulansayi = int(input("bilgisayar 0 ile 100 arası bir sayı tuttu onu tahmin et:"))
    print("Daha " + ("büyük" if tutulansayi < comp else "küçük") + " yazmalısın")
    sayac += 1
print("Tebrikler " + str(sayac) + " seferde buldunuz.")