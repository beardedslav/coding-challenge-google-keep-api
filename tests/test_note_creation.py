# Step 1
# In this step your goal is to create the API endpoint to be able to add a new note. For this challenge a note consists of:
#     Title
#     Note Content
# Make sure that your API allows a new note to be created and that the note is saved to some persistent storage. You could simple save the notes to disk or you could use some form of database.
# Consider carefully the trade-offs. Disk is fine for a personal application with a single user, even a few hundred users if done with care. If you wanted to be able to support the scale of Google Keep, some form of database will be required with thought given to how it scales.
# At this stage it would also be great to build some test automation and a set of tests that check both the happy path and error conditions.

from notes import create_note
import pytest


def test_note_creation_fails_with_empty_title():
    with pytest.raises(ValueError):
        create_note(title="", content="Test content")
