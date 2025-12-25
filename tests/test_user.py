from user import User

def test_valid_correct_email():
    user1 = User("email@wp.pl")

    assert user1.is_valid() == True

def test_valid_uncorrect_lack_at_email():
    user2 = User("emailwp.pl")

    assert user2.is_valid() == False


def test_valid_uncorrect_double_at_email():
    user3 = User("email@@wp.pl")

    assert user3.is_valid() == False

def test_valid_uncorrect_space_in_email():
    user4 = User("email@wp.pl ")

    assert user4.is_valid() == False


def test_valid_uncorrect_no_domain_email():
    user5 = User("email@")

    assert user5.is_valid() == False
