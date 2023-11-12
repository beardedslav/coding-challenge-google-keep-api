from models import Note
import storage
import uuid


def create_note(note: Note) -> Note:
    if note.title == "":
        raise ValueError("Title parameter can't be empty")
    note.id = uuid.uuid4()
    storage.save_note(note)
    return note
