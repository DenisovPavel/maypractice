import os.path
import colorama
from colorama import Fore, Style
import functions as Functions




def main():
    colorama.init
    os.system("cls")
    if os.path.exists('data.json'):
        file_name = 'data.json'
        notes = Functions.read_notes_file(file_name)
    else:
        Functions.get_file()
        file_name = 'data.json'
        notes = Functions.read_notes_file(file_name)
    

    while True:
        print(Fore.GREEN+'Choose action:')
        print('1. Show ALL Notes')
        print('2. Show notes according date')
        print('3. Show specific note')
        print('4. Add new note')
        print('5. Change note')
        print('6. Remove note')
        print('7. Exit')

        choice = input(Fore.YELLOW +'Your choice: ')

        if choice == '1':
            Functions.print_notes(notes) #все заметки
        elif choice == '2':
            date_str = input('Put date year-month-date(example "2023-05-27 10:13:30"): ') # установка даты
            filtered_notes = Functions.filter_notes_by_date(notes, date_str)
            Functions.print_notes(filtered_notes)
        elif choice == '3':
            id = int(input('Put Note ID: ')) # id
            flag = False
            for note in notes:
                if note['id'] == id:
                    Functions.print_note(note)
                    flag = True
                    break
            if flag == False: print(Fore.RED + 'Note not found' + Style.RESET_ALL)
        elif choice == '4':
            notes = Functions.add_note(notes)
            Functions.save_notes_json(notes, file_name)
            print(Fore.RED + 'Note added' + Style.RESET_ALL) # добавление
        elif choice == '5':
            id = int(input('Put Note ID to change note: ')) # изменение
            notes = Functions.edit_note(notes, id)
            Functions.save_notes_json(notes, file_name)
        elif choice == '6':
            id = int(input('put NOTE ID to remove note: ')) # удаление
            notes = Functions.delete_note(notes, id)
            Functions.save_notes_json(notes, file_name)
        elif choice == '7':
            print(Style.RESET_ALL) # выход
            os.system("EXIT")
            break
        else:
            print(Fore.BLUE + 'Uncorrect choise' + Style.RESET_ALL)

if __name__ == '__main__':
    main()