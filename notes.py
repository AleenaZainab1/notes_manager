# notes.py
import json

# Load existing notes
try:
    with open("notes.json") as f:
        notes = json.load(f)
except FileNotFoundError:
    notes = []

def add_note():
    note = input("Enter your note: ")
    notes.append(note)
    save_notes()
    print("Note added!")

def view_notes():
    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

def search_notes():
    term = input("Search for: ").lower()
    found = [n for n in notes if term in n.lower()]
    print(f"\nFound {len(found)} notes:")
    for i, note in enumerate(found, 1):
        print(f"{i}. {note}")

def delete_note():
    view_notes()
    try:
        num = int(input("Enter note number to delete: ")) - 1
        if 0 <= num < len(notes):
            deleted = notes.pop(num)
            save_notes()
            print(f"Deleted: {deleted}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

while True:
    print("\nNotes Manager")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Exit")
    
    choice = input("Choose option (1-5): ")
    
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        search_notes()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break