
# T1 and T2 still need to be tested


def test_register_2(client, app):
    # Email already in database
    # T3
    client.post("/register", 
                data={"email": "abc@def.com", "name":"Joe", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    with app.app_context():
        assert b'Email already in database' in response.data

def test_register_3(client, app):
    # '@' not in email
    # T4
    response = client.post("/register", 
                data={"email": "abcdef", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    with app.app_context():
        assert b'Invalid email address' in response.data
        
def test_register_4(client, app):
    # less than 3 char in email
    # T5 fail
    response = client.post("/register", 
                data={"email": "a@b", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    with app.app_context():
        assert b'Email must contain more than three characters' in response.data

def test_register_5(client, app):
    # name cannot be less than 3 char
    # T6 fail
    response = client.post("/register", 
                data={"email": "abc@def.com", "name":"xy", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    with app.app_context():
        assert b'Name must contain more than two characters' in response.data     

def test_register_6(client, app):
    # password1 != password2
    # T7
    response = client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "triangle"},
                follow_redirects=True)
                
    with app.app_context():
        assert b'Passwords do not match' in response.data  
        
def test_register_7(client, app):
    # password must contain more than 6 chars
    # T8
    response = client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "12345","password2": "12345"},
                follow_redirects=True)
    with app.app_context():
        assert b'Password must contain more than six characters' in response.data  
        
def test_register_8(client, app):
    # Successful registration
    # T9
    response = client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    with app.app_context():
        assert b'Success! Your account has been created' in response.data
        
