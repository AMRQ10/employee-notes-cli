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

## Tech Stack
- Python 3.x
- JSON for data persistence
