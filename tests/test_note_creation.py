import pytest
from models import Note
from notes import create_note


def test_note_creation_fails_with_empty_title():
    with pytest.raises(ValueError):
        create_note(Note(title="", content="Test content"))


def test_note_creation():
    new_note = create_note(Note(title="Title", content="Content"))
    assert new_note.title == "Title"
    assert new_note.content == "Content"
    assert new_note.id != 0
