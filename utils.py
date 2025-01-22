import hashlib
from datetime import datetime, timedelta

def generate_short_url(original_url: str) -> str:
    url_str = str(original_url)
    return hashlib.md5(url_str.encode()).hexdigest()[:6]

def calculate_expiry(expiry_hours: int) -> datetime:
    return datetime.utcnow() + timedelta(hours=expiry_hours)
