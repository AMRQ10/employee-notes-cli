from managers.note_manager import NoteManager
from utils1 import print_header, get_non_empty_input
from colorama import Fore, Style, init
from tabulate import tabulate

from dotenv import load_dotenv
import os

load_dotenv()
APP_NAME = os.getenv("APP_NAME", "Employee Notes System")
MAX_NOTES = int(os.getenv("MAX_NOTES", 100))


def show_menu():
    print_header(APP_NAME)
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search by Employee")
    print("4. Count Notes")
    print("5. Clear All Notes")
    print("6. Exit")

def handle_choice(choice, manager):
    if choice == "1":
        name = get_non_empty_input("Enter employee name: ")
        content = get_non_empty_input("Enter note content:")
        manager.add_note(name, content, max_notes=MAX_NOTES)

    elif choice == "2":
        notes = manager.get_all_notes()
        if not notes:
            print(Fore.YELLOW + "No notes found.")
        else:
            table_data = [
                [note.employee_name, note.content, note.created_at]
                for note in notes
            ]
            headers = ["Employee", "Note", "Date"]
            print(Fore.CYAN + tabulate(table_data, headers=headers, tablefmt="grid"))

    elif choice == "3":
        name = get_non_empty_input("Enter employee name to search: ")
        results = manager.search_by_employee(name)
        if not results:
            print(Fore.YELLOW + f"No notes found for {name}.")
        else:
            table_data = [
                [note.employee_name, note.content, note.created_at]
                for note in results
            ]
            headers = ["Employee", "Note", "Date"]
            print(Fore.CYAN + tabulate(table_data, headers=headers, tablefmt="grid"))

    elif choice == "4":
        print(Fore.CYAN + f"Total notes: {manager.count()}")

    elif choice == "5":
        confirm = input("Are you sure? (yes/no): ").strip().lower()
        if confirm == "yes":
            manager.clear_all()
            print(Fore.GREEN + "All notes cleared.")
        else:
            print(Fore.YELLOW + "Clear cancelled.")

    elif choice == "6":
        raise KeyboardInterrupt

    else:
        print(Fore.RED + "Invalid choice. Please enter a number between 1 and 6.")

def main():
    manager = NoteManager()
    while True:
        try:
            show_menu()
            choice = input("\nEnter choice: ").strip()
            handle_choice(choice, manager)
        except KeyboardInterrupt:
            print("\nExiting. Goodbye.")
            break
        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}")
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


