# Login, Registration, and Message System
- Creating a login, registration, and message system with Python Flask and MySQL.
- Importing `mysql.connector` module to connect MySQL database in Python.
- Connection pooling.

### ■ Technologies

- Front-end: HTML/CSS/JavaScript
- Back-end: Python Flask
- Database: MySQL

<hr>

### ■ Registration System

- Route: / ⇒ /signup
- HTTP Method: POST
1. **Registration Process (Success)**
    - The front end will send a request including the user’s information to the back end after a user fills out the name(姓名), username(帳號), and password(密碼) and clicks the signup(註冊) button.
    - Information will be added to the database after registering successfully, and the page will return back to the homepage.
    <br>
    <img src="https://user-images.githubusercontent.com/110411867/200277045-0efde8f7-3248-473d-bb63-f077a2ebdf0c.gif" width="500"/>

2. **Registration Process (Failed)**
    - If the username already exists, the page will return to the failed page.
    - If an input field is empty, the page will return to the failed page.
    <br>
    <img src="https://user-images.githubusercontent.com/110411867/200277051-b1271c17-bf9d-41ea-979c-48a3b1acd768.gif" width="500"/>
    
<hr>

### ■ Login System

1. **Login Success Page**
    - Route: / ⇒   /signin ⇒  /member
    - HTTP Method: POST
2. **Login Failed Page**
    - Route: / ⇒  /signin ⇒  /error?message=自訂的錯誤訊息
    - HTTP Method: GET
    
    <br>
    <img src="https://user-images.githubusercontent.com/110411867/200277033-023b0a64-1d1c-4e73-bfd2-6548be44c087.gif" width="500"/>

<hr>

### ■ Message/Chat System

- Route: /member ⇒ /message ⇒ /member
- HTTP Method: POST
- [https://gyazo.com/ce6ba344b111aaa741b2d42926144d96](https://gyazo.com/ce6ba344b111aaa741b2d42926144d96)
  
  <br>
  <img src="https://user-images.githubusercontent.com/110411867/200277053-5beacc75-6948-4277-b083-c94afa8cac02.gif" width="500"/>

<hr>

### ■ Logout System

- Route: /member ⇒ /signout ⇒ /member
- HTTP Method: GET
  
  <br>
  <img src="https://user-images.githubusercontent.com/110411867/200277059-6b3f60fd-13f6-431b-a552-dd0bcbe53c08.gif" width="500"/>