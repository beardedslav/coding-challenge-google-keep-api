def create_note(title: str, content: str):
    if title == "":
        raise ValueError("Title parameter can't be empty")
