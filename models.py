import enum
from typing import Optional, List
from uuid import UUID, uuid4

from pydantic import BaseModel
class Gender(str, enum.Enum):
    male="male"
    female="female"
class Role(str, enum.Enum):
    User="User"
    admin="admin"
    student="student"


class User(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:str
    last_name:str
    middle_name:Optional[str]
    gender:Gender
    roles:List[Role]
class UserUpdateRequest(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:Optional [str]
    last_name:Optional[str]
    middle_name:Optional[str]
    gender:Optional[Gender]
    roles:Optional[List[Role]]
