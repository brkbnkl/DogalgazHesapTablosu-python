import time

fiyat_model_listesi = {1: {1: [9000, '1)Bosch Condence 2500(24kw)'],
                           2: [9000, '2)Bosch Condence 2200i(24kW)'],
                           3: [8000, '3)ECA Citius Premix(24kW)'],
                           4: [8800, '4)ECA Calora Premix(24kW)'],
                           5: [9700, '5)ECA Proteus Premix(24kW)'],
                           6: [11100, '6)ECA Confeo Premix(24kW)'],
                           7: [7000, '7)Airfell Digifel Premix(23kW)'],
                           8: [0, '8)Yok'],
                           'soru': 'Kombinizi Seçiniz:',
                           'cevap': 'Kombi Seçimi Yapıldı'},
                       2: {1: [1500, '1)Komple Tesisat'],
                           2: [250, '2)Kısa Öteleme'],
                           3: [400, '3)Uzun Öteleme'],
                           4: [0, '4)Hazır Tesisat'],
                           'soru': 'Kalorifer Tesisatınızı Seçiniz:',
                           'cevap': 'Kalorifer Tesisatı Seçimi Yapıldı'},
                       3: {1: [0, '1)Hazır'],
                           2: [250, '2)Çekilecek'],
                           'soru': 'Sıcak Su Tesisatınızı Seçiniz:',
                           'cevap': 'Sıcak Su Tesisatı Seçildi'},
                       4: {1: [2000, '1)Çelik Boru Tesisat'],
                           2: [4000, '2)Esnek Boru Tesisat'],
                           3: [0, '3)Yok'],
                           'soru': 'Doğalgaz Tesisatı Tipini Seçiniz:',
                           'cevap': 'Doğalgaz Tesisatı Seçildi'},
                       5: {1: [1250, '1)ECA Radyatör'],
                           2: [1100, '2)Warmhaus Radyatör'],
                           3: [0, '3)Yok'],
                           'soru': 'Radyatör Markasını Seçiniz:',
                           'cevap': ['Radyatör Markası Seçildi', 'Radyatör Markası Seçilmeden devam ediliyor...']},
                       6: {1: [50, '1)ECA'],
                           2: [35, '2)Kalde'],
                           3: [0, '3)Yok'],
                           'soru': 'Radyatör Vana Markasını Seçiniz:',
                           'cevap': ['Radyatör Vanası Seçildi', 'Radyatör Vanası Seçilmeden devam ediliyor...']},
                       7: {1: [100, '1)ECA'],
                           2: [150, '2)Danfoss'],
                           3: [0, '3)Yok'],
                           'soru': 'Termostatik Vana Markasını Seçiniz:',
                           'cevap': ['Termostatik Vanası Seçildi', 'Termostatik Vanası Seçilmeden devam ediliyor...']},
                       8: {1: [300, '1)Bosch on/off Termostat'],
                           2: [1000, '2)Bosch Kablosuz Termostat'],
                           3: [350, '3)ECA Kablosuz Termostat'],
                           4: [0, '4)Yok'],
                           'soru': 'Oda Termostatını Seçiniz:',
                           'cevap': 'Oda Termostatı Seçildi'},
                       9: {1: [300, '1)Var'],
                           2: [0, '2)Yok'],
                           'soru': 'Kombi Dolabını Seçiniz:',
                           'cevap': 'Kombi Dolabı Seçildi'},
                       10: {1: [250, '1)Var'],
                            2: [0, '2)Yok'],
                            'soru': 'Havlupan Tipi Seçiniz:',
                            'cevap': 'Havlupan Seçildi'},
                       11: {1: [250, '1)1Metre'],
                            2: [100, '2)50Cm'],
                            3: [0, '3)Yok'],
                            'soru': 'Baca Uzatması Seçiniz:',
                            'cevap': 'Baca Uzatması Seçildi'},
                       12: {1: [150, '1)90 Derece'],
                            2: [100, '2)45 Derece'],
                            3: [0, '3)Yok'],
                            'soru': 'Baca Dirseği Seçiniz:',
                            'cevap': 'Baca Dirseği Seçildi'},
                       13: {1: [50, '1)Var'],
                            2: [0, '2)Yok'],
                            'soru': 'Cam-Menfez Tipi Seçiniz:',
                            'cevap': 'Cam-Menfez Seçildi'},
                       14: {1: [50, '1)Var'],
                            2: [0, '2)Yok'],
                            'soru': 'Elektrik Tipi Seçiniz:',
                            'cevap': 'Elektrik Tesisatı Seçildi'},
                       15: {1: [1000, '1)Komple'],
                            2: [750, '2)Montaj'],
                            3: [650, '3)Kombi-Gaz'],
                            'soru': 'İşçilik Tipi Seçiniz:',
                            'cevap': 'İşçilik Seçildi'},
                       16: {1: [500, '1)Var'],
                            2: [0, '2)Yok'],
                            'soru': 'Firma Gideri Tipi Seçiniz:',
                            'cevap': 'Firma Gideri Seçildi'},
                       17: {1: [9000, '1)Var'],
                            2: [0, '2)Yok'],
                            'soru': 'Extra İşçilik Tipi Seçiniz:',
                            'cevap': 'Extra İşçilik Seçildi'}}

secilenler = [False] * len(fiyat_model_listesi)
yildiz = '*' * 30
menu = f"Doğalgaz Hesap Tablosu\n{yildiz}\n1.Kombi Seçimi\n2.Kalorifer Tesisatı Seçimi\n3.Sıcak Su Tesisatı "\
       f"Seçimi\n4.Doğalgaz Tesisatı Seçimi\n5.Radyatör Seçimi\n6.Radyatör Vanası Seçimi\n7.Termostatik Vana "\
       f"Seçimi\n8.Oda Termostatı Seçimi\n9.Kombi Dolabı Seçimi\n10.Havlupan Seçimi\n11.Baca Uzatması Seçimi\n12.Baca "\
       f"Dirseği Seçimi\n13.Cam-Menfez Seçimi\n14.Elektrik Tesisatı Seçimi\n15.İşçilik Seçimi \n16.Firma Gideri "\
       f"Seçimi\n17.Extra İşçilik Seçimi \nÇIKIŞ İÇİN 'Q' YA BASINIZ...\n{yildiz}\n"

fiyatlar = [0] * len(fiyat_model_listesi)
secim = None
ana_menu = True

while True:
    if all(secilenler):
        print(yildiz)
        print('Maliyetler Toplanıyor...')
        time.sleep(3)
        rakam = int(sum(fiyatlar) * 1.12)
        kredi_karti = int(rakam * 1.07)
        oniki_senet = int(rakam * 1.24)
        onbes_senet = int(rakam * 1.30)
        onsekiz_senet = int(rakam * 1.36)
        print("Nakit: {} TL".format(rakam))
        print("Kredi Kartı: {} TL".format(kredi_karti))
        print("12 Ay Senet: {} TL".format(oniki_senet))
        print("15 Ay Senet: {} TL".format(onbes_senet))
        print("18 Ay Senet: {} TL".format(onsekiz_senet))
        break
    else:
        if ana_menu:
            print(yildiz)
            print(menu)
            secim = input('İşlemi Seçiniz:')
            print(yildiz)
            if secim.lower() == 'q':
                quit()
            secim = int(secim)
            if secim not in fiyat_model_listesi:
                print('Hatalı Seçim Yaptınız...')
            else:
                ana_menu = False
        else:
            if secim == 5:
                print(fiyat_model_listesi[secim]['soru'])
                print(yildiz)
                inp = int(input('\n'.join([v[1] for k, v in fiyat_model_listesi[secim].items() if isinstance(k, int)]) + '\n'))
                if inp in fiyat_model_listesi[secim]:
                    if inp == 3:
                        fiyatlar[secim - 1] = fiyat_model_listesi[secim][inp][0]
                        print(fiyat_model_listesi[secim]['cevap'][1])
                    else:
                        metraj = float(input('Metraj Giriniz:'))
                        fiyatlar[secim - 1] = fiyat_model_listesi[secim][inp][0] * metraj
                        print(fiyat_model_listesi[secim]['cevap'][0])
                    secilenler[secim - 1] = True
                    ana_menu = True
                else:
                    print('Yanlış Seçim Yaptınız...')
            elif secim == 6:
                print(fiyat_model_listesi[secim]['soru'])
                print(yildiz)
                inp = int(input('\n'.join([v[1] for k, v in fiyat_model_listesi[secim].items() if isinstance(k, int)]) + '\n'))
                if inp in fiyat_model_listesi[secim]:
                    if inp == 3:
                        fiyatlar[secim - 1] = fiyat_model_listesi[secim][inp][0]
                        print(fiyat_model_listesi[secim]['cevap'][1])
                    else:
                        adet = int(input('Adet Giriniz:'))
                        fiyatlar[secim - 1] = fiyat_model_listesi[secim][inp][0] * adet
                        print(fiyat_model_listesi[secim]['cevap'][0])
                    secilenler[secim - 1] = True
                    ana_menu = True
                else:
                    print('Yanlış Seçim Yaptınız...')
            elif secim == 7:
                print(fiyat_model_listesi[secim]['soru'])
                print(yildiz)
                inp = int(input('\n'.join([v[1] for k, v in fiyat_model_listesi[secim].items() if isinstance(k, int)]) + '\n'))
                if inp in fiyat_model_listesi[secim]:
                    if inp == 3:
                        fiyatlar[secim - 1] = fiyat_model_listesi[secim][inp][0]
                        print(fiyat_model_listesi[secim]['cevap'][1])
                    else:
                        adet = int(input('Adet Giriniz:'))
                        fiyatlar[secim - 1] = fiyat_model_listesi[secim][inp][0] * adet
                        print(fiyat_model_listesi[secim]['cevap'][0])
                    secilenler[secim - 1] = True
                    ana_menu = True
                else:
                    print('Yanlış Seçim Yaptınız...')
                    ana_menu = False
            else:
                print(fiyat_model_listesi[secim]['soru'])
                print(yildiz)
                inp = int(input('\n'.join([v[1] for k, v in fiyat_model_listesi[secim].items() if isinstance(k, int)]) + '\n'))
                if inp in fiyat_model_listesi[secim]:
                    fiyatlar[secim - 1] = fiyat_model_listesi[secim][inp][0]
                    print(fiyat_model_listesi[secim]['cevap'])
                    secilenler[secim - 1] = True
                    ana_menu = True
                else:
                    print('Yanlış Seçim Yaptınız...')
                    ana_menu = False
