from fastapi import FastAPI
from typing import Optional
app = FastAPI()
users = {}
@app.get("/")
def home():
    return {"status": "knotrah CRM online"}
@app.get ("/scim/v2/Users")
def list_users():
    return {"users": list(users.values())}
from pydantic import BaseModel
class User (BaseModel):
    userName: str
    active: bool = True
@app.post ("/scim/v2/Users")
def create_user(user: User):
    users[user.userName] = {
        "userName": user.userName,
        "active": user.active
    }
    return {
        "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
        "id": user.userName,
        "userName": user.userName,
        "active": user.active
    }
class UserUpdate (BaseModel):
    userName: Optional[str] = None
    active: Optional[bool] = None
@app.get("/scim/v2/Users/{user_id}")
def get_user(user_id: str):
    for key, user in users.items():
        if key.lower() == user_id.lower():
            return {
                "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
                "id": key,
                "userName": user["userName"],
                "active": user["active"]
            }
    return {"detail": "User not found"}
@app.patch ("/scim/v2/Users/{user_id}")
def update_user (user_id: str, update: UserUpdate):
        if user_id not in users :
            return {"error": "User not found"}
        if update.userName is not None:
            users[user_id] ["userName"] = update.userName
            if update.active is not None:
                users[user_id] ["active"] =update.active
                return users[user_id]
@app.get("/scim/v2/Groups")
def get_groups():
    return {"Resources": []}
@app.post("/scim/v2/Groups")
def create_group(group: dict):
    return group
