not_1 = int(input("Birinci sınav notunuzu giriniz:"))
not_2 = int(input("İkinci sınav notunuzu giriniz:"))
ortalama = (not_1 + not_2) / 2
if ortalama < 45:
    print("Başarısız")
elif ortalama >= 45 and ortalama < 55:
    print("Geçer")
elif ortalama >= 55 and ortalama < 70:
    print("orta")
elif ortalama >= 70 and ortalama < 85:
    print("iyi")
elif ortalama >= 85 and ortalama <= 100:
    print("Çok iyi")