from fastapi import APIRouter
from app.schemas.health import HealthCheck
from app.db.mongodb import db
import logging

router = APIRouter()

@router.get("/health", response_model=HealthCheck)
async def health_check() -> dict:
    db_status = False
    try:
        if db.client:
            await db.client.admin.command('ping')
            db_status = True
    except Exception as e:
        logging.error(f"Health check DB fail: {e}")
        db_status = False
        
    return {"status": "ok", "db_connected": db_status}
