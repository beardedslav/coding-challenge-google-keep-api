import json
from uuid import UUID

from tinydb import TinyDB

from notes import Note


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


db = TinyDB("db.json", cls=UUIDEncoder)


def save_note(note: Note) -> None:
    notes_table = db.table("notes")
    notes_table.insert(note.dict())
