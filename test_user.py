from User import User
import pytest


@pytest.fixture
def user():
    """Returns a basic user with all values"""
    return User("Megan", 38, "thequiltingriverotter@gmail.com", "123-456-7890")


@pytest.fixture
def user_without():
    """Returns a user without email or phone number"""
    return User("Bob", 50)


def test_user_values(user):
    assert user.name == "Megan"
    assert user.age == 38
    assert user.email == "thequiltingriverotter@gmail.com"
    assert user.phone_number == "123-456-7890"


def test_user_without_values(user_without):
    assert user_without.name == "Bob"
    assert user_without.age == 50
    assert user_without.email is None
    assert user_without.phone_number is None


def test_reset_values(user):
    user.age = 39
    user.email = "fakeemail@gmail.com"
    assert user.age == 39
    assert user.email == "fakeemail@gmail.com"


def test_reset_values_raise_type_error(user):
    with pytest.raises(TypeError):
        user.age = "39"


def test_reset_values_raise_value_error(user):
    with pytest.raises(ValueError):
        user.email = "fakeemail"


# test other value/type errors,
