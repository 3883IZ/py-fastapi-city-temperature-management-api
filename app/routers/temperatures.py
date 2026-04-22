from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import httpx
from .. import crud, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/temperatures/update')
async def update_temperatures(db: Session = Depends(get_db)):
    cities = crud.get_cities(db)
    async with httpx.AsyncClient() as client:
        for city in cities:
            # тут можна інтегрувати реальний API погоди
            temp_value = 20.0
            temp = schemas.TemperatureCreate(
                city_id=city.id,
                date_time=datetime.utcnow(),
                temperature=temp_value
            )
            crud.create_temperature(db, temp)
    return {'status': 'updated'}

@router.get('/temperatures', response_model=list[schemas.Temperature])
def get_temperatures(city_id: int | None = None, db: Session = Depends(get_db)):
    return crud.get_temperatures(db, city_id)
