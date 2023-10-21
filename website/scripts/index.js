function register(user,pass) {
    //send data to backend
}

function login(user, pass) {
    //check if user is exists in backend
    //if they are:
    let user = new User("username", "userID", "groups", "isauthenticated");
    localStorage.setItem("userinfo", user)
}

function createTask(name, groupID, desc, deadline, subtasks, priority, usersResponsible, isCompleted, parentTask, subTasks) {
    //send data to backend
}

function createGroup(groupName) {
    //send data to backend
}

function inviteUser(username, groupID) {
    //Sends request to backend to add user to invited users list for the group
}

function joinGroup(groupID) {
    userinfo = localStorage.getItem("userinfo")
    //check backend if userinfo.userID is invited to groupID, if so then add them as a member
}

function editTask(taskName, groupID, desc, deadline, subtasks, priority, usersResponsible, isCompleted, parentTask, subTasks) {
    //send data to backend
}

function retrieveGroupData(groupID, userID) {
    //fetch info from backend
}