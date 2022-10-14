from flask import Flask, make_response, render_template, redirect, request
from cryptography.fernet import Fernet
app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)
login = f.encrypt(b'login')
logout= f.encrypt(b'logout')

# 首頁
@app.route("/")
def index():
  return render_template("index.html")

# 登入驗證功能
@app.route("/signin", methods=["POST"])
def signIn():
  accountName = request.form["account-name"]
  password = request.form["password"]
  if accountName == "test" and password == "test":
    response = make_response(redirect("/member"))
    response.set_cookie("loginStatus", login)
    return response
  else:
    return redirect("/error?message=請輸入正確的帳號密碼")

# 登入成功
@app.route("/member")
def member():
  if request.cookies["loginStatus"] == login.decode("utf-8"): 
    return render_template("member.html")
  else:
    return redirect("/")

# 登入失敗
@app.route("/error")
def error():
  errorMessage = request.args.get("message")
  return render_template("error.html", message=errorMessage)

# 登出，轉回首頁
@app.route("/signout")
def signOut():
  response = make_response(redirect("/"))
  response.delete_cookie("loginStatus")
  response.set_cookie("loginStatus",logout)
  return response

app.run(port=3000)
