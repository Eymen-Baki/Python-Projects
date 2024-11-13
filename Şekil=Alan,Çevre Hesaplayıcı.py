import math
pi = 3.14

while True:
    secim=input("birini seçin:\n1.üçgen\n2.dikdörtgen\n3.daire\n4.çıkış\n")
    
    if secim=="1":
        taban=float(input("taban girinz:"))
        yükseklik=float(input("yükseklik giriniz:"))
        alan=(taban*yükseklik) / 2
        kenar1=float(input("kenar1 giriniz:"))
        kenar2=float(input("kenar2 giriniz:"))
        kenar3=float(input("kenar3 giriniz:"))
        cevre=kenar1+kenar2+kenar3
        print(f"Üçgenin Alanı :: ",({alan}))
        print(f"Üçgenin Çevresi:: ",({cevre}))
        continue

    elif secim=="2":
        kisakenar=float(input("kisakenar giriniz: "))
        uzunkenar=float(input("uzunkenar giriniz:"))
        alan1= kisakenar*uzunkenar
        cevre1=kisakenar+kisakenar+uzunkenar+uzunkenar
        print(f"Dikdörtgenin Alanı :: ",({alan1}))
        print(f"Dikdörtgenin Çevresi :: ",({cevre1}))
        continue

    elif secim=="3":
        yaricap=float(input("Yaricap Giriniz :: "))
        alan2= math.pi * yaricap ** 2
        cevre2= 2 * math.pi * yaricap
        print(f"Dairenin Alanı :: ",({alan2}))
        print(f"Dairenin Çevresi :: ",({cevre2}))
        continue
        
    elif secim=="4":
        print("program sonlanıyor...")
        break
    
    else:
        print("Geçersiz seçim! Lütfen 1, 2, 3 veya 4 giriniz.")
        continue