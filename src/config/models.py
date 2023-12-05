from pydantic import BaseModel


class Key(BaseModel):
    name: str
    value: str
    description: str
    icon: str

    def __hash__(self) -> int:
        return self.name.__hash__()
