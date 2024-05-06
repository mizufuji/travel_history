# 5番目に作成 1番最初に作成したmain.pyからお引越し
# 9番目に作成 UIからのフォーム送信でエラーが発生したので、クラスの詳細を変更。

from pydantic import BaseModel

class CreateLocation(BaseModel):
    location_name: str

class Location(CreateLocation):
    location_id: int

# 基本的には辞書型で入ってくるが、sqlalchemyのorm型で入ってきても対応できる
    class Config:
        orm_mode = True

class CreateTravel(BaseModel):
    location_id: int
    departure_month: int
    days: int

class Travel(CreateTravel):
    travel_id: int
    location_id: int

    class Config:
        orm_mode = True



# もともとあったクラス
#class Location(BaseModel):
    #location_id: int
    #location_name: str

# 基本的には辞書型で入ってくるが、sqlalchemyのorm型で入ってきても対応できる
    #class Config:
        #orm_mode = True