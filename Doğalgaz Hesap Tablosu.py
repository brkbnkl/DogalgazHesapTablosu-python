import time

for _ in range(17):

    print("""
******************************
Doğalgaz Hesap Tablosu
******************************
1.Kombi Seçimi\n2.Kalorifer Tesisatı Seçimi\n3.Sıcak Su Tesisatı Seçimi\n4.Doğalgaz Tesisatı Seçimi\n5.Radyatör Seçimi\n6.Radyatör Vanası Seçimi\n7.Termostatik Vana Seçimi\n8.Oda Termostatı Seçimi\n9.Kombi Dolabı Seçimi
10.Havlupan Seçimi\n11.Baca Uzatması Seçimi\n12.Baca Dirseği Seçimi\n13.Cam-Menfez Seçimi\n14.Elektrik Tesisatı Seçimi\n15.İşçilik Seçimi \n16.Firma Gideri Seçimi\n17.Extra İşçilik Seçimi \nÇIKIŞ İÇİN 'Q' YA BASINIZ...
******************************""")

    seçim = input("İşlemi Seçiniz:")
    print("*****************************")

    if seçim == "q":
        print("Çıkış Yapılıyor...")
        quit()
    elif seçim == "1":
        print("Kombinizi Seçiniz:")
        print("*****************************")
        while True:
            kombi_fiyat = input("1)Bosch Condence 2500(24kW)\n2)Bosch Condence 2200i(24kW)\n3)ECA Citius Premix(24kW)\n4)ECA Calora Premix(24kW)\n5)ECA Proteus Premix(24kW)\n6)ECA Confeo Premix(24kW)\n7)Airfell Digifel Premix(23kW)\n8)Yok\n")
            if kombi_fiyat == "1":
               kombi_fiyat = 9000
               print("Kombi Seçimi Yapıldı")
               break
            elif kombi_fiyat == "2":
               kombi_fiyat = 9000
               print("Kombi Seçimi Yapıldı")
               break
            elif kombi_fiyat == "3":
               kombi_fiyat = 8000
               print("Kombi Seçimi Yapıldı")
               break
            elif kombi_fiyat == "4":
               kombi_fiyat = 8800
               print("Kombi Seçimi Yapıldı")
               break
            elif kombi_fiyat == "5":
               kombi_fiyat = 9700
               print("Kombi Seçimi Yapıldı")
               break
            elif kombi_fiyat == "6":
               kombi_fiyat = 11100
               print("Kombi Seçimi Yapıldı")
               break
            elif kombi_fiyat == "7":
               kombi_fiyat = 7000
               print("Kombi Seçimi Yapıldı")
            elif kombi_fiyat == "8":
               kombi_fiyat = 0
               print("Kombi Seçilmeden devam ediliyor...")
               break
            else:
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "2":
        print("Kalorifer Tesisatınızı Seçiniz:")
        print("*****************************")
        while True:
            kalorifer_fiyat = input("1)Komple Tesisat\n2)Kısa Öteleme\n3)Uzun Öteleme\n4)Hazır Tesisat\n")
            if kalorifer_fiyat == "1":
                kalorifer_fiyat = 1500
                print("Kalorifer Tesisatı Seçimi Yapıldı")
                break
            elif kalorifer_fiyat == "2":
                kalorifer_fiyat = 250
                print("Kalorifer Tesisatı Seçimi Yapıldı")
                break
            elif kalorifer_fiyat == "3":
                kalorifer_fiyat = 400
                print("Kalorifer Tesisatı Seçimi Yapıldı")
                break
            elif kalorifer_fiyat == "4":
                kalorifer_fiyat = 0
                print("Kalorifer Tesisatı Seçilmeden devam ediliyor...")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "3":
        print("Sıcak Su Tesisatınızı Seçiniz:")
        print("*****************************")
        while True:
            sicak_su_fiyat = input("1)Hazır\n2)Çekilecek\n")
            if sicak_su_fiyat == "1":
                sicak_su_fiyat = 0
                print("Sıcak Su Tesisatı Seçildi")
                break
            elif sicak_su_fiyat == "2":
                sicak_su_fiyat = 250
                print("Sıcak Su Tesisatı Seçildi")
                break
            else:
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "4":
        print("Doğalgaz Tesisatı Tipini Seçiniz:")
        print("*****************************")
        while True:
            dogalgaz_fiyat = input("1)Çelik Boru Tesisat\n2)Esnek Boru Tesisat\n3)Yok\n")
            if dogalgaz_fiyat == "1":
               dogalgaz_fiyat = 2000
               print("Doğalgaz Tesisatı Seçildi")
               break
            elif dogalgaz_fiyat == "2":
               dogalgaz_fiyat = 4000
               print("Doğalgaz Tesisatı Seçildi")
               break
            elif dogalgaz_fiyat == 3:
               dogalgaz_fiyat = 0
               print("Doğalgaz Tesisatı Seçilmeden devam ediliyor...")
               break
            else:
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "5":
        print("Radyatör Markasını Seçiniz:")
        print("*****************************")
        while True:
            radyator_fiyat = input("1)ECA Radyatör\n2)Warmhaus Radyatör\n3)Yok\n")
            if radyator_fiyat == "1":
               metraj = float(input("Metraj Giriniz:"))
               radyator_fiyat = metraj * 1250
               print("Radyatör Seçildi")
               break
            elif radyator_fiyat == "2":
               metraj = float(input("Metraj Giriniz:"))
               radyator_fiyat = metraj * 1100
               print("Radyatör Seçildi")
               break
            elif radyator_fiyat == "3":
               radyator_fiyat = 0
               print("Radyatör Seçilmeden devam ediliyor...")
               break
            else:
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim =="6":
        print("Radyatör Vana Markasını Seçiniz:")
        print("*****************************")
        while True:
            vana_fiyat = input("1)ECA\n2)Kalde\n3)Yok\n")
            if vana_fiyat == "1":
                adet = int(input("Adet Giriniz:"))
                vana_fiyat = adet * 50
                print("Radyatör Vanası Seçildi")
                break
            elif vana_fiyat == "2":
                adet = int(input("Adet Giriniz:"))
                vana_fiyat = adet * 35
                print("Radyatör Vanası Seçildi")
                break
            elif vana_fiyat == "3":
                vana_fiyat = 0
                print("Radyatör Vanası Seçilmeden devam ediliyor...")
                break
            else:
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "7":
        print("Termostatik Vana Markasını Seçiniz:")
        print("*****************************")
        while True:
            termostatik_vana_fiyat = int(input("1)ECA\n2)Danfoss\n3)Yok\n"))
            if termostatik_vana_fiyat == 1:
                adet = int(input("Adet Giriniz:"))
                termostatik_vana_fiyat = adet * 100
                print("Termostatik Vana Seçildi")
                break
            elif termostatik_vana_fiyat == 2:
                adet = int(input("Adet Giriniz:"))
                termostatik_vana_fiyat = adet * 150
                print("Termostatik Vana Seçildi")
                break
            elif termostatik_vana_fiyat == 3:
                termostatik_vana_fiyat = 0
                print("Termostatik Vana Seçilmeden devam ediliyor...")
                break
            else:
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "8":
        print("Oda Termostatını Seçiniz:")
        print("*****************************")
        termostat_fiyat = int(input("1)Bosch on/off Termostat\n2)Bosch Kablosuz Termostat\n3)ECA Kablosuz Termostat\n4)Yok\n"))
        while True:
            if termostat_fiyat == 1:
                termostat_fiyat = 300
                print("Oda Termostatı Seçildi")
                break
            elif termostat_fiyat == 2:
                termostat_fiyat = 1000
                print("Oda Termostatı Seçildi")
                break
            elif termostat_fiyat == 3:
                termostat_fiyat = 350
                print("Oda Termostatı Seçildi")
                break
            elif termostat_fiyat == 4:
                termostat_fiyat = 0
                print("Oda Termostatı Seçilmeden devam ediliyor...")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "9":
        print("Kombi Dolabını Seçiniz:")
        print("*****************************")
        dolap_fiyat = int(input("1)Var\n2)Yok\n"))
        while True:
            if dolap_fiyat == 1:
                dolap_fiyat = 300
                print("Kombi Dolabı Seçildi")
                break
            elif dolap_fiyat == 2:
                dolap_fiyat = 0
                print("Kombi Dolabı Seçildi")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "10":
        print("Havlupan Tipi Seçiniz:")
        print("*****************************")
        havlupan_fiyat = int(input("1)Var\n2)Yok\n"))
        while True:
            if havlupan_fiyat == 1:
                havlupan_fiyat = 250
                print("Havlupan Seçildi")
                break
            elif havlupan_fiyat == 2:
                havlupan_fiyat = 0
                print("Havlupan Seçildi")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "11":
        print("Baca Uzatması Seçiniz:")
        print("*****************************")
        uzatma_fiyat = int(input("1)1Metre\n2)50Cm\n3)Yok\n"))
        while True:
            if uzatma_fiyat == 1:
                uzatma_fiyat = 200
                print("Baca Uzatması Seçildi")
                break
            elif uzatma_fiyat == 2:
                uzatma_fiyat = 100
                print("Baca Uzatması Seçildi")
                break
            elif uzatma_fiyat == 3:
                uzatma_fiyat = 0
                print("Baca Uzatması Seçilmeden devam ediliyor...")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "12":
        print("Baca Dirseği Seçiniz:")
        print("*****************************")
        dirsek_fiyat = int(input("1)90 Derece\n2)45 Derece\n3)Yok\n"))
        while True:
            if dirsek_fiyat == 1:
                dirsek_fiyat = 150
                print("Baca Dirseği Seçildi")
                break
            elif dirsek_fiyat == 2:
                dirsek_fiyat = 100
                print("Baca Dirseği Seçildi")
                break
            elif dirsek_fiyat == 3:
                dirsek_fiyat = 0
                print("Baca Dirseği Seçilmeden devam ediliyor...")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "13":
        print("Cam-Menfez Tipi Seçiniz:")
        print("*****************************")
        cam_fiyat = int(input("1)Var\n2)Yok\n"))
        while True:
            if cam_fiyat == 1:
                cam_fiyat = 50
                print("Cam-Menfez Seçildi")
                break
            elif cam_fiyat == 2:
                cam_fiyat = 0
                print("Cam-Menfez Seçilmeden devam ediliyor...")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "14":
        print("Elektrik Tipi Seçiniz:")
        print("*****************************")
        elektrik_fiyat = int(input("1)Var\n2)Yok\n"))
        while True:
            if elektrik_fiyat == 1:
                elektrik_fiyat = 50
                print("Elektrik Tesisatı Seçildi")
                break
            elif elektrik_fiyat == 2:
                elektrik_fiyat = 0
                print("Elektrik Tesisatı Seçilmeden devam ediliyor...")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "15":
        print("İşçilik Tipi Seçiniz:")
        print("*****************************")
        işçilik_fiyat = int(input("1)Komple\n2)Montaj\n3)Kombi-Gaz\n"))
        while True:
            if işçilik_fiyat == 1:
                işçilik_fiyat = 1000
                print("İşçilik Seçildi")
                break
            elif işçilik_fiyat == 2:
                işçilik_fiyat = 750
                print("İşçilik Seçildi")
                break
            elif işçilik_fiyat == 3:
                işçilik_fiyat = 650
                print("İşçilik Seçildi")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "16":
        print("Firma Gideri Tipi Seçiniz:")
        print("*****************************")
        firmagideri_fiyat = int(input("1)Var\n2)Yok\n"))
        while True:
            if firmagideri_fiyat == 1:
                firmagideri_fiyat = 500
                print("Firma Gideri Seçildi")
                break
            elif firmagideri_fiyat == 2:
                firmagideri_fiyat = 0
                print("Firma Gideri seçilmeden devam ediliyor...")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    elif seçim == "17":
        print("Extra İşçilik Tipi Seçiniz:")
        print("*****************************")
        extra_işçilik_fiyat = int(input("1)Var\n2)Yok\n"))
        while True:
            if extra_işçilik_fiyat == 1:
                extra_işçilik_fiyat = 300
                print("Extra İşçilik Seçildi")
                break
            elif extra_işçilik_fiyat == 2:
                extra_işçilik_fiyat = 0
                print("Extre İşçilik Seçilmeden devam ediliyor...")
                break
            else :
                print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

    else :

        print("Yanlış Seçim Yaptınız..Lütfen Tekrar Seçim Yapınız")

print("*****************************")
print("Maliyetler Toplanıyor...")
time.sleep(3)

rakam = int((kombi_fiyat + kalorifer_fiyat + sicak_su_fiyat + dogalgaz_fiyat + radyator_fiyat + vana_fiyat + termostatik_vana_fiyat + termostat_fiyat + dolap_fiyat + havlupan_fiyat + uzatma_fiyat + dirsek_fiyat + cam_fiyat + elektrik_fiyat + işçilik_fiyat + firmagideri_fiyat + extra_işçilik_fiyat) * 1.12)
kredi_karti = int(rakam * 1.07)
oniki_senet = int(rakam * 1.24)
onbes_senet = int(rakam * 1.30)
onsekiz_senet = int(rakam * 1.36)
print("Nakit: {} TL".format(rakam))
print("Kredi Kartı: {} TL".format(kredi_karti))
print("12 Ay Senet: {} TL".format(oniki_senet))
print("15 Ay Senet: {} TL".format(onbes_senet))
print("18 Ay Senet: {} TL".format(onsekiz_senet))