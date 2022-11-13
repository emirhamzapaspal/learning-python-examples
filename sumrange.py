a = int(input("Kaça kadar olsun?"))
dizi = range(0, a)
toplam = 0
for sayi in dizi:
    toplam = toplam + sayi
print("Toplam " + str(toplam))