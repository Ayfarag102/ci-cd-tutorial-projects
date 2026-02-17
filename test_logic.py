#This is a simptle test script
def test_math():
    assert 2 + 2 == 4 #This should pass

def test_string():
    greeting = "Hello to CI/CD"
    assert "CI/CD" in greeting #This should pass

print("Tests passed successfully!")
