# Literatür Araştırması

## 1. Araştırmanın Amacı

Bu literatür araştırmasının amacı, bulut tabanlı İHA telemetri izleme sistemleri, bulut bilişim ve konteyner tabanlı sanallaştırma teknolojileri üzerine gerçekleştirilen çalışmaları incelemektir.

İncelenen çalışmalar doğrultusunda geliştirilen sistemin teknolojik altyapısı, tasarım tercihleri, mevcut çalışmalarla benzerlikleri ve farklılıkları değerlendirilmiştir.

Ayrıca geliştirilen sistemin deneysel performans sonuçları, veri kalıcılığı ve hata yönetimi özellikleri literatürde incelenen yaklaşımlar doğrultusunda değerlendirilmiştir.

### 1.1. Literatür İnceleme Yöntemi

Literatür incelemesi üç temel konu kapsamında gerçekleştirilmiştir:

- Bulut tabanlı İHA telemetri ve izleme sistemleri.
- Sanal makine ve konteyner tabanlı sanallaştırma.
- Bulut bilişim ve uygulama taşınabilirliği.

Konuyla doğrudan ilişkili bilimsel makaleler, konferans bildirileri ve teknik yayınlar incelenmiştir.

Kaynaklar aşağıdaki ölçütler doğrultusunda değerlendirilmiştir:

- Araştırmanın amacı.
- Kullanılan yöntem.
- Kullanılan teknolojiler.
- Sistem mimarisi.
- Elde edilen sonuçlar.
- Geliştirilen proje ile benzerlikler ve farklılıklar.

İnceleme, seçilmiş kaynaklara dayalı anlatısal bir literatür araştırması niteliğindedir. Kapsamlı bir sistematik literatür taraması gerçekleştirilmemiştir.

## 2. Bulut Tabanlı İHA İzleme Sistemleri

### 2.1. Itkin, Kim ve Park (2016)

**Çalışmanın adı:** Development of Cloud-Based UAV Monitoring and Management System

**Çalışmanın amacı:**

İnsansız hava araçlarının bulut ortamında gerçek zamanlı olarak izlenmesini ve yönetilmesini sağlayan bir sistem geliştirmektir.

**Kullanılan yöntem:**

Araştırmacılar, İHA'lardan elde edilen GPS, batarya ve çeşitli sensör verilerinin web tabanlı bir uygulama üzerinden izlenmesini sağlayan bir sistem geliştirmişlerdir.

İHA konumları ve uçuş rotaları dinamik harita üzerinde görselleştirilmiştir. Ayrıca sistemde çarpışma önleme mekanizmalarına yer verilmiştir.

Sistemin geliştirilmesinde MongoDB, ExpressJS, AngularJS ve NodeJS teknolojilerinden yararlanılmıştır.

**Çalışmanın sonucu:**

Geliştirilen sistemin uygulanabilirliği ve performansı simülasyon ortamında değerlendirilmiştir.

**Geliştirilen proje ile ilişkisi:**

Bu projede de İHA telemetri verilerinin bulut ortamında izlenmesi amaçlanmaktadır.

GPS koordinatları, hız, irtifa ve batarya bilgileri Python simülatörü tarafından üretilmekte, PostgreSQL veritabanında saklanmakta ve Grafana üzerinden görüntülenmektedir.

İncelenen çalışmadan farklı olarak geliştirilen proje, konteyner tabanlı sanallaştırmaya, veri kalıcılığına, hata yönetimine ve düşük kaynak tüketimine odaklanmaktadır.

Itkin vd. (2016) tarafından geliştirilen sistemde MongoDB, ExpressJS, AngularJS ve NodeJS teknolojileri kullanılmıştır.

Bu projede ise Python, PostgreSQL, Grafana, Docker ve Docker Compose teknolojileri tercih edilmiştir.

Literatürdeki çalışma çoklu İHA yönetimi ve uçuş kontrolü üzerine yoğunlaşırken geliştirilen proje, telemetri verilerinin düzenli üretilmesi, kalıcı olarak saklanması, görselleştirilmesi ve bulut ortamında konteynerler ile çalıştırılması üzerine yoğunlaşmaktadır.

Çoklu İHA yönetimi ve çarpışma önleme mekanizmaları mevcut projenin kapsamına dahil edilmemiştir.

Bu nedenle iki sistem benzer bir izleme problemini farklı kapsam ve mimari tercihlerle ele almaktadır.

Kaynak: https://doi.org/10.3390/s16111913

## 3. Sanal Makineler ve Konteyner Performansı

### 3.1. Felter, Ferreira, Rajamony ve Rubio (2015)

**Çalışmanın adı:** An Updated Performance Comparison of Virtual Machines and Linux Containers

**Çalışmanın amacı:**

Geleneksel sanal makineler ile Linux konteynerlerinin performans özelliklerini karşılaştırmaktır.

**Kullanılan yöntem:**

Araştırmacılar, hipervizör tabanlı sanallaştırmayı temsil etmek için KVM, konteyner tabanlı sanallaştırmayı temsil etmek için Docker kullanmışlardır.

Farklı iş yükleri altında işlemci, bellek, ağ ve depolama performansı açısından karşılaştırmalar gerçekleştirilmiştir.

**Çalışmanın sonucu:**

Konteynerlerin incelenen durumların büyük bölümünde sanal makinelerle eşit veya daha iyi performans gösterdiği belirtilmiştir.

Yoğun giriş ve çıkış işlemleri gerektiren uygulamalarda her iki teknolojinin de yapılandırma optimizasyonuna ihtiyaç duyabileceği ifade edilmiştir.

**Geliştirilen proje ile ilişkisi:**

Bu projede Python simülatörü, PostgreSQL ve Grafana ayrı Docker konteynerleri içerisinde çalıştırılmaktadır.

AWS EC2 sanal sunucusu üzerinde gerçekleştirilen altı ölçüm sonucunda konteynerlerin toplam ortalama CPU kullanımı %0.462, toplam ortalama RAM kullanımı ise 342.15 MiB olarak hesaplanmıştır.

| Konteyner | Ortalama CPU kullanımı | Ortalama RAM kullanımı |
|---|---:|---:|
| Python simülatörü | %0.068 | 19.39 MiB |
| PostgreSQL | %0.053 | 59.45 MiB |
| Grafana | %0.340 | 263.32 MiB |
| Toplam | %0.462 | 342.15 MiB |

Toplam değerler, yuvarlanmamış ölçüm sonuçları kullanılarak hesaplanmıştır.

Bu sonuçlar mevcut sistemin tek İHA simülasyonu altında sınırlı donanım kaynaklarıyla çalışabildiğini göstermektedir.

AWS ortamında gerçekleştirilen tam simülasyon testinde 501.48 saniye içerisinde 500 telemetri kaydı başarıyla veritabanına kaydedilmiştir.

Ancak projede Docker ile geleneksel sanal makineler arasında karşılaştırmalı bir performans deneyi yapılmamıştır.

Bu nedenle kullanılan Docker altyapısının diğer sanallaştırma yöntemlerinden daha başarılı olduğu yönünde doğrudan bir sonuç çıkarılmamıştır.

İncelenen çalışma, projede tercih edilen konteyner tabanlı sanallaştırma yaklaşımının teorik dayanaklarından birini oluşturmaktadır.

Kaynak: https://doi.org/10.1109/ISPASS.2015.7095802

## 4. Bulut Bilişimin Teorik Temelleri

### 4.1. Mell ve Grance (2011)

**Çalışmanın adı:** The NIST Definition of Cloud Computing

**Yayının amacı:**

Bulut bilişim kavramını, temel özelliklerini, hizmet modellerini ve dağıtım modellerini tanımlamaktır.

**Bulut bilişimin temel özellikleri:**

- İsteğe bağlı self servis.
- Geniş ağ erişimi.
- Kaynak havuzlama.
- Hızlı esneklik.
- Ölçülebilir hizmet.

**Bulut bilişim hizmet modelleri:**

- IaaS: Hizmet olarak altyapı.
- PaaS: Hizmet olarak platform.
- SaaS: Hizmet olarak yazılım.

**Bulut bilişim dağıtım modelleri:**

- Genel bulut (Public Cloud).
- Özel bulut (Private Cloud).
- Hibrit bulut (Hybrid Cloud).
- Topluluk bulutu (Community Cloud).

**Geliştirilen proje ile ilişkisi:**

Projede Amazon EC2 kullanılarak bulut ortamında sanal bir sunucu oluşturulmuştur.

Amazon EC2, sanal işlemci, bellek, depolama ve ağ kaynaklarının kullanılmasına olanak sağlayan bir IaaS hizmetidir.

Projede genel bulut dağıtım modeli kapsamında AWS altyapısından yararlanılmıştır.

Geliştirilen uygulama ve veritabanı bu sanal sunucu üzerinde Docker Compose kullanılarak çalıştırılmıştır.

AWS EC2 sunucusunun temel özellikleri aşağıdaki gibidir:

| Özellik | Değer |
|---|---|
| Bulut sağlayıcısı | Amazon Web Services |
| Bulut hizmeti | Amazon EC2 |
| Hizmet modeli | IaaS |
| Sunucu tipi | t3.small |
| Sanal işlemci | 2 vCPU |
| Bellek | 2 GiB RAM |
| İşletim sistemi | Ubuntu 26.04.1 LTS |
| Sanallaştırma türü | HVM |
| Bulut bölgesi | eu-north-1 (Stockholm) |
| Konteyner teknolojisi | Docker |
| Konteyner yönetimi | Docker Compose |

Sunucuya uzaktan erişilebilmesi, gerektiğinde başlatılıp durdurulabilmesi ve kaynak kullanımının ölçülebilmesi bulut bilişim yaklaşımının uygulamadaki örnekleridir.

Uygulama bileşenleri AWS EC2 sanal makinesi içerisinde ayrı Docker konteynerleri olarak çalıştırılmıştır.

Böylece sanal makine tabanlı altyapı ile konteyner tabanlı sanallaştırma birlikte kullanılmıştır.

Kaynak: https://doi.org/10.6028/NIST.SP.800-145

## 5. Docker ve Uygulama Taşınabilirliği

### 5.1. Merkel (2014)

**Çalışmanın adı:** Docker: Lightweight Linux Containers for Consistent Development and Deployment

**Yayının amacı:**

Docker teknolojisinin uygulama geliştirme ve dağıtım süreçlerinde sağladığı taşınabilirliği ve bağımlılık yönetimini açıklamaktır.

**Çalışmanın içeriği:**

Uygulamaların gerekli bağımlılıklarıyla birlikte konteynerler içerisinde paketlenmesi, farklı çalışma ortamları arasında ortaya çıkabilecek uyumluluk sorunlarının azaltılmasına yardımcı olmaktadır.

Konteyner tabanlı sanallaştırma, uygulamaların birbirinden izole edilmesine ve çalışma ortamlarının daha tutarlı biçimde oluşturulmasına olanak sağlamaktadır.

**Geliştirilen proje ile ilişkisi:**

Projenin ilk geliştirme aşaması Windows işletim sistemine sahip yerel bir bilgisayarda gerçekleştirilmiştir.

Daha sonra aynı Docker yapılandırması kullanılarak uygulama AWS EC2 üzerindeki Ubuntu işletim sistemine aktarılmıştır.

Dockerfile, requirements.txt ve compose.yaml dosyaları sayesinde uygulamanın bağımlılıkları tanımlanmış ve bulut ortamında yeniden kurulabilmesi sağlanmıştır.

Projede üç temel konteyner bulunmaktadır:

- Python telemetri simülatörü.
- PostgreSQL veritabanı.
- Grafana izleme uygulaması.

Konteynerler Docker Compose aracılığıyla yönetilmektedir.

PostgreSQL ve Grafana verilerinin kalıcı olarak saklanması için Docker volume yapısı kullanılmıştır.

Konteynerlerin kaldırılıp yeniden oluşturulmasının ardından PostgreSQL veritabanındaki 1233 kaydın sayısal olarak korunduğu deneysel olarak doğrulanmıştır.

Bu süreç Docker teknolojisinin uygulama taşınabilirliği, yeniden kurulabilirlik ve veri kalıcılığı açısından sağladığı faydalara örnek oluşturmaktadır.

Kaynak: https://www.linuxjournal.com/content/docker-lightweight-linux-containers-consistent-development-and-deployment

## 6. Literatür Karşılaştırması

### 6.1. Teknolojik ve Mimari Karşılaştırma

| Çalışma | Odak noktası | Proje ile benzerliği | Projenin farklılığı |
|---|---|---|---|
| Itkin vd. (2016) | Bulut tabanlı İHA izleme ve yönetimi | Telemetri, GPS, harita ve uzaktan izleme | Python, Docker, PostgreSQL ve Grafana odaklı sadeleştirilmiş mimari |
| Felter vd. (2015) | Sanal makine ve konteyner performansı | Docker ve kaynak tüketimi | İHA telemetri uygulaması üzerinde kaynak ve kayıt performansı ölçümü |
| Mell ve Grance (2011) | Bulut bilişim kavramları ve hizmet modelleri | IaaS ve uzaktan erişim | AWS EC2 üzerinde uygulamalı sistem geliştirme |
| Merkel (2014) | Docker ve uygulama taşınabilirliği | Konteynerleştirme ve bağımlılık yönetimi | Windows ortamından AWS Ubuntu sunucusuna telemetri uygulamasının aktarılması |

### 6.2. Deneysel Sonuçların Değerlendirilmesi

Geliştirilen sistemin kayıt performansı, kaynak tüketimi, hata yönetimi ve veri kalıcılığı deneysel olarak değerlendirilmiştir.

| Performans ölçütü | Elde edilen sonuç |
|---|---|
| Ortalama toplam konteyner CPU kullanımı | %0.462 |
| Ortalama toplam konteyner RAM kullanımı | 342.15 MiB |
| Kaynak tüketimi ölçüm sayısı | 6 |
| 60 saniyelik veri üretim testi | 60 kayıt |
| Ortalama kayıt aralığı | 1.0169 saniye |
| Minimum kayıt aralığı | 1 saniye |
| Maksimum kayıt aralığı | 2 saniye |
| Veri kalıcılığı testi | 1233 kayıt korundu |
| AWS tam simülasyon süresi | 501.48 saniye |
| AWS toplam kayıt girişimi | 500 |
| AWS başarılı kayıt sayısı | 500 |
| AWS başarısız kayıt sayısı | 0 |
| AWS belirsiz girişim sayısı | 0 |
| AWS gözlemlenen hata oranı | %0 |
| AWS gözlemlenen başarı oranı | %100 |
| AWS ortalama başarılı kayıt hızı | 0.997 kayıt/saniye |
| CSV veri setindeki kayıt sayısı | 1648 |

Kaynak tüketimi ölçümleri ve tam simülasyon testi farklı deney oturumlarında gerçekleştirilmiştir.

AWS ortamında gerçekleştirilen tam simülasyon öncesinde veritabanında 1648 kayıt bulunmaktadır.

Simülasyon sonunda toplam kayıt sayısı 2148 olmuştur.

Böylece 500 yeni kaydın veritabanına eklendiği SQL sorgusu ile doğrulanmıştır.

Ortalama başarılı kayıt hızı aşağıdaki şekilde hesaplanmıştır:

    Ortalama kayıt hızı =
        Başarılı kayıt sayısı / Test süresi

    Ortalama kayıt hızı =
        500 / 501.48

    Ortalama kayıt hızı =
        0.997 kayıt/saniye

Elde edilen sonuç, sistemin yaklaşık saniyede bir telemetri kaydı oluşturma hedefini mevcut deney koşullarında karşılayabildiğini göstermektedir.

Felter vd. (2015) tarafından gerçekleştirilen performans incelemesi, konteyner tabanlı sanallaştırma tercihinin teorik dayanağını desteklemektedir.

Bununla birlikte mevcut projede farklı sanallaştırma teknolojileri aynı iş yükü altında karşılaştırılmamıştır.

Itkin vd. (2016) tarafından gerçekleştirilen çalışma ile geliştirilen sistem arasında bulut tabanlı izleme ve telemetri görselleştirme açısından benzerlik bulunmaktadır.

Ancak kullanılan donanım, yazılım mimarisi, İHA sayısı ve deney koşulları farklı olduğundan doğrudan sayısal üstünlük karşılaştırması yapılmamıştır.

### 6.3. Kontrollü Hata Yönetimi Deneyi

Sistemin normal çalışma koşullarındaki kayıt performansının yanı sıra geçersiz veriler karşısındaki davranışı da incelenmiştir.

Bu amaçla üç farklı deney gerçekleştirilmiştir:

1. Yerel ortamda normal çalışma testi.
2. Yerel ortamda kontrollü hata testi.
3. AWS ortamında tam simülasyon testi.

| Ölçüt | Yerel normal test | Kontrollü hata testi | AWS normal test |
|---|---:|---:|---:|
| Toplam kayıt girişimi | 15 | 19 | 500 |
| Başarılı kayıt | 15 | 16 | 500 |
| Başarısız kayıt | 0 | 3 | 0 |
| Test süresi (saniye) | 14.66 | 18.42 | 501.48 |
| Hata oranı | %0 | %15.79 | %0 |
| Başarı oranı | %100 | %84.21 | %100 |
| Belirsiz girişim | 0 | 0 | 0 |

Başarı ve hata oranları aşağıdaki formüller kullanılarak hesaplanmıştır:

    Başarı oranı (%) =
        (Başarılı kayıt / Toplam girişim) x 100

    Hata oranı (%) =
        (Başarısız kayıt / Toplam girişim) x 100

    Belirsiz girişim =
        Toplam girişim -
        Başarılı kayıt -
        Başarısız kayıt

Kontrollü hata testinde simulator/hata_testi.py dosyası kullanılmıştır.

Her beşinci telemetri girişiminde drone_id alanına bilerek None değeri atanmıştır.

PostgreSQL veritabanının NOT NULL kısıtı nedeniyle üç geçersiz kayıt reddedilmiştir.

Rollback mekanizması sayesinde başarısız işlemler geri alınmış ve simülatör sonraki geçerli kayıtları işlemeye devam etmiştir.

Kontrollü deneyde ölçülen hata oranı:

    Hata oranı = (3 / 19) x 100

    Hata oranı = %15.79

Kontrollü deneyde ölçülen başarı oranı:

    Başarı oranı = (16 / 19) x 100

    Başarı oranı = %84.21

Kontrollü deneyde ölçülen %15.79 hata oranı, normal çalışma sırasında kendiliğinden oluşan bir hata oranı değildir. Bilerek oluşturulan geçersiz kayıt girişimlerinin sonucudur.

Test sırasında oluşturulan üç geçersiz kayıt girişiminin tamamı PostgreSQL tarafından reddedilmiştir.

Normal AWS testinde ise 500 girişimin tamamı başarıyla sonuçlanmıştır.

Bu sonuçlar geliştirilen sistemin mevcut deney koşullarında düzenli veri üretebildiğini ve test edilen veri bütünlüğü hatalarını yönetebildiğini göstermektedir.

Deneysel sonuçlar sistemin her koşulda hatasız çalışacağını garanti etmemektedir.

### 6.4. Veri Kalıcılığı ve Yeniden Kurulabilirlik

Docker konteynerleri kaldırılıp yeniden oluşturulduğunda veritabanındaki kayıtların korunup korunmadığı test edilmiştir.

| Ölçüt | Sonuç |
|---|---:|
| Konteynerler kaldırılmadan önceki kayıt sayısı | 1233 |
| Konteynerler yeniden oluşturulduktan sonraki kayıt sayısı | 1233 |
| Kayıt sayısı bazında korunma oranı | %100 |

Docker volume kullanımı sayesinde konteynerlerin yaşam döngüsünden bağımsız olarak veritabanı verilerinin saklanması sağlanmıştır.

Bu sonuç Merkel (2014) tarafından ele alınan konteyner tabanlı uygulama dağıtımı yaklaşımıyla ilişkilendirilebilir.

Ancak veri kalıcılığı testi kayıt sayısı üzerinden gerçekleştirilmiştir. Kayıtların bütün alanları içerik bazında karşılaştırılmamıştır.

### 6.5. Deneysel Veri Seti ve Test Kanıtları

AWS EC2 üzerinde çalışan PostgreSQL veritabanından 1648 telemetri kaydı CSV formatında dışa aktarılmıştır.

Oluşturulan veri seti aşağıdaki alanları içermektedir:

- id
- drone_id
- timestamp
- latitude
- longitude
- speed
- altitude
- battery

Veri seti proje deposunda aşağıdaki konumda bulunmaktadır:

    data/sample_telemetry.csv

CSV dosyasında başlık satırı dahil olmak üzere toplam 1649 satır bulunmaktadır.

Veri seti, 500 kayıtlık son AWS tam simülasyon testinden önce dışa aktarılmıştır. Bu nedenle CSV dosyasında 1648 kayıt bulunurken son AWS testi tamamlandığında veritabanındaki toplam kayıt sayısı 2148 olmuştur.

AWS tam simülasyon testinin ham terminal çıktıları aşağıdaki dosyada saklanmaktadır:

    docs/test-evidence/aws-telemetry-test.log

Ayrıntılı deneysel değerlendirmeler ise aşağıdaki dosyada belgelenmiştir:

    docs/test-results.md

Bu dosyalar deneysel sonuçların incelenebilmesine ve proje kapsamında gerçekleştirilen testlerin belgelenmesine katkı sağlamaktadır.

## 7. Geliştirilen Projenin Katkıları

Literatürde incelenen yaklaşımlar doğrultusunda geliştirilen sistemin uygulamaya yönelik katkıları aşağıdaki gibidir:

- Python ile İHA telemetri verilerinin simüle edilmesi.
- Telemetri verilerinin PostgreSQL veritabanında kalıcı olarak saklanması.
- Grafana ile GPS, hız, irtifa ve batarya bilgilerinin görselleştirilmesi.
- Düşük batarya seviyesinin terminal ve izleme paneli üzerinden takip edilebilmesi.
- Uygulama bileşenlerinin ayrı Docker konteynerleri içerisinde çalıştırılması.
- Docker Compose ile merkezi konteyner yönetiminin sağlanması.
- Sistemin AWS EC2 bulut sunucusuna aktarılması.
- SSH tüneli üzerinden uzaktan erişimin sağlanması.
- CPU ve RAM tüketiminin deneysel olarak ölçülmesi.
- Docker volume kullanımının veri kalıcılığı açısından test edilmesi.
- Veritabanı kayıt hatalarının yakalanması.
- Rollback mekanizması ile başarısız işlemlerin geri alınması.
- Başarılı ve başarısız kayıtların sayısal olarak ölçülmesi.
- Hata ve başarı oranlarının otomatik hesaplanması.
- Sonucu belirsiz kayıt girişimlerinin takip edilmesi.
- Kontrollü hata senaryosunun oluşturulması ve test edilmesi.
- AWS ortamında tam batarya döngüsü boyunca performans testi yapılması.
- 1648 simülasyon kaydından oluşan CSV veri setinin hazırlanması.
- Deneysel sonuçların ham test çıktılarıyla belgelenmesi.
- Sistem mimarisinin ve yazılım davranışının diyagramlarla belgelenmesi.
- Git ve GitHub kullanılarak proje geliştirme sürecinin sürüm kontrolü altında tutulması.

Gerçekleştirilen veri kayıt performansı testinde 60 saniye içerisinde 60 yeni telemetri kaydı oluşturulmuştur.

Veri kalıcılığı testinde ise konteynerler kaldırılıp yeniden oluşturulmasına rağmen 1233 kaydın sayısal olarak korunduğu doğrulanmıştır.

AWS ortamında gerçekleştirilen tam simülasyon testinde 501.48 saniye içerisinde 500 telemetri kaydının tamamı başarıyla veritabanına kaydedilmiştir.

Kontrollü hata testinde geçersiz kayıtların reddedildiği ve simülatörün sonraki geçerli kayıtları işlemeye devam ettiği gözlemlenmiştir.

Projenin temel katkısı, söz konusu teknolojilerin eğitim amaçlı, yeniden kurulabilir, ölçülebilir ve sınırlı kaynak gereksinimine sahip bir İHA telemetri izleme sistemi içerisinde bütünleştirilmesidir.

### 7.1. Projenin Literatürden Ayrılan Yönleri

Geliştirilen sistemin literatürde incelenen çalışmalardan ayrılan temel yönü, bulut bilişim ve sanallaştırma teknolojilerinin eğitim amaçlı bir İHA telemetri uygulaması üzerinde birlikte değerlendirilmesidir.

Proje yalnızca telemetri verilerinin görselleştirilmesine değil, aynı zamanda aşağıdaki konulara odaklanmaktadır:

- Konteyner tabanlı uygulama dağıtımı.
- Bulut ortamında uygulama ve veritabanı yönetimi.
- Veri kalıcılığı.
- Kaynak tüketiminin ölçülmesi.
- Kayıt performansının değerlendirilmesi.
- Kontrollü hata yönetimi.
- Uygulamanın farklı ortamlarda yeniden kurulabilmesi.

Projenin amacı yeni bir sanallaştırma algoritması geliştirmek veya literatürdeki sistemlerden daha yüksek performans elde edildiğini kanıtlamak değildir.

Temel amaç, mevcut teknolojileri bütünleştirerek çalışan ve deneysel olarak değerlendirilebilen bir sistem ortaya koymaktır.

## 8. Araştırmanın Sınırlılıkları

- Gerçek İHA verileri yerine simülasyon verileri kullanılmıştır.
- Yalnızca tek İHA simülasyonu gerçekleştirilmiştir.
- Çoklu İHA yönetimi ve uçuş kontrolü gerçekleştirilmemiştir.
- Uzun süreli performans ve yüksek yük testleri yapılmamıştır.
- AWS tam simülasyon testi yaklaşık 8 dakika 21 saniye ile sınırlıdır.
- CPU ve RAM kullanımı altı örnek ölçüm üzerinden değerlendirilmiştir.
- Konteyner teknolojileri arasında karşılaştırmalı deney gerçekleştirilmemiştir.
- Literatürde incelenen çalışmalarla aynı deney ortamı kullanılmadığından doğrudan sayısal performans karşılaştırması yapılmamıştır.
- Kontrollü hata deneyi yerel ortamda gerçekleştirilmiştir.
- Kontrollü hata testi yalnızca NOT NULL kısıtının ihlal edilmesini kapsamaktadır.
- Ağ kesintisi ve sunucu arızası altında otomatik kurtarma testleri yapılmamıştır.
- Otomatik veritabanı yeniden bağlanma mekanizması bulunmamaktadır.
- Normal testlerde gözlemlenen %0 hata oranı tüm çalışma koşullarına genellenemez.
- Veri kalıcılığı kayıt sayısı üzerinden doğrulanmıştır; içeriklerin tamamı karşılaştırılmamıştır.
- Literatür incelemesi seçilmiş dört temel yayınla sınırlıdır.
- Kapsamlı bir sistematik literatür taraması gerçekleştirilmemiştir.

### 8.1. Gelecekte Yapılabilecek Çalışmalar

Mevcut sistem aşağıdaki geliştirmeler ile genişletilebilir:

- Gerçek İHA telemetri verilerinin sisteme aktarılması.
- Birden fazla İHA'nın eş zamanlı olarak izlenmesi.
- Yüksek veri üretim hızları altında performans testlerinin gerçekleştirilmesi.
- Uzun süreli kaynak tüketimi ölçümlerinin yapılması.
- Otomatik veritabanı yeniden bağlanma mekanizmasının geliştirilmesi.
- Ağ kesintisi ve bağlantı hatalarına karşı kurtarma mekanizmalarının oluşturulması.
- Farklı sanallaştırma teknolojilerinin aynı iş yükü altında karşılaştırılması.
- Telemetri verilerinin anomali tespiti yöntemleriyle analiz edilmesi.
- Gerçek zamanlı bildirim ve alarm mekanizmalarının geliştirilmesi.
- Veri bütünlüğünün içerik bazlı doğrulama yöntemleriyle test edilmesi.

## 9. Genel Değerlendirme

İncelenen çalışmalar, bulut bilişim ve konteyner tabanlı uygulama dağıtımının uzaktan izleme sistemlerinde kullanılabileceğini göstermektedir.

Geliştirilen projede bu yaklaşımlar bir araya getirilerek İHA telemetri verilerinin üretilmesi, saklanması ve görselleştirilmesi sağlanmıştır.

Python simülatörü, PostgreSQL veritabanı ve Grafana izleme uygulaması Docker konteynerleri içerisinde çalıştırılmıştır.

Docker Compose kullanılarak uygulama bileşenlerinin yönetilmesi ve AWS EC2 bulut sunucusu üzerinde yeniden kurulması sağlanmıştır.

Kaynak tüketimi ölçümlerinde konteynerlerin toplam ortalama CPU kullanımı %0.462, toplam ortalama RAM kullanımı ise 342.15 MiB olarak hesaplanmıştır.

AWS ortamında gerçekleştirilen tam simülasyon testinde 501.48 saniye içerisinde 500 telemetri kaydının tamamı başarıyla veritabanına kaydedilmiştir.

Bu deneyde gözlemlenen başarı oranı %100, hata oranı ise %0 olarak hesaplanmıştır.

Kontrollü hata deneyinde geçersiz verilerin PostgreSQL tarafından reddedildiği ve rollback işleminin ardından geçerli kayıtların işlenmeye devam ettiği gözlemlenmiştir.

Veri kalıcılığı testinde konteynerlerin kaldırılıp yeniden oluşturulmasına rağmen 1233 kaydın sayısal olarak korunduğu doğrulanmıştır.

Deneysel sonuçlar, geliştirilen sistemin belirlenen temel gereksinimleri mevcut test koşulları altında karşılayabildiğini göstermektedir.

Kaynak tüketimi ölçümleri, geliştirilen sistemin tek İHA iş yükü altında sınırlı donanım kaynakları ile çalışabildiğini göstermektedir.

Projenin temel katkısı yeni bir sanallaştırma algoritması geliştirmek değil; bulut bilişim, konteyner tabanlı sanallaştırma, veri yönetimi, izleme ve hata yönetimi teknolojilerini uygulamalı bir sistem içerisinde bütünleştirmektir.

Sonuç olarak geliştirilen sistem, bulut bilişim ve sanallaştırma teknolojilerinin İHA telemetri izleme uygulamalarında kullanılmasına yönelik eğitim amaçlı, yeniden kurulabilir ve deneysel olarak değerlendirilebilir bir örnek oluşturmaktadır.

## 10. Kaynakça

Felter, W., Ferreira, A., Rajamony, R., & Rubio, J. (2015). An updated performance comparison of virtual machines and Linux containers. 2015 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS), 171–172. https://doi.org/10.1109/ISPASS.2015.7095802

Itkin, M., Kim, M., & Park, Y. (2016). Development of cloud-based UAV monitoring and management system. Sensors, 16(11), 1913. https://doi.org/10.3390/s16111913

Mell, P., & Grance, T. (2011). The NIST definition of cloud computing (NIST Special Publication 800-145). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-145

Merkel, D. (2014). Docker: Lightweight Linux containers for consistent development and deployment. Linux Journal, 2014(239). https://www.linuxjournal.com/content/docker-lightweight-linux-containers-consistent-development-and-deployment
