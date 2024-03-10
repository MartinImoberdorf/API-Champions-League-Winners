from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from bd.database import session
from models.winners import Winner as ModelWinner
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

routerWinner=APIRouter()


class Winner(BaseModel):
    season:str=Field()
    year:int=Field()
    winner:str=Field()
    score:str=Field()
    runners_up:str=Field()
    stadium:str=Field()
    attendance:float=Field()

    def to_dic(self):
        return{
            "Season":self.season,
            "Year":self.year,
            "Winner":self.winner,
            "Score":self.score,
            "Runners-up":self.runners_up,
            "Stadium":self.stadium,
            "Attendance":self.attendance,
        }



@routerWinner.get("/winners",tags=["Winners"], status_code=200)
def get_winners():
    db=session()
    data=db.query(ModelWinner).all()
    if not data:
        return JSONResponse(status_code=404, content={"message":"Winner not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(data))

@routerWinner.get("/winner/{year}",tags=["Winners"], status_code=200)
def get_winner_by_year(year:int):
    db=session()
    data=db.query(ModelWinner).filter(ModelWinner.year==year).first()
    if not data:
        return JSONResponse(status_code=404, content={"message":"Winner not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(data))


@routerWinner.get("/winner/",tags=["Winners"], status_code=200)
def get_winner_by_winner(winner:str):
    db=session()
    data=db.query(ModelWinner).filter(ModelWinner.winner == winner).all()
    if not data:
        return JSONResponse(status_code=404, content={"message":"Winner not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(data))


@routerWinner.get("/winner_season/",tags=["Winners"], status_code=200)
def get_winner_by_season(season: str):
    db=session()
    data=db.query(ModelWinner).filter(ModelWinner.season==season).first()
    if not data:
        return JSONResponse(status_code=404, content={"message":"Winner not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(data))

@routerWinner.get("/winner_score/",tags=["Winners"], status_code=200)
def get_winner_by_score(score: str):
    db=session()
    data=db.query(ModelWinner).filter(ModelWinner.score==score).all()
    if not data:
        return JSONResponse(status_code=404, content={"message":"Winner not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(data))
