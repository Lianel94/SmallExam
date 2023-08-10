# Напишите проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.
import datetime as DT

def show_menu():
    print("\nChoose the action:\n"
        "1. Create a note and save as a txt. format:\n"
        "2. Show all the notes:\n"
        "3. Find the note by its date:\n"
        "4. Edit the note:\n"
        "5. Delete the note:\n"
        "6. Finish the work:\n")
    choice = int(input())
    return choice

def read_csv(filename: str) -> list:
    data = []
    fields = ["Heading", "Content", "Date"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def work_with_notes():
    choice = show_menu()
    allNotes = read_csv('notes.txt')

    while(choice != 6):
        if choice == 1:
            create_new_note(allNotes)
            save_note('notes.txt', allNotes)
        elif choice == 2:
            show_all_notes(allNotes)
        elif choice == 3:
            date = get_search_date()
            print("The results: ")
            show_all_notes(find_by_date(allNotes, date))
        elif choice == 4:
            edit_note(allNotes)
            rewrite_note('notes.txt', allNotes)
        elif choice == 5:
            delete_note(allNotes)
            rewrite_note('notes.txt', allNotes)
        choice = show_menu()

def create_new_note(allNotes:list):
    record = dict({"Heading" : input("Type your heading: "), "Content" : input("Type your message: "), "Date" : input("Type the date in the format dd/mm/yyyy: ")})
    allNotes.append(record)

def save_note(filename, allNotes:list):
    with open(filename, 'a', encoding='utf-8') as data:
        line = ''
        for v in allNotes[-1].values():
            line += v + ', '
        data.write(f"{line[:-1]}\n")
        

def show_all_notes(allNotes:list):
    for elem in allNotes:
        for key in elem:
            print(f'{key} : {elem[key]}')
        print()
    

def find_by_date(allNotes: list, date: str):
    results = []
    for elem in allNotes:
        if elem["Date"] == date:
            results.append(elem)
    return results

def get_search_date():
    return input("Type the date in the format dd/mm/yyyy: ")

def edit_note(allNotes:list):
    searching_date = input("Type the date in the format dd/mm/yyyy of the note you want to change: ")
    field = input("Type the field you want to change (Heading or Content): ")
    new_filed_value = input("Type new heading or content: ")
    for elem in allNotes:
        for v in elem.values():
            if v == searching_date:
                elem[field] = elem[field].replace(
                    elem[field], new_filed_value)

def rewrite_note(filename, allNotes:list):
    with open(filename, 'w', encoding='utf-8') as data:
        for i in range(len(allNotes)):
            line = ''
            for v in allNotes[i].values():
                line += v + ', '
            data.write(f"{line[:-1]}\n")

def delete_note(allNotes:list):
    deleted_heading = input("Type the heading you want to delete: ")
    for elem in allNotes:
        for v in elem.values():
            if v == deleted_heading:
                allNotes.remove(elem)

work_with_notes()