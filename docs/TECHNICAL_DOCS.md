# ⚙️ Online Randevu & Hasta Kayıt Servisi - Teknik Dokümantasyon

## 1. Mimari Mimarisi
- **Programlama Dili:** Python (FastAPI)
- **Katmanlar:** 
  1. *Presentation Layer (UI):* HTML5, TailwindCSS, Fetch API
  2. *API Gateway / Controller:* REST HTTP Uç Noktaları
  3. *Business Logic Layer:* Appointment CRUD ve istatistik mantığı
  4. *Data Models:* Tip korumalı modeller

## 2. REST API Spesifikasyonu

### `GET /api/appointments`
- **Açıklama:** Kayıtlı tüm Appointments nesnelerini döner.
- **Örnek cURL:**
  ```bash
  curl -X GET http://localhost:8080/api/appointments
  ```

### `POST /api/appointments`
- **Açıklama:** Yeni bir Randevu kaydı oluşturur.
- **Örnek cURL:**
  ```bash
  curl -X POST http://localhost:8080/api/appointments \
       -H "Content-Type: application/json" \
       -d '{"patient_name": "Test"}'
  ```

## 3. Docker Dağıtım Talimatı
```bash
docker build -t devhive-appointment-core-api .
docker run -d -p 8080:8080 devhive-appointment-core-api
```
