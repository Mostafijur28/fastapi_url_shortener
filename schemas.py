from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class ShortenRequest(BaseModel):
    original_url: HttpUrl
    expiry_hours: Optional[int] = 24

class ShortenResponse(BaseModel):
    shortened_url: str
    expiration_time: datetime

class AnalyticsResponse(BaseModel):
    shortened_url: str
    access_count: int
    access_logs: list
