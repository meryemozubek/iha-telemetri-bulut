# Literatür Araştırması

## 1. Araştırmanın Amacı

Bu literatür araştırmasının amacı, bulut tabanlı İHA telemetri izleme sistemleri, bulut bilişim ve konteyner tabanlı sanallaştırma teknolojileri üzerine gerçekleştirilen çalışmaları incelemektir.

İncelenen çalışmalar doğrultusunda geliştirilen sistemin teknolojik altyapısı, tasarım tercihleri, mevcut çalışmalarla benzerlikleri ve farklılıkları değerlendirilmiştir.

## 2. Bulut Tabanlı İHA İzleme Sistemleri

### 2.1. Itkin, Kim ve Park (2016)

**Çalışmanın adı:** Development of Cloud-Based UAV Monitoring and Management System

**Çalışmanın amacı:**

İnsansız hava araçlarının bulut ortamında gerçek zamanlı olarak izlenmesini ve yönetilmesini sağlayan bir sistem geliştirmektir.

**Kullanılan yöntem:**

Araştırmacılar, İHA'lardan elde edilen GPS, batarya ve çeşitli sensör verilerinin web tabanlı bir uygulama üzerinden izlenmesini sağlayan bir sistem geliştirmişlerdir. İHA konumları ve uçuş rotaları dinamik harita üzerinde görselleştirilmiştir. Ayrıca sistemde çarpışma önleme mekanizmalarına yer verilmiştir.

**Çalışmanın sonucu:**

Geliştirilen sistemin uygulanabilirliği ve performansı simülasyon ortamında değerlendirilmiştir.

**Geliştirilen proje ile ilişkisi:**

Bu projede de İHA telemetri verilerinin bulut ortamında izlenmesi amaçlanmaktadır. GPS koordinatları, hız, irtifa ve batarya bilgileri Python simülatörü tarafından üretilmekte, PostgreSQL veritabanında saklanmakta ve Grafana üzerinden görüntülenmektedir.

İncelenen çalışmadan farklı olarak geliştirilen proje, konteyner tabanlı sanallaştırmaya, veri kalıcılığına ve düşük kaynak tüketimine odaklanmaktadır.

Çoklu İHA yönetimi ve çarpışma önleme mekanizmaları mevcut projenin kapsamına dahil edilmemiştir.

Kaynak: https://doi.org/10.3390/s16111913

## 3. Sanal Makineler ve Konteyner Performansı

### 3.1. Felter, Ferreira, Rajamony ve Rubio (2015)

**Çalışmanın adı:** An Updated Performance Comparison of Virtual Machines and Linux Containers

**Çalışmanın amacı:**

Geleneksel sanal makineler ile Linux konteynerlerinin performans özelliklerini karşılaştırmaktır.

**Kullanılan yöntem:**

Araştırmacılar, hipervizör tabanlı sanallaştırmayı temsil etmek için KVM, konteyner tabanlı sanallaştırmayı temsil etmek için Docker kullanmışlardır. Farklı iş yükleri altında performans karşılaştırmaları gerçekleştirilmiştir.

**Çalışmanın sonucu:**

Konteynerlerin incelenen durumların büyük bölümünde sanal makinelerle eşit veya daha iyi performans gösterdiği belirtilmiştir. Yoğun giriş ve çıkış işlemleri gerektiren uygulamalarda her iki teknolojinin de yapılandırma optimizasyonuna ihtiyaç duyabileceği ifade edilmiştir.

**Geliştirilen proje ile ilişkisi:**

Bu projede Python simülatörü, PostgreSQL ve Grafana ayrı Docker konteynerleri içerisinde çalıştırılmaktadır.

AWS EC2 sanal sunucusu üzerinde gerçekleştirilen altı ölçüm sonucunda konteynerlerin toplam ortalama CPU tüketimi %0.462, toplam ortalama RAM tüketimi ise 342.15 MiB olarak hesaplanmıştır.

Bu sonuçlar mevcut sistemin tek İHA simülasyonu altında düşük kaynak tüketimiyle çalışabildiğini göstermektedir.

Ancak projede Docker ile geleneksel sanal makineler arasında karşılaştırmalı bir performans deneyi yapılmamıştır. Bu nedenle kullanılan Docker altyapısının diğer sanallaştırma yöntemlerinden daha başarılı olduğu yönünde doğrudan bir sonuç çıkarılmamıştır.

Kaynak: https://doi.org/10.1109/ISPASS.2015.7095802

## 4. Bulut Bilişimin Teorik Temelleri

### 4.1. Mell ve Grance (2011)

**Çalışmanın adı:** The NIST Definition of Cloud Computing

**Yayının amacı:**

Bulut bilişim kavramını, temel özelliklerini, hizmet modellerini ve dağıtım modellerini tanımlamaktır.

**Bulut bilişimin temel özellikleri:**

- İsteğe bağlı self servis
- Geniş ağ erişimi
- Kaynak havuzlama
- Hızlı esneklik
- Ölçülebilir hizmet

**Bulut bilişim hizmet modelleri:**

- IaaS: Hizmet olarak altyapı
- PaaS: Hizmet olarak platform
- SaaS: Hizmet olarak yazılım

**Geliştirilen proje ile ilişkisi:**

Projede Amazon EC2 kullanılarak bulut ortamında sanal bir sunucu oluşturulmuştur.

Amazon EC2, sanal işlemci, bellek, depolama ve ağ kaynaklarının kullanılmasına olanak sağlayan bir IaaS hizmetidir.

Geliştirilen uygulama ve veritabanı bu sanal sunucu üzerinde Docker Compose kullanılarak çalıştırılmıştır.

Sunucuya uzaktan erişilebilmesi, gerektiğinde başlatılıp durdurulabilmesi ve kaynak kullanımının ölçülebilmesi bulut bilişim yaklaşımının uygulamadaki örnekleridir.

Kaynak: https://doi.org/10.6028/NIST.SP.800-145

## 5. Docker ve Uygulama Taşınabilirliği

### 5.1. Merkel (2014)

**Çalışmanın adı:** Docker: Lightweight Linux Containers for Consistent Development and Deployment

**Yayının amacı:**

Docker teknolojisinin uygulama geliştirme ve dağıtım süreçlerinde sağladığı taşınabilirliği ve bağımlılık yönetimini açıklamaktır.

**Çalışmanın içeriği:**

Uygulamaların gerekli bağımlılıklarıyla birlikte konteynerler içerisinde paketlenmesi, farklı çalışma ortamları arasında ortaya çıkabilecek uyumluluk sorunlarının azaltılmasına yardımcı olmaktadır.

**Geliştirilen proje ile ilişkisi:**

Projenin ilk geliştirme aşaması Windows işletim sistemine sahip yerel bir bilgisayarda gerçekleştirilmiştir.

Daha sonra aynı Docker yapılandırması kullanılarak uygulama AWS EC2 üzerindeki Ubuntu işletim sistemine aktarılmıştır.

Dockerfile, requirements.txt ve compose.yaml dosyaları sayesinde uygulamanın bağımlılıkları tanımlanmış ve bulut ortamında yeniden kurulabilmesi sağlanmıştır.

Bu süreç Docker teknolojisinin uygulama taşınabilirliği açısından sağladığı faydalara örnek oluşturmaktadır.

Kaynak: https://www.seltzer.com/margo/teaching/CS508.19/papers/merkel14.pdf

## 6. Literatür Karşılaştırma Tablosu

| Çalışma | Odak noktası | Proje ile benzerliği | Projenin farklılığı |
|---|---|---|---|
| Itkin vd. (2016) | Bulut tabanlı İHA izleme | Telemetri, GPS, harita ve uzaktan izleme | Docker, PostgreSQL ve Grafana odaklı sadeleştirilmiş mimari |
| Felter vd. (2015) | Sanal makine ve konteyner performansı | Docker ve kaynak tüketimi | İHA telemetri uygulaması üzerinde kaynak ölçümü |
| Mell ve Grance (2011) | Bulut bilişim kavramları | IaaS ve uzaktan erişim | AWS EC2 üzerinde uygulamalı sistem geliştirme |
| Merkel (2014) | Docker ve uygulama taşınabilirliği | Konteynerleştirme ve bağımlılık yönetimi | Windows ortamından AWS Ubuntu sunucusuna telemetri uygulamasının aktarılması |

## 7. Geliştirilen Projenin Katkıları

Literatürde incelenen yaklaşımlar doğrultusunda geliştirilen sistemin uygulamaya yönelik katkıları aşağıdaki gibidir:

- Python ile İHA telemetri verilerinin simüle edilmesi.
- Telemetri verilerinin PostgreSQL veritabanında kalıcı olarak saklanması.
- Grafana ile GPS, hız, irtifa ve batarya bilgilerinin görselleştirilmesi.
- Uygulama bileşenlerinin ayrı Docker konteynerleri içerisinde çalıştırılması.
- Docker Compose ile merkezi konteyner yönetiminin sağlanması.
- Sistemin AWS EC2 bulut sunucusuna aktarılması.
- SSH tüneli üzerinden uzaktan erişimin sağlanması.
- CPU ve RAM tüketiminin deneysel olarak ölçülmesi.
- Docker volume kullanımının veri kalıcılığı açısından test edilmesi.

Gerçekleştirilen veri kayıt performansı testinde 60 saniye içerisinde 60 yeni telemetri kaydı oluşturulmuştur.

Veri kalıcılığı testinde ise konteynerler kaldırılıp yeniden oluşturulmasına rağmen 1233 kaydın sayısal olarak korunduğu doğrulanmıştır.

Projenin temel katkısı, söz konusu teknolojilerin eğitim amaçlı, yeniden kurulabilir ve düşük kaynak gereksinimine sahip bir İHA telemetri izleme sistemi içerisinde bütünleştirilmesidir.

## 8. Araştırmanın Sınırlılıkları

- Gerçek İHA verileri yerine simülasyon verileri kullanılmıştır.
- Yalnızca tek İHA simülasyonu gerçekleştirilmiştir.
- Uzun süreli performans ve yüksek yük testleri yapılmamıştır.
- Konteyner teknolojileri arasında karşılaştırmalı deney gerçekleştirilmemiştir.
- Literatürde incelenen çalışmalarla aynı deney ortamı kullanılmadığından doğrudan sayısal performans karşılaştırması yapılmamıştır.
- Literatür incelemesi seçilmiş dört temel yayınla sınırlıdır.

## 9. Genel Değerlendirme

İncelenen çalışmalar, bulut bilişim ve konteyner tabanlı uygulama dağıtımının uzaktan izleme sistemlerinde kullanılabileceğini göstermektedir.

Geliştirilen projede bu yaklaşımlar bir araya getirilerek İHA telemetri verilerinin üretilmesi, saklanması ve görselleştirilmesi sağlanmıştır.

Deneysel sonuçlar, geliştirilen sistemin belirlenen temel gereksinimleri mevcut test koşulları altında karşılayabildiğini göstermektedir.

## 10. Kaynakça

Felter, W., Ferreira, A., Rajamony, R., & Rubio, J. (2015). An updated performance comparison of virtual machines and Linux containers. 2015 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS), 171–172. https://doi.org/10.1109/ISPASS.2015.7095802

Itkin, M., Kim, M., & Park, Y. (2016). Development of cloud-based UAV monitoring and management system. Sensors, 16(11), 1913. https://doi.org/10.3390/s16111913

Mell, P., & Grance, T. (2011). The NIST definition of cloud computing (NIST Special Publication 800-145). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-145

Merkel, D. (2014). Docker: Lightweight Linux containers for consistent development and deployment. Linux Journal, 2014(239).
