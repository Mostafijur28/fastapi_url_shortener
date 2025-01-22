from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ShortenRequest, ShortenResponse
from service import create_short_url

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/shorten", response_model=ShortenResponse)
def shorten_url(payload: ShortenRequest, db: Session = Depends(get_db)):
    # Convert the Pydantic Url object to a string
    original_url_str = str(payload.original_url)

    # Pass the string version to the service function
    db_url = create_short_url(db, original_url_str, payload.expiry_hours)
    return {
        "shortened_url": f"http://short.ly/{db_url.shortened_url}",
        "expiration_time": db_url.expiration_time
    }

