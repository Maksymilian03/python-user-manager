from user_manager import UserManager

def print_menu():
    print("Witaj w User Manager! \n 1. Utwórz usera \n 2. Wyświetl userów \n 3. Zapisz \n"
          " 4. Zakoncz i zapisz \n 5. Zakoncz\n")

path = "plik.json"
flag = True
manager = UserManager(path)
while flag:
    print_menu()
    choice = input().strip()
    if choice == "1":
        email = input("Podaj email dla nowego usera: ")
        if manager.add_user(email):
            print("Dodano pomyślnie")
        else:
            print("BŁĄD w trakcie dodawania, email niepoprawny lub już istnieje")

    elif choice == "2":
        for user in manager.list_users():
            print(user)

    elif choice == "3":
        manager.save()
    elif choice == "4":
        manager.save()
        flag = False
    elif choice == "5":
        print("Czy zapisać przed wyjściem? \n 1. Tak \n 2. Nie")
        if input() == "1":
            manager.save()
        else :
            flag = False

        flag = False
    else:
        print("Wybierz poprawną opcję")


