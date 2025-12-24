from user import User

def test_valid_email():
    user1 = User("email@wp.pl")
    user2 = User("emailwp.pl")
    user3 = User("email@@wp.pl")
    user4 = User("email@wp.pl ")
    user5 = User("email@")

    assert user1.is_valid() == True

    assert user2.is_valid() == False

    assert user3.is_valid() == False

    assert user4.is_valid() == False

    assert user5.is_valid() == False