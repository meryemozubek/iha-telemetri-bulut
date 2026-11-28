import main


# Orijinal telemetri uretme fonksiyonunu sakla
orijinal_telemetri_uret = main.telemetri_uret

test_sayaci = 0


def test_telemetri_uret():
    global test_sayaci

    veri = orijinal_telemetri_uret()
    test_sayaci += 1

    # Her 5. kayitta bilerek hata olustur
    if test_sayaci % 5 == 0:
        veri["drone_id"] = None

    return veri


# Test sirasinda telemetri fonksiyonunu degistir
main.telemetri_uret = test_telemetri_uret

# Simulasyonu baslat
main.simulasyonu_baslat()