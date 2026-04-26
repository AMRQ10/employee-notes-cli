def print_header(title):
    print("=" * 30)
    print(title)
    print("=" * 30)

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty")