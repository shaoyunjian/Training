import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv() 
USER=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")
SECRET_KEY=os.getenv("SECRET_KEY")

from flask import Flask, render_template, redirect, request, session, url_for
app = Flask(__name__)
app.secret_key = SECRET_KEY

connection = mysql.connector.connect(
  host='localhost',
  port='3306',
  user=USER,
  password=PASSWORD,
  database="website")
cursor = connection.cursor()

# Homepage
@app.route("/")
def index():
  return render_template("index.html")

# Signup
@app.route("/signup", methods=["POST"])
def signup():
  name = request.form["name"]
  username = request.form["username"]
  password = request.form["password"]
  select = "SELECT member.username FROM member WHERE username=%s"
  cursor.execute(select, (username,))
  usernameDB = cursor.fetchone()

  if not name or not username or not password:
    return redirect(url_for("error", message="請不要有空白"))
  elif usernameDB == None:
    insert = "INSERT INTO member(name, username, password) VALUES (%s, %s, %s)"
    values = (name, username,password)
    cursor.execute(insert, values)
    connection.commit()
    return redirect("/")
  else:
    return redirect(url_for("error", message="帳號已經被註冊"))

# Login
@app.route("/signin", methods=["POST"])
def signin():
  username = request.form["username"]
  password = request.form["password"]
  select = "SELECT * FROM member WHERE username=%s AND password=%s"
  cursor.execute(select, (username, password),)
  user = cursor.fetchone()
  connection.commit()
  if not username or not password:
    return redirect(url_for("error", message="請不要有空白"))
  elif user == None:
    return redirect("/error?message=帳號或密碼輸入錯誤")
  else:
    session['loggedin'] = True
    session['id'] = user[0]
    session["name"] = user[1]
    session["username"] = username
    session["password"] = password 
    return redirect("/member")

# Login success
@app.route("/member")
def member():
  if 'loggedin' in session:
    select_message = ("SELECT member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id ORDER BY message.id DESC")
    cursor.execute(select_message)
    messages = cursor.fetchall()
    return render_template("member.html", name=session["name"], messages=messages)
  else:
    return redirect("/")

# Message
@app.route("/message", methods=["POST"])
def message():
  message = request.form["message"]
  if not message:
    return redirect("/member")
  else:
    insert = "INSERT INTO message(member_id, content) VALUES (%s, %s)"
    cursor.execute(insert, (str(session['id']), message))
    connection.commit()
    return redirect("/member")


# Login failed
@app.route("/error")
def error():
  errorMessage = request.args.get("message")
  return render_template("error.html", message=errorMessage)

# Sign out and back to homepage
@app.route("/signout")
def signout():
  session.pop('loggedin', None)
  session.pop('id', None)
  session.pop("name", None) 
  session.pop("username", None) 
  session.pop("password", None) 
  return redirect("/")

app.run(port=3000)
cursor.close()
connection.close()