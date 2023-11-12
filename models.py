import uuid
from pydantic import BaseModel


class Note(BaseModel):
    id: uuid.UUID | None = None
    title: str
    content: str
