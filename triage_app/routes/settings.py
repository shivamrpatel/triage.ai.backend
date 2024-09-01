from fastapi import APIRouter, Depends, HTTPException
from .. import schemas
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..crud import update_settings, decode_token, get_settings_by_filter, get_settings
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/settings')

@router.get("/id/{id}", response_model=schemas.Settings)
def get_settings_by_id(id: int, db: Session = Depends(get_db), agent_data: schemas.TokenData = Depends(decode_token)):
    settings = get_settings_by_filter(db, filter={'id': id})
    if not settings:
        raise HTTPException(status_code=400, detail=f'No settings found with id {id}')
    return settings

@router.get("/get", response_model=list[schemas.Settings])
def get_all_settingss(db: Session = Depends(get_db), agent_data: schemas.TokenData = Depends(decode_token)):
    return get_settings(db)

@router.put("/put/{id}", response_model=schemas.Settings)
def settings_update(id: int, updates: schemas.SettingsUpdate, db: Session = Depends(get_db), agent_data: schemas.TokenData = Depends(decode_token)):
    settings = update_settings(db, id, updates)
    if not settings:
        raise HTTPException(status_code=400, detail=f'Settings with id {id} not found')
    
    return settings

