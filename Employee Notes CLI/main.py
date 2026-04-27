from managers.note_manager import NoteManager
from utils1 import print_header, get_non_empty_input

def show_menu():
    print_header("Employee Notes System")
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
        manager.add_note(name, content)

    elif choice == "2":
        notes = manager.get_all_notes()
        if not notes:
            print("No notes found.")
        else:
            for note in notes:
                print(note)

    elif choice == "3":
        name = get_non_empty_input("Enter employee name to search: ")
        results = manager.search_by_employee(name)
        if not results:
            print(f"No notes found for {name}.")
        else:
            for note in results:
                print(note)

    elif choice == "4":
        print(f"Total notes: {manager.count()}")

    elif choice == "5":
        confirm = input("Are you sure? (yes/no): ").strip().lower()
        if confirm == "yes":
            manager.clear_all()
            print("All notes cleared.")

    elif choice == "6":
        raise KeyboardInterrupt

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

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
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


