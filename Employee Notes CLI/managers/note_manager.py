from datetime import datetime

class Note:
    def __init__ (self, employee_name, content):
        self.employee_name = employee_name
        self.content = content
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict (self):
        return {
            "employee_name": self.employee_name, 
            "content": self.content,
            "created_at": self.created_at
        }
        
    def __str__(self):
        return f"[{self.created_at}] {self.employee_name}: {self.content}"
    

class NoteManager:
    def __init__ (self):
        self.notes = []

    def add_note(self, employee_name, content):
        note = Note(employee_name, content)
        self.notes.append(note)
        print(f"Note added for {employee_name}.")

    def get_all_notes(self):
        return self.notes
    
    def search_by_employee(self, name):
        return [n for n in self.notes if n.employee_name.lower() == name.lower()]
    
    def count(self):
        return len(self.notes)

manager = NoteManager()
manager.add_note("Ali", "Completed Q3 report")
manager.add_note("Sara", "Missed standup meeting")
manager.add_note("Ali", "Promoted to senior analyst")

print(f"Total notes: {manager.count()}")

for note in manager.search_by_employee("Ali"):
    print(note)

