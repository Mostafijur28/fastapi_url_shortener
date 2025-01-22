from sqlalchemy.orm import Session
from models import URL, AccessLog
from utils import generate_short_url, calculate_expiry

def create_short_url(db: Session, original_url: str, expiry_hours: int):
    short_url = generate_short_url(original_url)
    expiration_time = calculate_expiry(expiry_hours)

    existing_url = db.query(URL).filter(URL.original_url == original_url).first()
    if existing_url:
        return existing_url

    db_url = URL(original_url=original_url, shortened_url=short_url, expiration_time=expiration_time)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_original_url(db: Session, short_url: str):
    return db.query(URL).filter(URL.shortened_url == short_url).first()

def log_access(db: Session, short_url: str, ip_address: str):
    access_log = AccessLog(shortened_url=short_url, ip_address=ip_address)
    db.add(access_log)
    db.commit()

def get_analytics(db: Session, short_url: str):
    logs = db.query(AccessLog).filter(AccessLog.shortened_url == short_url).all()
    return logs
