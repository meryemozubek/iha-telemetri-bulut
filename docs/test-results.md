# İHA Telemetri İzleme Sistemi – Test Sonuçları

## 1. Testin Amacı

Bu çalışmada geliştirilen bulut tabanlı İHA telemetri izleme ve kayıt sisteminin işlevselliği, kaynak tüketimi, veri kayıt performansı ve veri kalıcılığı incelenmiştir.

## 2. Test Ortamı

| Özellik | Değer |
|---|---|
| Test tarihi | 28.11.2026 |
| Bulut sağlayıcısı | Amazon Web Services (AWS) |
| Bulut hizmeti | Amazon EC2 |
| Sunucu bölgesi | Stockholm (eu-north-1) |
| Sunucu tipi | t3.small |
| İşlemci | 2 vCPU |
| RAM | 2 GiB |
| İşletim sistemi | Ubuntu 26.04.1 LTS |
| Docker sürümü | 29.1.3 |
| Docker Compose sürümü | 2.40.3 |
| Python sürümü | 3.10 |
| Veritabanı | PostgreSQL 15 |
| Görselleştirme aracı | Grafana 12.3.0 |
| Simüle edilen İHA sayısı | 1 |
| Hedef veri üretim aralığı | 1 saniye |

## 3. İşlevsel Sistem Testleri

| Test | Sonuç |
|---|---|
| Docker kurulumu ve hello-world testi | Başarılı |
| GitHub üzerinden projenin sunucuya aktarılması | Başarılı |
| Docker imajlarının oluşturulması | Başarılı |
| Konteynerlerin başlatılması | Başarılı |
| PostgreSQL bağlantısı | Başarılı |
| Telemetri verilerinin üretilmesi | Başarılı |
| Telemetri verilerinin veritabanına kaydedilmesi | Başarılı |
| Grafana veri kaynağı bağlantısı | Başarılı |
| Batarya göstergesi | Başarılı |
| GPS konumunun haritada gösterilmesi | Başarılı |
| İrtifa grafiği | Başarılı |
| Hız grafiği | Başarılı |
| SSH üzerinden güvenli uzaktan erişim | Başarılı |

## 4. Konteyner Kaynak Tüketimi Testi

### 4.1. Test Yöntemi

Konteynerlerin CPU ve RAM tüketimini ölçmek için Docker Stats komutu kullanılmıştır.

```bash
sudo docker stats --no-stream
```

Altı ölçüm gerçekleştirilmiştir. İlk ve son ölçüm arasında 61 saniye bulunmaktadır. Ölçümler yaklaşık 12-13 saniye aralıklarla alınmıştır.

### 4.2. CPU Ölçümleri

| Ölçüm | Python (%) | Grafana (%) | PostgreSQL (%) |
|---|---:|---:|---:|
| 1 | 0.08 | 0.25 | 0.06 |
| 2 | 0.06 | 0.42 | 0.07 |
| 3 | 0.07 | 0.30 | 0.04 |
| 4 | 0.07 | 0.26 | 0.05 |
| 5 | 0.06 | 0.55 | 0.06 |
| 6 | 0.07 | 0.26 | 0.04 |

### 4.3. CPU İstatistikleri

| Konteyner | Minimum (%) | Ortalama (%) | Maksimum (%) |
|---|---:|---:|---:|
| Python simülatörü | 0.06 | 0.0683 | 0.08 |
| Grafana | 0.25 | 0.3400 | 0.55 |
| PostgreSQL | 0.04 | 0.0533 | 0.07 |
| Toplam | 0.37 | 0.4617 | 0.67 |

### 4.4. RAM Ölçümleri

Bütün bellek değerleri MiB cinsindendir.

| Ölçüm | Python | Grafana | PostgreSQL |
|---|---:|---:|---:|
| 1 | 19.26 | 266.80 | 59.43 |
| 2 | 19.51 | 266.80 | 59.43 |
| 3 | 19.26 | 261.40 | 59.63 |
| 4 | 19.51 | 261.40 | 59.39 |
| 5 | 19.27 | 261.90 | 59.39 |
| 6 | 19.51 | 261.60 | 59.43 |

### 4.5. RAM İstatistikleri

| Konteyner | Minimum (MiB) | Ortalama (MiB) | Maksimum (MiB) |
|---|---:|---:|---:|
| Python simülatörü | 19.26 | 19.39 | 19.51 |
| Grafana | 261.40 | 263.32 | 266.80 |
| PostgreSQL | 59.39 | 59.45 | 59.63 |
| Toplam | 340.30 | 342.15 | 345.74 |

### 4.6. Sonuçların Değerlendirilmesi

Üç konteynerin toplam ortalama CPU tüketimi %0.462, toplam ortalama RAM tüketimi ise 342.15 MiB olarak hesaplanmıştır.

Grafana, diğer bileşenlere göre daha fazla bellek tüketmektedir. Python simülatörü ve PostgreSQL düşük kaynak tüketimiyle çalışmaktadır.

Ölçüm sonuçları, sistemin mevcut AWS EC2 t3.small sunucusunda tek İHA simülasyonu altında düşük kaynak tüketimiyle çalışabildiğini göstermektedir.

## 5. Veri Kayıt Performansı Testi

### 5.1. Test Yöntemi

PostgreSQL veritabanındaki kayıt sayısı test başlangıcında ve 60 saniye sonunda ölçülmüştür.

```sql
SELECT COUNT(*) FROM telemetry;
```

### 5.2. Test Sonuçları

| Ölçülen özellik | Değer |
|---|---:|
| Başlangıç zamanı (UTC) | 12:55:49 |
| Bitiş zamanı (UTC) | 12:56:49 |
| Test süresi | 60 saniye |
| Başlangıç kayıt sayısı | 1009 |
| Bitiş kayıt sayısı | 1069 |
| Beklenen yeni kayıt sayısı | 60 |
| Gerçekleşen yeni kayıt sayısı | 60 |
| Ortalama kayıt hızı | 1 kayıt/saniye |
| Hedef kayıt hızına ulaşma oranı | %100 |

### 5.3. Hesaplamalar

- Yeni kayıt sayısı = 1069 - 1009 = 60
- Ortalama kayıt hızı = 60 / 60 = 1 kayıt/saniye
- Hedefe ulaşma oranı = (60 / 60) x 100 = %100

### 5.4. Değerlendirme

Sistem, 60 saniyelik test süresince hedeflenen kayıt sayısına ulaşmıştır. Bu sonuç, test koşulları altında saniyede bir telemetri kaydı oluşturulabildiğini göstermektedir.

## 6. Kayıt Aralığı ve Hata Kontrolü

### 6.1. Kayıt Aralığı Testi

PostgreSQL LAG fonksiyonu kullanılarak ID değerleri 1010-1069 arasındaki ardışık kayıtların zaman damgaları karşılaştırılmıştır.

| Ölçülen özellik | Sonuç |
|---|---:|
| İncelenen kayıt sayısı | 60 |
| Zaman aralığı sayısı | 59 |
| Hedeflenen kayıt aralığı | 1 saniye |
| Ortalama kayıt aralığı | 1.0169 saniye |
| Minimum kayıt aralığı | 1 saniye |
| Maksimum kayıt aralığı | 2 saniye |
| Hedef aralığa göre ortalama sapma | %1.69 |

Ortalama kayıt aralığının hedeflenen bir saniyelik değere yakın olduğu görülmüştür. Zaman damgası hassasiyeti ve veri işleme süresi ölçülen farklılıkları etkileyebilir.

### 6.2. Hata Loglarının İncelenmesi

Simülatör logları aşağıdaki komut ile incelenmiştir.

```bash
sudo docker compose logs --no-color simulator | grep -Ei "hata|error|exception|traceback|failed"
```

Komut sonucunda herhangi bir hata ifadesi bulunmamıştır.

Bu sonuç, incelenen loglarda belirtilen hata ifadelerinin bulunmadığını göstermektedir. Bütün kayıt denemeleri bağımsız olarak sayılmadığından kesin hata oranı hesaplanmamıştır.

## 7. Veri Kalıcılığı Testi

### 7.1. Testin Amacı

Docker volume kullanılarak PostgreSQL kayıtlarının konteynerler kaldırılıp yeniden oluşturulduğunda korunup korunmadığının incelenmesi amaçlanmıştır.

### 7.2. Test Adımları

1. Python simülatörü durdurulmuştur.
2. PostgreSQL kayıt sayısı ölçülmüştür.
3. Docker konteynerleri ve Docker ağı kaldırılmıştır.
4. Docker volume alanlarının korunduğu doğrulanmıştır.
5. PostgreSQL ve Grafana konteynerleri yeniden oluşturulmuştur.
6. PostgreSQL kayıt sayısı tekrar ölçülmüştür.

Kullanılan temel komutlar:

```bash
sudo docker compose stop simulator
sudo docker compose down
sudo docker volume ls
sudo docker compose up -d postgres grafana
```

### 7.3. Test Sonuçları

| Ölçülen özellik | Değer |
|---|---:|
| Test öncesi kayıt sayısı | 1233 |
| Test sonrası kayıt sayısı | 1233 |
| Kayıt sayısındaki kayıp | 0 |
| Kayıt sayısının korunma oranı | %100 |

### 7.4. Değerlendirme

Konteynerler kaldırılıp yeniden oluşturulmasına rağmen PostgreSQL kayıt sayısı değişmemiştir. Docker volume kullanımının veri kalıcılığı sağladığı kayıt sayısı bakımından doğrulanmıştır.

Kayıt içeriklerinin birebir karşılaştırılması bu testin kapsamına dahil edilmemiştir.

## 8. Sunucunun Genel Kaynak Tüketimi

Sunucunun genel kaynak tüketimini ölçmek için aşağıdaki komutlar kullanılmıştır.

```bash
free -h
df -h /
uptime
sudo docker system df
```

### 8.1. Bellek ve Disk Kullanımı

| Ölçülen özellik | Sonuç |
|---|---:|
| Toplam kullanılabilir RAM | 1.9 GiB |
| Kullanılan RAM | 659 MiB |
| Kullanıma hazır RAM | 1.2 GiB |
| Toplam disk kapasitesi | 6.7 GiB |
| Kullanılan disk alanı | 4.2 GiB |
| Boş disk alanı | 2.5 GiB |
| Disk kullanım oranı | %64 |
| Swap | 0 B |

### 8.2. Sistem Yükü

| Zaman aralığı | Load Average |
|---|---:|
| 1 dakika | 0.00 |
| 5 dakika | 0.03 |
| 15 dakika | 0.00 |

### 8.3. Docker Kaynakları

| Kaynak | Sayı | Boyut |
|---|---:|---:|
| Docker imajları | 4 | 1.653 GB |
| Konteynerler | 3 | 274.4 kB |
| Docker volume alanları | 2 | 98.89 MB |
| Build cache | 11 | 216.7 MB |

Ölçüm sırasında üç konteyner ve iki Docker volume alanı aktiftir.

## 9. Karşılaşılan Sorunlar ve İyileştirme Önerileri

- Yerel Docker imajı oluşturulurken ağ bağlantısı kaynaklı indirme sorunları yaşanmıştır. Farklı bir ağ bağlantısı kullanılarak sorun çözülmüştür.
- AWS sunucusuna SSH bağlantısı sırasında erişim sorunları yaşanmıştır. Güvenlik grubu kuralları kontrol edilerek bağlantı sağlanmıştır.
- Simülatörün bataryası tükendiğinde veri üretimi durmaktadır. Yeni bir uçuş için simülatör yeniden başlatılabilmektedir.
- Simülatörün Docker üzerinden durdurulması sırasında 137 çıkış kodu gözlemlenmiştir. Bu durum, durdurma süresi sonunda işlemin zorla sonlandırılmış olabileceğini göstermektedir. Güvenli kapanma mekanizmasının geliştirilmesi gelecekte yapılabilecek iyileştirmeler arasındadır.

## 10. Testlerin Sınırlılıkları

- Deneyler tek İHA simülasyonu ile gerçekleştirilmiştir.
- Gerçek bir İHA üzerinden veri alınmamıştır.
- CPU ve RAM ölçümleri kısa süreli testlere dayanmaktadır.
- Yüksek yük ve çoklu İHA performansı ölçülmemiştir.
- Kesin veri kayıt hata oranı hesaplanmamıştır.
- Veri kalıcılığı kayıt sayısı üzerinden değerlendirilmiştir.
- Uzun süreli disk tüketimi ve sistem kararlılığı ayrıca incelenmelidir.

## 11. Genel Sonuç

Geliştirilen bulut tabanlı İHA telemetri izleme ve kayıt sistemi AWS EC2 sanal sunucusu üzerinde Docker Compose kullanılarak çalıştırılmıştır.

Python simülatörü tarafından üretilen GPS, hız, irtifa ve batarya verileri PostgreSQL veritabanına kaydedilmiş ve Grafana üzerinden görselleştirilmiştir.

Gerçekleştirilen testlerde sistemin hedeflenen veri kayıt hızına ulaştığı, düşük kaynak tüketimiyle çalıştığı ve konteynerlerin yeniden oluşturulması sırasında kayıt sayısının korunduğu gözlemlenmiştir.

Sonuçlar, geliştirilen sistemin belirlenen temel işlevsel gereksinimleri mevcut deney koşulları altında karşılayabildiğini göstermektedir.
---

## Ek Deneysel Testler ve Hata Orani Analizi

### Test Tarihi

28.11.2026

### Testin Amaci

Telemetri verilerinin PostgreSQL veritabanina kaydedilmesi
sirasinda olusan basarili ve basarisiz kayit girisimlerinin
belirlenmesi, hata yonetiminin dogrulanmasi ve sistemin
bulut ortamindaki kayit performansinin olculmesi amaclanmistir.

Bu kapsamda Python simulatorune toplam girisim, basarili kayit,
basarisiz kayit ve belirsiz girisim sayaclari eklenmistir.
Test suresi time.monotonic() fonksiyonu ile olculmustur.

### 1. Yerel Normal Calisma Testi

Simulator, yerel bilgisayarda PostgreSQL veritabanina
baglanarak normal calisma kosullarinda test edilmistir.

| Olcut | Sonuc |
|---|---:|
| Toplam kayit girisimi | 15 |
| Basarili kayit | 15 |
| Basarisiz kayit | 0 |
| Belirsiz girisim | 0 |
| Test suresi | 14.66 saniye |
| Basari orani | %100 |
| Hata orani | %0 |

Test sonucunda normal calisma kosullarinda herhangi bir
kayit hatasi gozlemlenmemistir.

### 2. Kontrollu Hata Testi

Hata yonetiminin dogrulanmasi icin simulator/hata_testi.py
dosyasi olusturulmustur.

Her besinci kayit girisiminde drone_id alanina None degeri
atanarak PostgreSQL NOT NULL kisitinin ihlal edilmesi
saglanmistir.

| Olcut | Sonuc |
|---|---:|
| Toplam kayit girisimi | 19 |
| Basarili kayit | 16 |
| Basarisiz kayit | 3 |
| Belirsiz girisim | 0 |
| Test suresi | 18.42 saniye |
| Basari orani | %84.21 |
| Hata orani | %15.79 |

PostgreSQL, 5., 10. ve 15. kayit girisimlerini reddetmistir.
Python tarafinda psycopg.Error ile hatalar yakalanmis ve
rollback() islemi uygulanmistir.

Simulator, hatali kayitlardan sonra calismaya devam etmis
ve sonraki gecerli verileri veritabanina kaydetmistir.

Bu testteki hata orani bilerek olusturulan gecersiz verilerden
kaynaklanmaktadir. Normal sistem performansini temsil etmez.

### 3. AWS Bulut Ortami Normal Calisma Testi

#### Test Ortami

- Bulut saglayicisi: Amazon Web Services (AWS)
- Sanal sunucu: EC2 t3.small
- Bolge: eu-north-1 (Stockholm)
- Islemci: 2 vCPU
- Bellek: 2 GiB RAM
- Isletim sistemi: Ubuntu 26.04.1 LTS
- Konteyner yonetimi: Docker Compose
- Veritabani: PostgreSQL 15
- Gorsellestirme: Grafana 12.3.0
- Programlama dili: Python 3.10

#### Test Yontemi

Guncellenen simulator kaynak kodu GitHub uzerinden AWS
sunucusuna aktarilmis ve Docker imaji yeniden olusturulmustur.

Simulator, baslangic bataryasi %100 olacak sekilde
calistirilmis ve batarya tamamen tukenene kadar herhangi
bir manuel mudahale yapilmamistir.

Test sirasinda bilerek hata olusturulmamistir.

#### Test Sonuclari

| Olcut | Sonuc |
|---|---:|
| Toplam kayit girisimi | 500 |
| Basarili kayit | 500 |
| Basarisiz kayit | 0 |
| Belirsiz girisim | 0 |
| Test suresi | 501.48 saniye |
| Basari orani | %100 |
| Hata orani | %0 |
| Ortalama kayit hizi | 0.997 kayit/saniye |

#### Veritabani Dogrulamasi

| Olcut | Kayit Sayisi |
|---|---:|
| Test oncesi kayit sayisi | 1648 |
| Test sonrasi kayit sayisi | 2148 |
| Eklenen yeni kayit sayisi | 500 |

Kayit artisi:

2148 - 1648 = 500 kayit

Python tarafinda olculen basarili kayit sayisi ile
PostgreSQL veritabanindaki kayit sayisi artisi eslesmistir.

### 4. Performans Hesaplamalari

Hata orani:

Hata orani = (Basarisiz kayit / Toplam girisim) x 100

AWS testi:

Hata orani = (0 / 500) x 100 = %0

Basari orani:

Basari orani = (Basarili kayit / Toplam girisim) x 100

AWS testi:

Basari orani = (500 / 500) x 100 = %100

Ortalama kayit hizi:

500 / 501.48 = 0.997 kayit/saniye

Ortalama dongu suresi:

501.48 / 500 = 1.003 saniye/kayit

Bu sure, yalnizca veritabani sorgu gecikmesini degil,
simulatorun bekleme suresi dahil toplam calisma suresini
temsil etmektedir.

### 5. Deneysel Testlerin Karsilastirilmasi

| Olcut | Yerel Normal | Kontrollu Hata | AWS Normal |
|---|---:|---:|---:|
| Toplam girisim | 15 | 19 | 500 |
| Basarili kayit | 15 | 16 | 500 |
| Basarisiz kayit | 0 | 3 | 0 |
| Belirsiz girisim | 0 | 0 | 0 |
| Sure (saniye) | 14.66 | 18.42 | 501.48 |
| Basari orani | %100 | %84.21 | %100 |
| Hata orani | %0 | %15.79 | %0 |

### 6. Ornek Veri Seti

AWS PostgreSQL veritabaninda bulunan telemetri kayitlari
CSV formatinda disa aktarilmistir.

- Dosya: data/sample_telemetry.csv
- Veri sayisi: 1648
- Baslik dahil satir sayisi: 1649
- Sutun sayisi: 8
- Dosya boyutu: Yaklasik 105 KB
- Aktarim yontemi: SCP

Veri seti simulator tarafindan uretilen sentetik
telemetri verilerinden olusmaktadir.

CSV dosyasi son 500 kayitlik AWS testinden once
olusturuldugu icin bu testin kayitlarini icermemektedir.

### 7. Test Kanitlari

AWS testinin terminal ciktilari tee komutu kullanilarak
bir log dosyasina kaydedilmistir.

Log dosyasi:

[aws-telemetry-test.log](test-evidence/aws-telemetry-test.log)

Ornek veri seti:

[sample_telemetry.csv](../data/sample_telemetry.csv)

### 8. Sonuclarin Degerlendirilmesi

AWS ortaminda gerceklestirilen 500 kayitlik testte
herhangi bir kayit hatasi gozlemlenmemistir.

Sistem, saniyede yaklasik bir telemetri kaydi olusturma
hedefine ulasmistir.

Kontrollu hata testinde gecersiz verilerin PostgreSQL
tarafindan reddedildigi ve simulatorun sonraki kayitlara
devam edebildigi dogrulanmistir.

Onceki kaynak tuketimi testlerinde olculen ortalama
toplam CPU kullanimi yaklasik %0.462, toplam konteyner
bellek kullanimi ise 342.15 MiB olarak belirlenmistir.

Bu olcumler ayri test kosularinda gerceklestirilmistir.

### 9. Testlerin Sinirliliklari

- Testler tek bir sanal IHA ile gerceklestirilmistir.
- Gercek IHA veya fiziksel sensor kullanilmamistir.
- Uzun sureli ve yuksek yuk altinda stres testi yapilmamistir.
- Tam baglanti kopmasi ve otomatik yeniden baglanma
  mekanizmasi test edilmemistir.
- Veritabani kayit gecikmesi bagimsiz olarak olculmemistir.
- AWS testindeki %0 hata orani yalnizca gerceklestirilen
  500 kayitlik deneyin sonucunu temsil etmektedir.

Elde edilen sonuclar sistemin belirlenen test kosullarinda
basarili calistigini gostermektedir. Tum olasi calisma
kosullarinda hatasiz calisacagini garanti etmemektedir.
