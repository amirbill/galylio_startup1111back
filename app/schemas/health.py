from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: str
    db_connected: bool = False
