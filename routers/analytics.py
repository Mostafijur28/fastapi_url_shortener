from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import AnalyticsResponse
from service import get_analytics

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/analytics/{short_url}", response_model=AnalyticsResponse)
def analytics(short_url: str, db: Session = Depends(get_db)):
    logs = get_analytics(db, short_url)
    return {
        "shortened_url": short_url,
        "access_count": len(logs),
        "access_logs": [{"ip_address": log.ip_address, "timestamp": log.access_time} for log in logs]
    }
