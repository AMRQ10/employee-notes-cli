# Employee Notes CLI

A command-line application for managing employee notes, built with Python.
Demonstrates OOP architecture, JSON persistence, and error handling.

## Features
- Add, view, search, and clear employee notes
- Persistent storage via JSON
- Input validation and graceful error handling
- Modular OOP structure with separated concerns

## Project Structure
employee-notes-cli/
├── models/
│   └── note.py
├── managers/
│   └── note_manager.py
├── utils.py
├── main.py
└── notes.json

## Setup
```bash
git clone https://github.com/yourname/employee-notes-cli
cd employee-notes-cli
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
python main.py
```

## Progress Log
- **Day 1 — Apr 25:** Modular CLI structure with JSON persistence
- **Day 2 — Apr 26:** Refactored into OOP with Note and NoteManager classes
- **Day 3 — Apr 27:** Error handling, input validation, custom exceptions

## Tech Stack
- Python 3.x
- JSON for data persistence

## What I Learned
- Modular Python project structure with separated concerns
- OOP design with classes, inheritance, and dunder methods
- JSON file persistence and data serialization
- Error handling and input validation patterns
- Git workflow and professional commit messages
