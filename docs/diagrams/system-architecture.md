# Sistem Mimarisi

```mermaid
flowchart TD
    subgraph AWS["AWS EC2 - Ubuntu"]
        subgraph Docker["Docker Compose"]
            A["Python Telemetri Simülatörü"]
            B["PostgreSQL 15"]
            C["Grafana 12.3.0"]
            D[("PostgreSQL Volume")]
            E[("Grafana Volume")]

            A -->|Telemetri verisi - INSERT| B
            C -->|SQL sorgusu| B
            B -->|Sorgu sonuçları| C
            B --- D
            C --- E
        end
    end

    F["Kullanıcı Bilgisayarı - Web Tarayıcısı"]
    F <-->|SSH Tüneli| C

    style A fill:#FFF3CD,stroke:#D97706,color:#000
    style B fill:#DBEAFE,stroke:#2563EB,color:#000
    style C fill:#FFEDD5,stroke:#EA580C,color:#000
    style D fill:#DBEAFE,stroke:#2563EB,color:#000
    style E fill:#FFEDD5,stroke:#EA580C,color:#000
    style F fill:#DCFCE7,stroke:#16A34A,color:#000
```

## Mimari Açıklaması

Sistem, AWS EC2 sanal sunucusu üzerinde Docker Compose
kullanılarak çalıştırılan üç temel konteynerden oluşmaktadır.

Python simülatörü tarafından üretilen GPS, hız, irtifa ve
batarya verileri PostgreSQL veritabanına kaydedilmektedir.

Grafana, PostgreSQL veritabanından SQL sorguları ile aldığı
verileri kullanıcıya görsel olarak sunmaktadır.

Docker volume alanları verilerin kalıcılığını sağlamaktadır.

Kullanıcı, Grafana izleme paneline SSH tüneli üzerinden
erişmektedir.