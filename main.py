from user_manager import UserManager


def print_menu():
    print("Witaj w User Manager! \n 1. Utwórz usera \n 2. Wyświetl userów \n 3. Zapisz \n"
          " 4. Zakoncz i zapisz \n 5. Zakoncz\n")

path = "plik.json"
manager = UserManager(path)
flag = True

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


from storage import load_users
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# app = FastAPI()
#
# class UserCreateRequest(BaseModel):
#     email: str
#
# @app.get("/health")
# def health():
#     return {"status": "ok"}
#
#
# @app.post("/users")
# def create_user(data: UserCreateRequest, status_code=201):
#     if not manager.add_user(data.email):
#         raise HTTPException(status_code=400, detail='Invalid or duplicate email')
#
#     return {"message": "User created"}


