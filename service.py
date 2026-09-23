# Business Logic for Online Randevu & Hasta Kayıt Servisi
from typing import List, Optional
from models import AppointmentModel, AppointmentCreate

class AppointmentService:
    def __init__(self):
        self._items = [{'id': 1, 'patient_name': 'Ahmet Yılmaz', 'doctor_name': 'Dr. Selin Kaya', 'department': 'Dahiliye', 'appointment_date': '2026-09-25', 'appointment_time': '10:00', 'status': 'Onaylandı'}, {'id': 2, 'patient_name': 'Fatma Şahin', 'doctor_name': 'Dr. Murat Çelik', 'department': 'Göz Hastalıkları', 'appointment_date': '2026-09-26', 'appointment_time': '11:30', 'status': 'Bekliyor'}, {'id': 3, 'patient_name': 'Burak Öztürk', 'doctor_name': 'Dr. Ayşe Yılmaz', 'department': 'Kardiyoloji', 'appointment_date': '2026-09-27', 'appointment_time': '15:00', 'status': 'Tamamlandı'}]
        self._counter = 4

    def get_all(self, search: Optional[str] = None) -> List[dict]:
        if not search:
            return self._items
        s = search.lower()
        return [
            item for item in self._items
            if any(s in str(v).lower() for v in item.values())
        ]

    def get_by_id(self, item_id: int) -> Optional[dict]:
        for item in self._items:
            if item.get("id") == item_id:
                return item
        return None

    def create(self, data: AppointmentCreate) -> dict:
        new_item = data.model_dump()
        new_item["id"] = self._counter
        self._counter += 1
        self._items.append(new_item)
        return new_item

    def get_stats(self) -> dict:
        return {
            "total_count": len(self._items),
            "status": "HEALTHY",
            "entity": "Appointment"
        }
