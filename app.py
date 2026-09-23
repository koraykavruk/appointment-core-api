# REST API for Online Randevu & Hasta Kayıt Servisi
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import Optional, List
from pathlib import Path

from models import AppointmentModel, AppointmentCreate
from service import AppointmentService

app = FastAPI(
    title="Online Randevu & Hasta Kayıt Servisi",
    description="Built autonomously by DevHive AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

service = AppointmentService()

@app.get("/")
def index():
    static_file = Path("static/index.html")
    if static_file.exists():
        return FileResponse(static_file)
    return {"status": "online", "domain": "Online Randevu & Hasta Kayıt Servisi"}

@app.get("/api/appointments")
def list_items(search: Optional[str] = Query(None)):
    return service.get_all(search)

@app.post("/api/appointments", status_code=201)
def create_item(payload: AppointmentCreate):
    return service.create(payload)

@app.get("/api/appointments/stats")
def get_stats():
    return service.get_stats()
