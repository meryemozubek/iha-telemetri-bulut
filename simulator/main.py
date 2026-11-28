import random
import time
import psycopg
from datetime import datetime
from veritabani import veritabanina_baglan, telemetri_kaydet


# IHA'nin baslangic bilgileri
enlem = 40.9876
boylam = 29.1254
hiz = 20.0
irtifa = 50.0
batarya = 100.0


# Yeni telemetri verisi olusturan fonksiyon
def telemetri_uret():
    global enlem, boylam, hiz, irtifa, batarya

    # GPS koordinatlarini guncelle
    enlem += random.uniform(-0.0001, 0.0001)
    boylam += random.uniform(-0.0001, 0.0001)

    # Hizi guncelle
    hiz += random.uniform(-3, 3)
    hiz = max(0, min(80, hiz))

    # Irtifayi guncelle
    irtifa += random.uniform(-2, 2)
    irtifa = max(0, min(150, irtifa))

    # Batarya seviyesini azalt
    batarya = max(0, batarya - 0.2)

    # Guncel tarih ve saat
    zaman = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    # Verileri bir sozlukte topla
    telemetri_verisi = {
        "drone_id": 1,
        "timestamp": zaman,
        "latitude": round(enlem, 6),
        "longitude": round(boylam, 6),
        "speed": round(hiz, 2),
        "altitude": round(irtifa, 2),
        "battery": round(batarya, 2)
    }

    return telemetri_verisi


# Simulasyonu calistiran fonksiyon
def simulasyonu_baslat():

    # Performans ve hata sayaclari
    toplam_girisim = 0
    basarili_kayit = 0
    basarisiz_kayit = 0

    # Test baslangic zamani
    baslangic_zamani = time.monotonic()

    print("IHA Telemetri Simulatoru Baslatildi!")
    print("Durdurmak icin CTRL + C tuslarina basin.")

    try:
        # Veritabanina bir kez baglan
        with veritabanina_baglan() as baglanti:

            while batarya > 0:

                # Yeni telemetri verisi uret
                veri = telemetri_uret()

                # Kayit girisimini say
                toplam_girisim += 1

                try:
                    telemetri_kaydet(baglanti, veri)
                    basarili_kayit += 1

                except psycopg.Error as hata:
                    basarisiz_kayit += 1

                    print("Veritabani kayit hatasi:", hata)

                    # Basarisiz islemi geri al
                    baglanti.rollback()

                # Verileri terminalde goster
                print("----------------------------------")
                print("IHA ID:", veri["drone_id"])
                print("Zaman:", veri["timestamp"])
                print("GPS:", veri["latitude"], veri["longitude"])
                print("Hiz:", veri["speed"], "km/sa")
                print("Irtifa:", veri["altitude"], "metre")
                print("Batarya:", veri["battery"], "%")

                # Dusuk batarya uyarisi
                if veri["battery"] < 20:
                    print("UYARI: Dusuk batarya!")

                time.sleep(1)

            print("Batarya bitti. Simulasyon sona erdi.")

    except KeyboardInterrupt:
        print("\nSimulasyon kullanici tarafindan durduruldu.")

    except psycopg.Error as hata:
        print("Veritabani baglanti veya islem hatasi:", hata)
        raise

    finally:

        # Toplam calisma suresini hesapla
        test_suresi = time.monotonic() - baslangic_zamani

        print("\n==================================")
        print("SIMULASYON TEST SONUCLARI")
        print("==================================")

        print("Toplam kayit girisimi:", toplam_girisim)
        print("Basarili kayit:", basarili_kayit)
        print("Basarisiz kayit:", basarisiz_kayit)
        print(f"Test suresi: {test_suresi:.2f} saniye")

        if toplam_girisim > 0:

            hata_orani = (
                basarisiz_kayit / toplam_girisim
            ) * 100

            basari_orani = (
                basarili_kayit / toplam_girisim
            ) * 100

            print(f"Hata orani: %{hata_orani:.2f}")
            print(f"Basari orani: %{basari_orani:.2f}")

        else:
            print("Hata orani: Hesaplanamadi")
            print("Basari orani: Hesaplanamadi")

        belirsiz_kayit = (
            toplam_girisim - basarili_kayit - basarisiz_kayit
        )

        print("Sonucu belirsiz girisim:", belirsiz_kayit)
        print("==================================")


# Programin baslangic noktasi
if __name__ == "__main__":
    simulasyonu_baslat()