import json
from datetime import datetime

notes_file = 'notes.json'

def load_notes():
    try:
        with open(notes_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def save_notes(notes):
    with open(notes_file, 'w') as file:
        json.dump(notes, file, indent=4)

def generate_id(notes):
    return len(notes) + 1 if notes else 1

def add_note():
    notes = load_notes() if load_notes() else []
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note = {
        'id': generate_id(notes),
        'title': title,
        'body': body,
        'created': str(datetime.now()),
        'modified': str(datetime.now())
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes():
    notes = load_notes()
    if notes is None:
        print("Файл с заметками не найден.")
        return
    for note in notes:
        print(f"{note['id']}: {note['title']}: {note['body']} (Создано: {note['created']}, Обновлено: {note['modified']})")

def edit_note():
    notes = load_notes()
    if notes is None:
        print("Файл с заметками не найден.")
        return
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новое тело заметки: ")
            note['modified'] = str(datetime.now())
            save_notes(notes)
            print("Заметка успешно обновлена")
            return
    print("Заметка с таким ID не найдена")

def delete_note():
    notes = load_notes()
    if notes is None:
        print("Файл с заметками не найден.")
        return
    note_id = int(input("Введите ID заметки для удаления: "))
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена")

while True:
    command = input("Введите команду (add, list, edit, delete, exit): ")
    if command == 'add':
        add_note()
    elif command == 'list':
        list_notes()
    elif command == 'edit':
        edit_note()
    elif command == 'delete':
        delete_note()
    elif command == 'exit':
        break
