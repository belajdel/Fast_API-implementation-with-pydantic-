
from typing import List
from uuid import  UUID

from fastapi import FastAPI, HTTPException

from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()
db: List[User]=[
    User(id=UUID("59b62a85-e77a-4d9d-8329-20ad2a64b8b3"),first_name="amine",
         last_name="lajdel",
         middle_name=None,
         gender=Gender.male,
         roles=[Role.student]
         ),
    User(id=UUID("54ddbe7a-a16d-48e8-8204-134fd12fd35b"), first_name="homs",
         last_name="zbib",
         middle_name=None,
         gender=Gender.male,
         roles=[Role.admin]
         )
]
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/Users")
async  def fetch_users():
    return db

@app.post("/api/v1/Users")
async def register_user(user: User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/Users/{user_id}")
async  def delete_user(user_id:UUID):
    for user in(db):
        if user.id==user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
@app.put("/api/v1/Users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(status_code=404, detail=f"User with id{user_id} not found")
