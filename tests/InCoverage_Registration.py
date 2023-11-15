import pytest

@pytest.mark.parametrize("name, email, password, confirm_password", [
    ("JJ", "JJ1@gmail.com", "123456", "123456"),        # Test Case 1
    ("J", "JJ1@gmail.com", "123456", "123456"),          # Test Case 2
    ("Test3", "JJ1gmail.com", "123456", "123456"),       # Test Case 3
    ("Test4", "JJ1@gmail.com", "123456", "123456"),      # Test Case 4
    ("Test5", "Test5@gmail.com", "12345", "12345"),      # Test Case 5
    ("Test6", "Test6@gmail.com", "123456", "654321"),     # Test Case 6
    ("Test7", "123456789123456789123456789123456789123456789123456@gmail.com", "123456", "123456"),     # Test Case 7
    ("123456789123456789123456789123456789123456789123456", "Test8@gmail.com", "123456", "123456"),     # Test Case 8
    ("Test9", "Test9@gmail.com", "123456789123456789123456789123456789123456789123456", "123456789123456789123456789123456789123456789123456")     # Test Case 9
])

def test_register(name, email, password, confirm_password):
    result = register(name, email, password, confirm_password)
    print(result)  # Print the result or use it in your assertions

def register(name, email, password, confirm_password):

    if '@' not in email:
        return 'Invalid email address'
    elif len(name) < 2:
        return 'Name must contain more than two characters'
    elif password != confirm_password:
        return 'Passwords do not match'
    elif len(password) < 6:
        return 'Password must contain more than six characters'
    elif len(email) > 50:
        return 'Email must contain less than 50 characters'
    elif len(name) > 50:
        return 'Name must contain less than 50 characters'
    elif len(password) > 50:
        return 'Password must contain less than 50 characters'
    else:
        return 'Success! Your account has been created'


test_data = [
    ("JJ", "JJ1@gmail.com", "123456", "123456", "Success! Your account has been created"),  # Test Case 1 (Should Succeed)
    ("JJ", "JJ1@gmail.com", "123456", "123456", "Name must contain more than two characters"),  # Test Case 2
    ("Test3", "JJ1gmail.com", "123456", "123456", "Email must contain @"),  # Test Case 3
    ("Test4", "JJ1@gmail.com", "123456", "123456", "Email must not be the same as another"),  # Test Case 4
    ("Test5", "Test5@gmail.com", "12345", "12345", "Password must contain more than six characters"),  # Test Case 5
    ("Test6", "Test6@gmail.com", "123456", "654321", "Passwords do not match"),  # Test Case 6
    ("Test7", "123456789123456789123456789123456789123456789123456@gmail.com", "123456", "123456", "Email must contain less than 50 characters"),  # Test Case 7
    ("123456789123456789123456789123456789123456789123456", "Test8@gmail.com", "123456", "123456", "Name must contain less than 50 characters"),  # Test Case 8
    ("Test9", "Test9@gmail.com", "123456789123456789123456789123456789123456789123456", "123456789123456789123456789123456789123456789123456", "Passwords must contain less than 50 characters")  # Test Case 9
]