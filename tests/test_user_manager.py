import pytest
from user_manager import UserManager


@pytest.fixture
def empty_manager():
    return UserManager("test.json")

def test_add_correct_user(empty_manager):

    assert empty_manager.add_user("correct_test@wp.pl") == True

def test_add_uncorrect_user(empty_manager):
    empty_manager.add_user("uncorrect_test@wp.pl")

    assert empty_manager.add_user("uncorrect_test@wp.pl") == False  #User juz istnieje

def test_remove_correct_user(empty_manager):
    empty_manager.add_user("remove@wp.pl")

    assert empty_manager.remove_user("remove@wp.pl") == True

def test_remove_uncorrect_user(empty_manager):

    assert empty_manager.remove_user("nieistnieje@wp.pl") == False   #Nie ma takiego usera

def test_list_correct_users(empty_manager):
    empty_manager.add_user("test@wp.pl")

    assert empty_manager.list_users() == ['test@wp.pl']