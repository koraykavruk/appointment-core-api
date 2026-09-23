# 📖 Online Randevu & Hasta Kayıt Servisi - Kullanıcı Kılavuzu

Bu belge, **DevHive AI** tarafından otonom olarak inşa edilen **appointment-core-api** uygulamasının son kullanıcı ve operasyon ekibi tarafından nasıl kullanılacağını adım adım açıklar.

---

## 1. Uygulama Genel Bakışı
- **Teknoloji Altyapısı:** Python (FastAPI)
- **Yönetilen Varlık:** Randevu (Appointment)
- **Konteyner Desteği:** Docker Desktop 1-Tık Yayını

## 2. Web Arayüzü Nasıl Kullanılır?
1. Tarayıcınızdan uygulamanın canlı adresine (`http://localhost:8080`) gidin.
2. Sol tarafta yer alan **"Yeni Randevu Ekle"** formunu doldurun.
3. **"✓ Kaydet"** butonuna bastığınızda veriniz anında servis katmanına kaydedilir ve sağdaki tabloda güncellenir.
4. Üstteki arama kutucuğunu kullanarak listedeki kayıtları anlık olarak filtreleyebilirsiniz.

## 3. Sıkça Sorulan Sorular (SSS)
- **S: API doğrudan dışarıdan çağrılabilir mi?**  
  C: Evet, `/api/appointments` uç noktası standart JSON REST standardındadır.
