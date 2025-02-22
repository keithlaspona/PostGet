from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd


app = FastAPI()

user_data_list = []

class UserCreate(BaseModel):
    user_id: int
    username: str

@app.post("/create_user/")
async def create_user(user_data: UserCreate):
    user_id = user_data.user_id
    username = user_data.username
    
    user_data_list.append({"user_id": user_id, "username": username})
    df = pd.DataFrame(user_data_list)
    df.to_csv("user_data.csv", index=False)
    
    
    return {
        "msg": "we got data successfully",
        "user_id": user_id,
        "username": username,
    }
    
    
@app.get("/get_users/")
async def get_users():
    return user_data_list


@app.get("/export_users/")
async def export_users():
    df = pd.DataFrame(user_data_list)
    
    df.to_csv("user_data.csv", index=False)
    
    return {
        "msg": "Users exported to CSV successfully"
    }
