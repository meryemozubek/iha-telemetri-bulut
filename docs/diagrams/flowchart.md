# Simülatör Akış Diyagramı

```mermaid
flowchart TD
    A([Başla]) --> B["Başlangıç değerlerini tanımla"]
    B --> C["PostgreSQL veritabanına bağlan"]
    C --> D["GPS, hız ve irtifa değerlerini güncelle"]
    D --> E["Batarya seviyesini azalt"]
    E --> F["Zaman damgasını oluştur"]
    F --> G["Telemetri verisini hazırla"]
    G --> H["Telemetri verisini terminalde göster"]
    H --> I["Veriyi PostgreSQL veritabanına kaydet"]
    I --> J{"Batarya %20'nin altında mı?"}

    J -->|Evet| K["Düşük batarya uyarısı ver"]
    J -->|Hayır| L{"Batarya tükendi mi?"}
    K --> L

    L -->|Hayır| M["1 saniye bekle"]
    M --> D

    L -->|Evet| N["Simülasyonu sonlandır"]
    N --> O([Bitiş])

    style A fill:#DCFCE7,stroke:#16A34A,color:#000
    style O fill:#FEE2E2,stroke:#DC2626,color:#000
    style J fill:#FFF3CD,stroke:#D97706,color:#000
    style L fill:#FFF3CD,stroke:#D97706,color:#000
    style K fill:#FFEDD5,stroke:#EA580C,color:#000
    style C fill:#DBEAFE,stroke:#2563EB,color:#000
    style I fill:#DBEAFE,stroke:#2563EB,color:#000
```

## Algoritmanın Açıklaması

Simülatör başlatıldığında İHA'nın başlangıç değerleri
tanımlanır ve PostgreSQL veritabanına bağlantı sağlanır.

Her döngüde GPS koordinatları, hız ve irtifa değerleri
belirlenen sınırlar içerisinde güncellenir.

Batarya seviyesi her döngüde 0.2 yüzde puan azaltılır.
Oluşturulan telemetri verisine zaman damgası eklenir
ve veri PostgreSQL veritabanına kaydedilir.

Batarya seviyesi %20'nin altına düştüğünde düşük
batarya uyarısı oluşturulur.

Batarya tamamen tükenmediği sürece simülatör yaklaşık
bir saniyelik aralıklarla veri üretmeye devam eder.

Batarya seviyesi sıfıra ulaştığında simülasyon sonlandırılır.

## Sözde Kod (Pseudocode)

    BAŞLA

    Başlangıç değerlerini tanımla
    Veritabanına bağlan

    Batarya tükenmediği sürece:

        GPS koordinatlarını güncelle
        Hız değerini güncelle
        İrtifa değerini güncelle
        Batarya seviyesini azalt
        Zaman damgasını oluştur

        Telemetri verisini hazırla
        Telemetri verisini ekrana yazdır
        Telemetri verisini veritabanına kaydet

        Eğer batarya seviyesi 20'nin altındaysa:
            Düşük batarya uyarısı ver

        Eğer batarya seviyesi sıfıra ulaştıysa:
            Döngüyü sonlandır

        1 saniye bekle

    Simülasyonu sonlandır

    BİTİR