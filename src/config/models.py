from pydantic import BaseModel


class Key(BaseModel):
    name: str
    value: str
    description: str
    icon: str
