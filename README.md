# 🌌 OrbitSim PRO: İnteraktif Kütleçekim & Fizik Motoru

**OrbitSim PRO**, Newton'un Evrensel Kütleçekim Yasası'nı temel alarak gök cisimlerinin etkileşimlerini simüle eden, yüksek performanslı bir fizik motorudur. Bu proje, kaotik bir güneş sisteminin matematiksel dengesini interaktif bir deneyime dönüştürür.

## 🚀 Öne Çıkan Özellikler

* **Hiyerarşik Kütleçekimi:** Dünya Güneş etrafında dönerken, Ay'ın da Dünya'nın çekimine kapılarak spiral bir yörünge izlediği çiftli sistem simülasyonu.
* **Dinamik Satürn Halkaları:** Bir gezegenin çekim alanına kilitlenmiş 60'tan fazla bağımsız parçacıktan oluşan gerçek zamanlı halka sistemi.
* **Gelişmiş Zaman Kontrolü:** Klavyedeki **Yukarı/Aşağı Ok** tuşları ile zaman akışını (Time Scale) hızlandırma veya yavaşlatma yeteneği.
* **Tam Ekran & Mükemmel Merkezleme:** Özel kamera optimizasyonları ile Güneş'in her zaman ekranın tam geometrik merkezinde kalması sağlanmıştır.
* **İnteraktif Asteroid Sistemi:** Fare tıklamasıyla uzay boşluğuna yeni kütleler ekleme ve bu kütlelerin devasa gezegenler tarafından nasıl saptırıldığını gözlemleme.

## 🏗️ Teknik Mimari

Proje, modüler ve yüksek performanslı üç ana bileşenden oluşur:

1.  **`celestial_body.py`**: Cisimlerin kütle, hız ve konum vektörlerini yöneten nesne yönelimli sınıf yapısı.
2.  **`physics_engine.py`**: Evrensel kütleçekim formülünü kullanarak tüm etkileşimleri anlık hesaplayan vektörel çekirdek.
3.  **`simulator.py`**: `FuncAnimation` ve `Blit` teknolojisi ile yüksek FPS değerlerinde görselleştirme yapan ana orkestratör.

## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

```bash
# Depoyu klonlayın
git clone [https://github.com/kullaniciadin/OrbitSim.git](https://github.com/kullaniciadin/OrbitSim.git)

# Dizine gidin
cd OrbitSim

# Gerekli kütüphaneleri yükle
pip install numpy matplotlib

# Simülasyonu başlat
python simulator.py
