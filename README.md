# ♻️ Geri Dönüşüm Ayrıştırma Konveyör Bandı (Recycling Sorter)

Mekatronik Mühendisliği bitirme projesi kapsamında 4 kişilik bir ekip olarak geliştirdiğimiz, görüntü işleme tabanlı otonom atık ayrıştırma sistemi. 

Projenin asıl olayı; üretim/ayrıştırma bandında ilerleyen malzemeleri gerçek zamanlı olarak kameradan okuyup, yapay zeka ile ne olduğunu anlayarak donanımsal olarak doğru yerlere yönlendirmektir.

## 🛠 Donanım ve Kullanılan Teknolojiler

* **Görüntü İşleme:** Raspberry Pi 4 Model B (YOLOv8)
* **Alt Seviye Kontrolcü:** STM32F429I-DISCO
* **Arayüz (HMI):** Nextion Ekran
* **Motor & Sürücü:** L298N ile sürülen DC Fırçasız Motor
* **Haberleşme:** UART

## ⚙️ Sistem Nasıl Çalışıyor?

Sistemin akışı genel olarak 3 adımdan oluşuyor:

1. **Teşhis:** Bant üzerinde akan atığın görüntüsü Raspberry Pi üzerinden YOLOv8 ile işleniyor ve nesnenin sınıfı (plastik, metal, cam vs.) tespit ediliyor.
2. **Haberleşme:** Raspberry Pi, tespit ettiği nesne bilgisini bekleme yapmadan **UART** üzerinden STM32'ye basıyor.
3. **Donanım ve Arayüz Kontrolü:** STM32 gelen bu veriye göre eyleme geçiyor. L298N üzerinden bant hızını ayarlıyor ve ayrıştırıcı mekanizmayı tetikliyor. Aynı zamanda Nextion HMI ekrana da güncel ayrıştırma verilerini gönderip arayüzü güncelliyor.

## 🚀 Repoyu Kullanma

Projeyi lokalde denemek veya kodları incelemek isterseniz:

```bash
git clone [https://github.com/mehmetefedaver/Recycling-Sorter-Band.git](https://github.com/mehmetefedaver/Recycling-Sorter-Band.git)
pip install -r requirements.txt
