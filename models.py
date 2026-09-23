# Data Models for Online Randevu & Hasta Kayıt Servisi
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AppointmentModel(BaseModel):
    id: Optional[int] = None
    patient_name: str = Field(..., description='Hasta Adı Soyadı', example='Mehmet Demir')
    doctor_name: str = Field(..., description='Doktor', example='Dr. Ayşe Yılmaz')
    department: str = Field(..., description='Poliklinik', example='Kardiyoloji')
    appointment_date: str = Field(..., description='Randevu Tarihi', example='2026-09-28')
    appointment_time: str = Field(..., description='Saat', example='14:30')
    status: str = Field(..., description='Durum', example='Onaylandı')
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class AppointmentCreate(BaseModel):
    patient_name: str = Field(..., description='Hasta Adı Soyadı', example='Mehmet Demir')
    doctor_name: str = Field(..., description='Doktor', example='Dr. Ayşe Yılmaz')
    department: str = Field(..., description='Poliklinik', example='Kardiyoloji')
    appointment_date: str = Field(..., description='Randevu Tarihi', example='2026-09-28')
    appointment_time: str = Field(..., description='Saat', example='14:30')
    status: str = Field(..., description='Durum', example='Onaylandı')
