# 6番目に作成 この段階では実弾テストはしていない。
# ひとまずDBに必要な情報を整備することができた。main.pyで関数を実行する。

from sqlalchemy.orm import Session
# DBのデータ構造を規定するmodel.pyとFastAPIのデータ構造を規定するschemas.pyをimportする。
from . import models, schemas

# 旅行先一覧を取得
def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LocationDB).offset(skip).limit(limit).all()

# 旅行履歴一覧を取得
def get_travels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TravelDB).offset(skip).limit(limit).all()

# 旅行先登録
# UIでユーザー名を入力→送信ボタンを押す→FastAPI側で送信データを受け取る→受け取ったデータをDBに保存
# 1行目はFastAPI側の話なので、schemas.Location
 
def create_location(db: Session, locationapi: schemas.Location):
# 以降はDB側の話になるので、model.LocationDB
    # インスタンス化
    # models.LocationDBの引数は、location_idとlocation_nameなので、引数名は限定される。
    db_locationapi = models.LocationDB(location_name = locationapi.location_name)
    db.add(db_locationapi)
    db.commit()
    db.refresh(db_locationapi)
    return db_locationapi


def create_travel(db: Session, travelapi: schemas.Travel):
    db_travelapi = models.TravelDB(
        location_id = travelapi.location_id,
        departure_month = travelapi.departure_month,
        days = travelapi.days
        )
    db.add(db_travelapi)
    db.commit()
    db.refresh(db_travelapi)
    return db_travelapi