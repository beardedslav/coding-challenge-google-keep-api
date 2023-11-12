from fastapi import FastAPI
from models import Note
import notes

app = FastAPI()


@app.post("/notes")
async def create_note(note: Note):
    notes.create_note(note)
    return note
