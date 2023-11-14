from website.models import User

def test_register_1(client, app):
    # Successful registration
    response = client.post("/register", 
                data={"email": "test@test.com", "name":"test", "password1": "testpassword","password2": "testpassword"},
                follow_redirects=True)
    with app.app_context():
        assert b'Success! Your account has been created' in response.data

def test_register_2(client, app):
    # Email already in database
    client.post("/register", 
                data={"email": "test@test.com", "name":"test", "password1": "testpassword","password2": "testpassword"},
                follow_redirects=True)
    response = client.post("/register", 
                data={"email": "test@test.com", "name":"test", "password1": "testpassword","password2": "testpassword"},
                follow_redirects=True)
    with app.app_context():
        assert b'Email already in database' in response.data

    
        