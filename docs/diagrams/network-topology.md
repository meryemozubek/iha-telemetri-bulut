# Ağ Topolojisi

```mermaid
flowchart TD
    subgraph LOCAL["Yerel Bilgisayar - Windows"]
        A["Web Tarayıcısı - localhost:3001"]
        B["SSH İstemcisi - Git Bash"]
        A <-->|HTTP - 3001| B
    end

    I(("İnternet"))

    subgraph AWS["AWS EC2 - Stockholm"]
        SG["Security Group - TCP 22"]
        SSH["Ubuntu SSH Sunucusu - Port 22"]
        H["127.0.0.1:3000"]

        subgraph NETWORK["Docker Bridge Network"]
            P["Python Simülatörü"]
            DB["PostgreSQL - Port 5432"]
            G["Grafana - Port 3000"]

            P -->|TCP 5432| DB
            G <-->|TCP 5432 - SQL| DB
        end

        SG <--> SSH
        SSH <--> H
        H <--> G
    end

    B <-->|Şifreli SSH Tüneli| I
    I <-->|TCP 22| SG

    style A fill:#DCFCE7,stroke:#16A34A,color:#000
    style B fill:#DCFCE7,stroke:#16A34A,color:#000
    style SG fill:#FEE2E2,stroke:#DC2626,color:#000
    style SSH fill:#F3E8FF,stroke:#9333EA,color:#000
    style P fill:#FFF3CD,stroke:#D97706,color:#000
    style DB fill:#DBEAFE,stroke:#2563EB,color:#000
    style G fill:#FFEDD5,stroke:#EA580C,color:#000
```

## Ağ Topolojisi Açıklaması

AWS EC2 sunucusuna SSH protokolü üzerinden erişilmektedir.
AWS Security Group üzerinde TCP 22 portuna yalnızca
yetkilendirilen kullanıcı IP adresinden erişim sağlanmaktadır.

Docker Compose tarafından oluşturulan bridge ağı sayesinde
Python, PostgreSQL ve Grafana konteynerleri birbirleriyle
haberleşebilmektedir.

Python simülatörü ve Grafana, PostgreSQL veritabanına
Docker ağı üzerinden 5432 portu ile bağlanmaktadır.

Grafana'nın 3000 portu ve PostgreSQL'in sunucu üzerindeki
5433 portu yalnızca 127.0.0.1 adresine bağlanmıştır.
Bu servisler doğrudan internete açılmamıştır.

Kullanıcı, SSH tüneli aracılığıyla kendi bilgisayarındaki
3001 portunu AWS sunucusundaki 3000 portuna yönlendirerek
Grafana izleme paneline erişmektedir.

## Kullanılan Portlar

| Port | Kullanım amacı | Erişim |
|---|---|---|
| 22 | SSH bağlantısı | Yetkilendirilmiş IP |
| 3000 | Grafana | Sunucu localhost ve Docker ağı |
| 3001 | Grafana SSH tüneli | Kullanıcı bilgisayarı |
| 5432 | PostgreSQL | Docker ağı |
| 5433 | PostgreSQL port yönlendirmesi | Sunucu localhost |

## Ağ Güvenliği

- SSH anahtarı ile kimlik doğrulama
- IP adresi sınırlandırılmış Security Group
- SSH tüneli ile şifreli veri aktarımı
- PostgreSQL parola koruması
- Grafana kullanıcı doğrulaması
- Veritabanının doğrudan internete açılmaması
- Konteynerler arası özel Docker ağı