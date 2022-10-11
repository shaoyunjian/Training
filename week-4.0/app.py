from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "anything"

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
    session["user"] = "test"
    return redirect("/member")
  else:
    return redirect("/error?message=請輸入正確的帳號密碼")

# 登入成功
@app.route("/member")
def member():
  if "user" in session: 
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
  session.pop("user", None) 
  return redirect("/")

# 計算正整數的平方
@app.route("/square/<number>")
def number(number):
  number = int(number)
  result = str(number * number)
  return render_template("square.html", number=result)


app.run(port=3000)
