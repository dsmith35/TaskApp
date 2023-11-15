def test_login_1(client, app):
    # Successful login
    client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/login", 
                data={"email": "abc@def.com", "password": "123456"},
                follow_redirects=True)
    with app.app_context():
        assert b'Login Successful!' in response.data

def test_login_2(client, app):
    # Email not found
    response = client.post("/login", 
                data={"email": "xyz@qrt.com", "password": "123456"},
                follow_redirects=True)
    with app.app_context():
        assert b'Email not found' in response.data

def test_login_3(client, app):
    # Login failed (wrong password)
    client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/login", 
                data={"email": "abc@def.com", "password": "wrongpassword"},
                follow_redirects=True)
    with app.app_context():
        assert b'Login Failed!' in response.data


    
        