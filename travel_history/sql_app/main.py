# 1番目に作成
# 7番目に作成 sql_appフォルダの中に移動


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# main.pyはAPIの中枢。 他のpythonファイルを読み込んで使う。
from . import crud, models, schemas
from .database import sessionLocal, engine

from typing import List

# ここでDBを作成。sqliteはDBをファイルとして作成している。
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Read
# responseする場合はFastAPIのデータ型であるschemasのLocationクラス
# shemas.Locationは1つのデータなので、TypingモジュールをimportしてList化する。
@app.get("/locations", response_model=List[schemas.Location])
async def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations_list = crud.get_locations(db, skip=skip, limit=limit)
    return locations_list

@app.get("/travels", response_model=List[schemas.Travel])
async def read_travels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    travels_list = crud.get_travels(db, skip=skip, limit=limit)
    return travels_list



# 最初にテストした関数
#@app.get("/travels")
#async def travels(travels: Travel):
    #return {"travels": travels}




# Create
# Createの場合は、response_modelは単数系でOK
@app.post("/locations", response_model=schemas.Location)
# createするときのデータ構造はCreateLocationなので
async def create_locations(location: schemas.CreateLocation, db: Session = Depends(get_db)):
    return crud.create_location(db=db, locationapi= location)

@app.post("/travels", response_model=schemas.Travel)
async def create_travels(travel: schemas.CreateTravel, db: Session = Depends(get_db)):
    return crud.create_travel(db=db, travelapi= travel)
    


#@app.post("/locations", response_model=schemas.Location)
#async def create_locations(location: schemas.Location, db: Session = Depends(get_db)):
    #create_loc = crud.create_location(db=db, locationapi= location)
    #return create_loc

#@app.post("/travels", response_model=schemas.Travel)
#async def create_travels(travel: schemas.Travel, db: Session = Depends(get_db)):
    #create_tra = crud.create_travel(db=db, travelapi= travel)
    #return create_tra

# 最初にテストした関数
#@app.post("/travels")
#async def travels(travels: Travel):
    #return {"travels": travels}