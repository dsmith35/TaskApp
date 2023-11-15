def test_logout_1(client, app):
    # Successful registration
    client.post("/register", 
                data={"email": "test@test.com", "name":"test", "password1": "testpassword","password2": "testpassword"},
                follow_redirects=True)
    response = client.get("/logout",
                follow_redirects=True)
    with app.app_context():
        assert response.status_code == 200