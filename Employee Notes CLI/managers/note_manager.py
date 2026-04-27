import json
import os
from models.notes import Note

NOTES_FILE = "notes.json"

class NoteManager:
    def __init__(self):
        self.notes = []
        self.load_from_file()

    def add_note(self, employee_name, content):
        note = Note(employee_name, content)
        self.notes.append(note)
        self.save_to_file()
        print(f"Note added for {employee_name}.")

    def get_all_notes(self):
        return self.notes
    
    def search_by_employee(self, name):
        return [n for n in self.notes if n.employee_name.lower() == name.lower()]
    
    def count(self):
        return len(self.notes)
    
    def clear_all(self):
        self.notes = []
        self.save_to_file()

    def save_to_file(self):
        try:
            with open(NOTES_FILE, "w") as f:
                data = [note.to_dict() for note in self.notes]
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving notes: {e}")

    def load_from_file(self):
        try:
            with open(NOTES_FILE, "r") as f:
                data = json.load(f)
                self.notes = [
                    Note(d["employee_name"], d["content"], d["created_at"])
                    for d in data
                ]
        except FileNotFoundError:
            self.notes = []
        except json.JSONDecodeError:
            print("Warning: notes file corrupted. Starting fresh.")
            self.notes = []





