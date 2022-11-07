# Username Search & Update System

- Create a member API with Python Flask and Call the API with AJAX.
- Import `mysql.connector` module to connect MySQL database in Python.
- Connection pooling.

### ■ Technologies

- Frontend: Vanilla JavaScript
- Backend: Python Flask
- Database: MySQL

---

### ■ Username Search System

- 「找不到（Not Found）」will show up if the user inputs a member’s name who has NOT registered.
- The user’s name and account name will show up if the user inputs a member’s name who has registered.

<br>
<img src="https://user-images.githubusercontent.com/110411867/200311011-cb9b3759-fed3-4dbe-958c-b026cc7ee569.gif" width="500"/>

---

### ■ Username Update System

- Create an API for front end to send a request to edit username.
- Request Method: PATCH
- After changing to a new username, data will be updated from database as well.
- Use “session” to check if the user is logged in or not.
if the user is not logged in, other users are NOT able to send requests to backend from other places such as POSTMAN.

<br>
<img src="https://user-images.githubusercontent.com/110411867/200311004-d238acd8-d874-41c5-9f64-7c767978552c.gif" width="500"/>
