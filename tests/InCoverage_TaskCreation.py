import pytest
from datetime import datetime

@pytest.mark.parametrize("task_name, assignee, description, start_date, deadline", [
    ("Task", "John", "This is a testing description", "2023-11-14", "2023-11-15"),  # Test Case 1
    ("Task", "", "", "2023-11-14", ""),  # Test Case 2
    ("", "John", "This is a testing description", "2023-11-14", "2023-11-15"),  # Test Case 3
    ("Task", "John", "This is a testing description", "", "2023-11-15"),  # Test Case 4
    ("Task", "John", "This is a testing description", "2023-11-14", "2023-11-13"),  # Test Case 5
    ("Task", "", "", "2023-11-14", "2023-11-14"),  # Test Case 6
    ("ThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacess", "", "", "2023-11-14", "2023-11-14"),  # Test Case 7
    ("Task", "ThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacesThisIsALongStringWithNoSpacess", "", "2023-11-14", "2023-11-14"),  # Test Case 8
])

def test_taskCreation(task_name, assignee, description, start_date, deadline):
    result = create_task(task_name, assignee, description, start_date, deadline)
    print(result)  # Print the result or use it in your assertions


def create_task(task_name, assignee, description, start_date, deadline):
    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if deadline:
        deadline = datetime.strptime(deadline, "%Y-%m-%d")

    if not task_name:
        return ' Task name is required'
    elif not start_date:
        return ' Start Date is required'
    elif len(task_name) > 120:
        return ' Task name must be less than 120 characters'
    elif len(task_name) > 120:
        return ' Task name must be less than 120 characters'
    elif len(assignee) > 120:
        return ' Assignee name must be less than 120 characters'
    elif len(description) > 9999:
        return ' Description must be less than 9999 characters'
    elif deadline and deadline < start_date:
        return ' Deadline must be after Start Date'
    else:
        return ' Task was created successfully!'
