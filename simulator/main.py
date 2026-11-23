
import random
import time
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
    zaman = datetime.now().astimezone().isoformat(timespec="seconds")

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

    print("IHA Telemetri Simulatoru Baslatildi!")
    print("Durdurmak icin CTRL + C tuslarina basin.")

    try:
        # Veritabanina bir kez baglan
        with veritabanina_baglan() as baglanti:

            while batarya > 0:

                # Yeni telemetri verisi uret
                veri = telemetri_uret()

                # Ayni baglantiyi kullanarak kaydet
                telemetri_kaydet(baglanti, veri)

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



# Programin baslangic noktasi
if __name__ == "__main__":
    simulasyonu_baslat()
