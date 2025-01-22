from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from database import SessionLocal
from service import get_original_url, log_access
from datetime import datetime
from fastapi import Request
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{short_url}")
def redirect(short_url: str, request: Request, db: Session = Depends(get_db)):
    db_url = get_original_url(db, short_url)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    if db_url.expiration_time < datetime.utcnow():
        raise HTTPException(status_code=404, detail="URL expired")

    log_access(db, short_url, request.client.host)  # Log access
    return RedirectResponse(url=db_url.original_url)
