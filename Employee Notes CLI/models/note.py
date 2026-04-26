import json
import os
from models.note import Note

NOTES_FILE = "notes.json"

class NoteManager:
    def __init__(self):
        self.notes = []
        self.load_from_file()

    def save_to_file(self):
        data = [note.to_dict() for note in self.notes]
        with open(NOTES_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as f:
                data = json.load(f)
                self.notes = [
                    Note(d["employee_name"], d["content"], d["created_at"])
                    for d in data
                ]

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)


