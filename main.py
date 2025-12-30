from user_manager import UserManager
#
#
# def print_menu():
#     print("Witaj w User Manager! \n 1. Utwórz usera \n 2. Wyświetl userów \n 3. Zapisz \n"
#           " 4. Zakoncz i zapisz \n 5. Zakoncz\n")
#


# flag = True
#
# while flag:
#     print_menu()
#     choice = input().strip()
#     if choice == "1":
#         email = input("Podaj email dla nowego usera: ")
#         if manager.add_user(email):
#             print("Dodano pomyślnie")
#         else:
#             print("BŁĄD w trakcie dodawania, email niepoprawny lub już istnieje")
#
#     elif choice == "2":
#         for user in manager.list_users():
#             print(user)
#
#     elif choice == "3":
#         manager.save()
#     elif choice == "4":
#         manager.save()
#         flag = False
#     elif choice == "5":
#         print("Czy zapisać przed wyjściem? \n 1. Tak \n 2. Nie")
#         if input() == "1":
#             manager.save()
#         else :
#             flag = False
#
#         flag = False
#     else:
#         print("Wybierz poprawną opcję")


from storage import load_users
from fastapi import FastAPI, HTTPException
from schemas import UserCreate


path = "plik.json"
manager = UserManager(path)
empty_api_manager = UserManager("pustyplik.json")
app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/users", status_code=201)
def create_user(data: UserCreate):
    if not manager.add_user(data.email):
        raise HTTPException(status_code=400, detail='Invalid or duplicate email')

    return {"message": "User created"}


@app.delete("/users/{email}")
def delete_user(email: str):
    result = manager.remove_user(email)

    if result:
        return {"message": "User deleted"}

    raise HTTPException(
        status_code = 404,
        detail = "User not found"
    )

@app.get("/users")
def get_users():
    return manager.list_users()

@app.get("/users/{email}")
def get_user(email: str):
    user = manager.get_user(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"email": email}


