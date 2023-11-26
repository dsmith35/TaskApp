def test_project_2(client, app):
    # No project name provided
    # Covers T1
    client.post("/register",
                data={"email": "abc@def.com", "name": "John", "password1": "123456", "password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject",
                           data={"description": "", "sdate": "", "use-deadline": "False"},
                           follow_redirects=True)
    with app.app_context():
        assert b"Project name is required" in response.data

def test_project_3(client, app):
    # GET request, no input data, shouldn't cause issues
    # Covers T2
    client.get("/register",
                data={"email": "abc@def.com", "name": "John", "password1": "123456", "password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject",
                           data={},
                           follow_redirects=True)
    with app.app_context():
        assert response.status_code == 200

def test_project_4(client, app):
    # No start date
    # Covers T3
    client.post("/register",
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject",
                data={"name": "FakeName123", "use-deadline": "False"},
                follow_redirects=True)
    with app.app_context():
        assert b"Start date is required" in response.data

def test_project_5(client, app):
    # Deadline not given (only if use-deadline box is checked)
    # Covers T4
    client.post("/register",
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject",
                data={"name": "FakeName123", "sdate": "2023-11-25","use-deadline": "True"},
                follow_redirects=True)
    with app.app_context():
        assert b"No deadline given" in response.data


def test_project_1(client, app):
    # Successfully created new project
    # Covers T5
    client.post("/register",
                data={"email": "abc@def.com", "name":"John", "password1": "123456", "password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject",
                data={"name": "FakeName123", "sdate": "2023-11-25", "use-deadline": "True", "deadline": "2023-11-27"},
                follow_redirects=True)
    with app.app_context():
        assert b"New Project [FakeName123] created successfully" in response.data


def test_project_6(client, app):
    # Start date after deadline error
    # Covers T6
    client.post("/register",
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject",
                data={"name": "FakeName123", "sdate": "2023-11-27", "use-deadline": "True", "deadline": "2023-11-25"},
                follow_redirects=True)
    with app.app_context():
        assert b"Start date must be before the deadline" in response.data

