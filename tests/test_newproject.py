def test_project_1(client, app):
    # Successfully created new project
    client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject", 
                data={"name":"TestProject", "description":"a test project", "sdate": "2023-11-01","use-deadline":"True","deadline": "2023-11-11"},
                follow_redirects=True)
    with app.app_context():
        assert b"New Project [TestProject] created successfully" in response.data

def test_project_2(client, app):
    # No start date
    client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject", 
                data={"name":"TestProject", "description":"a test project","use-deadline":"True","deadline": "2023-11-11"},
                follow_redirects=True)
    with app.app_context():
        assert b"Start date is required" in response.data

def test_project_3(client, app):
    # Start date after deadline error
    client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject", 
                data={"name":"TestProject", "description":"a test project","sdate": "2100-11-14","use-deadline":"True","deadline": "2001-11-14"},
                follow_redirects=True)
    with app.app_context():
        assert b"Start date must be before the deadline" in response.data

def test_project_4(client, app):
    # Deadline not given (only if use-deadline box is checked)
    client.post("/register", 
                data={"email": "abc@def.com", "name":"John", "password1": "123456","password2": "123456"},
                follow_redirects=True)
    response = client.post("/newproject", 
                data={"name":"TestProject", "description":"a test project","sdate": "2000-10-14","use-deadline":"True"},
                follow_redirects=True)
    with app.app_context():
        assert b"No deadline given" in response.data
