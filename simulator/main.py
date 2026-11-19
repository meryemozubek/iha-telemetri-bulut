
import random
import time
from datetime import datetime


# 1. IHA'nin baslangic bilgileri
enlem = 40.9876
boylam = 29.1254
hiz = 20.0
irtifa = 50.0
batarya = 100.0

print("IHA Telemetri Simulatoru Baslatildi!")
print("Programi durdurmak icin CTRL + C tuslarina basin.")


try:
    # Batarya bitene kadar ucus verileri uret
    while batarya > 0:

        # 2. IHA'nin GPS konumunu degistir
        enlem += random.uniform(-0.0001, 0.0001)
        boylam += random.uniform(-0.0001, 0.0001)

        # 3. IHA'nin hizini guncelle
        hiz += random.uniform(-3, 3)
        hiz = max(0, min(80, hiz))

        # 4. IHA'nin irtifasini guncelle
        irtifa += random.uniform(-2, 2)
        irtifa = max(0, min(150, irtifa))

        # 5. Batarya seviyesini azalt
        batarya = max(0, batarya - 0.2)

        # 6. Verinin olusturuldugu zamani al
        zaman = datetime.now().astimezone().isoformat(timespec="seconds")

        # 7. Tum ucus verilerini bir sozlukte topla
        telemetri_verisi = {
            "drone_id": 1,
            "timestamp": zaman,
            "latitude": round(enlem, 6),
            "longitude": round(boylam, 6),
            "speed": round(hiz, 2),
            "altitude": round(irtifa, 2),
            "battery": round(batarya, 2)
        }

        # 8. Ucus bilgilerini terminalde goster
        print("----------------------------------")
        print("IHA ID:", telemetri_verisi["drone_id"])
        print("Zaman:", telemetri_verisi["timestamp"])
        print("GPS:", telemetri_verisi["latitude"], telemetri_verisi["longitude"])
        print("Hiz:", telemetri_verisi["speed"], "km/sa")
        print("Irtifa:", telemetri_verisi["altitude"], "metre")
        print("Batarya:", telemetri_verisi["battery"], "%")

        # 9. Batarya seviyesi dusukse uyari ver
        if batarya < 20:
            print("UYARI: Dusuk batarya!")

        # 10. Yeni veri uretmeden once 1 saniye bekle
        time.sleep(1)

    print("Batarya bitti. Simulasyon sona erdi.")

except KeyboardInterrupt:
    print("\nSimulasyon kullanici tarafindan durduruldu.")
