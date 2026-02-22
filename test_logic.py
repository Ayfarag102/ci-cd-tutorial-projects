# This is a simple test script
def test_math():
    assert 2 + 2 == 4  # This should pass


def test_string():
    greeting = "Hello to CI/CD"
    assert "CI/CD" in greeting  # This should pass


def test_list():
    fruits = ["apple", "banana", "cherry"]
    assert "banana" in fruits
    assert len(fruits) == 3


print("Tests passed successfully!")
