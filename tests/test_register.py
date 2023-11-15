def test_register_1(client, app):
    # Successful registration
    response = client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    with app.app_context():
        assert b'Success! Your account has been created' in response.data

def test_register_2(client, app):
    # Email already in database
    client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/register", 
                data={"email": "abc@def.com", "name":"Joe", "password1": "654321","password2": "654321"},
                follow_redirects=True)
    with app.app_context():
        assert b'Email already in database' in response.data

    
        