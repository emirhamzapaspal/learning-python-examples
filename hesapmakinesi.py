print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")
islem = int(input("Yapmak istediğiniz işlemi seçiniz (1,2,3,4):"))
if (islem ==1) or (islem ==2) or (islem ==3) or (islem ==4):
    sayi_1 = int(input("İlk sayıyı giriniz:"))
    sayi_2 = int(input("İkinci sayıyı girniz:"))
    if islem ==1:
        sonuc = sayi_1 + sayi_2
    elif islem == 2:
        sonuc = sayi_1 - sayi_2
    elif islem == 3:
        sonuc = sayi_1 * sayi_2
    elif islem == 4:
        sonuc = sayi_1 / sayi_2
    metin = "Seçtiğiniz işlemin sonucu: {}"
    print(metin.format(sonuc))
else:
    print("Yanlış bir seçim yaptınız")
