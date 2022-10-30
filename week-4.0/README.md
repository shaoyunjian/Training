# Build Web Application Using Python Flask

### ■ Build an Index Page

- Create a form including input space for username & password, and create a login button.
- Use the HTTP POST method to send request.

<img src="https://user-images.githubusercontent.com/110411867/198884440-581aac7c-5f65-4814-bcaa-1a6ea457f1d6.png" width="500"/>

<hr/>

### ■ Login Success Page

- After logging in successfully, the current page will be redirected from http://127.0.0.1:3000 to http://127.0.0.1:3000/member
- A login success message will be displayed on the page if the user inputs the correct username and password.

<img src="https://user-images.githubusercontent.com/110411867/198884442-aa49c362-bafe-48ef-ab5a-6019e0c5b2fa.png" width="500"/>

<hr/>

### ■ Login Failed Message

- After logging in successfully, the current page will be redirected from http://127.0.0.1:3000 to [http://127.0.0.1:3000/error?message=請輸入正確的帳號密碼](http://127.0.0.1:3000/error?message=%E8%AB%8B%E8%BC%B8%E5%85%A5%E6%AD%A3%E7%A2%BA%E7%9A%84%E5%B8%B3%E8%99%9F%E5%AF%86%E7%A2%BC)
- A login failed message will be displayed on the page if the user inputs the wrong username and password or if the input is empty.
- The URL of the login-failed page will include query strings. The login-failed message will be displayed on the page and URL at the same time.

<img src="https://user-images.githubusercontent.com/110411867/198884444-5ce26cf8-c4d7-4b62-abee-b3a4606088af.png" width="500"/>
<img src="https://user-images.githubusercontent.com/110411867/198884445-28ec5eca-4ae3-49b6-9a55-e5cee2f65f34.png" width="500"/>

<hr/>

### ■ Sessions are Stored Client-side in Browser Cookies

- Login Success Page URL: [http://127.0.0.1:3000/member](http://127.0.0.1:3000/member)
- If the user clicks the button to log out, the page will be redirected to the index page.
- Even though the user tries to use the URL: [http://127.0.0.1:3000/member](http://127.0.0.1:3000/member) to access the member page, the page will be redirected immediately.
- Only if the status is login, users are able to access the member page.

<img src="https://user-images.githubusercontent.com/110411867/198884446-598a262e-4295-4166-b0fd-b90d6f6b5981.png" width="500"/>

<hr/>

### ■ Flask Dynamic Routing

- Input a number and click the button, the page will be redirected to http://127.0.0.1:3000/square/number, and the result will be the number’s square.
- The number should be a positive integer.
- For example, if you input a number of 10, the result will be 100.

<img src="https://user-images.githubusercontent.com/110411867/198884447-a053869e-4d34-4975-908b-6d4d7f83db62.png" width="500"/>
<img src="https://user-images.githubusercontent.com/110411867/198884449-d5cd2a77-34e2-4172-8d82-04209633a0a1.png" width="500"/>

<hr/>

### ■ Encrypt String and Store it in Cookies instead of using Session.

⁂ URL：[https://github.com/shaoyunjian/training/tree/main/week-4.1](https://github.com/shaoyunjian/training/tree/main/week-4.1)

- Encrypt String and Store it in Cookies instead of using Session.
- Using `Flask Cryptography Package` to encrypt and decrypt.

<img src="https://user-images.githubusercontent.com/110411867/198884451-d6c1f5f8-4404-46b6-995e-44f7c9f577fd.png" width="500"/>
