import pytest

from notes import create_note


def test_note_creation_fails_with_empty_title():
    with pytest.raises(ValueError):
        create_note(title="", content="Test content")


def test_note_creation():
    new_note = create_note("Title", "Content")
    assert new_note.title == "Title"
    assert new_note.content == "Content"
    assert new_note.id != 0
