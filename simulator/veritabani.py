
import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv


# Projenin ana klasorunu bul
proje_klasoru = Path(__file__).resolve().parent.parent

# .env dosyasindaki bilgileri yukle
load_dotenv(proje_klasoru / ".env")


# PostgreSQL baglantisi olustur
def veritabanina_baglan():
    baglanti = psycopg.connect(
        host="127.0.0.1",
        port=5433,
        dbname="iha_telemetri",
        user="iha_user",
        password=os.getenv("POSTGRES_PASSWORD")
    )

    return baglanti


# Telemetri verisini PostgreSQL'e kaydet
def telemetri_kaydet(baglanti, veri):

    with baglanti.cursor() as imlec:
        imlec.execute(
            """
            INSERT INTO telemetry (
                drone_id,
                timestamp,
                latitude,
                longitude,
                speed,
                altitude,
                battery
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                veri["drone_id"],
                veri["timestamp"],
                veri["latitude"],
                veri["longitude"],
                veri["speed"],
                veri["altitude"],
                veri["battery"]
            )
        )

    # Kaydi kalici hale getir
    baglanti.commit()

    print("Telemetri verisi veritabanina kaydedildi.")
