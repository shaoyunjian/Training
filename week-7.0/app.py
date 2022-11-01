from flask import Flask, render_template, redirect, request, session, url_for, jsonify
from mysql.connector.pooling import MySQLConnectionPool
from dotenv import load_dotenv
import os
load_dotenv() 
USER=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")
SECRET_KEY=os.getenv("SECRET_KEY")
app = Flask(__name__)
app.secret_key = SECRET_KEY

cnxpool = MySQLConnectionPool(
  pool_name = "mypool",
  pool_size=10,
  host="localhost",
  port="3306", 
  user=USER, 
  password=PASSWORD, 
  database="website"
)

# Homepage
@app.route("/")
def index():
  return render_template("index.html")

# Signup
@app.route("/signup", methods=["POST"])
def signup():
  try:
    cnx1 = cnxpool.get_connection()
    cursor1 = cnx1.cursor()
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    select = "SELECT member.username FROM member WHERE username=%s"
    values = (username,)
    cursor1.execute(select, values)
    usernameDB = cursor1.fetchone()
    if not name or not username or not password:
      return redirect(url_for("error", message="請不要有空白"))
    elif usernameDB == None:
      insert = "INSERT INTO member(name, username, password) VALUES (%s, %s, %s)"
      values = (name, username, password)
      cursor1.execute(insert, values)
      cnx1.commit()
      return redirect("/")
    else:
      return redirect(url_for("error", message="帳號已經被註冊"))
  finally:
    cursor1.close()
    cnx1.close()

# Login
@app.route("/signin", methods=["POST"])
def signin():
  with cnxpool.get_connection() as cnx2:
    with cnx2.cursor() as cursor2:
      username = request.form["username"]
      password = request.form["password"]
      select = "SELECT * FROM member WHERE username=%s AND password=%s"
      values = (username, password)
      cursor2.execute(select, values)
      user = cursor2.fetchone()
      if not username or not password:
        return redirect(url_for("error", message="請不要有空白"))
      elif user == None:
        return redirect("/error?message=帳號或密碼輸入錯誤")
      else:
        session["loggedin"] = True
        session["id"] = user[0]
        session["name"] = user[1]
        session["username"] = username
        session["password"] = password
        return redirect("/member")

# Login success
@app.route("/member")
def member():
  with cnxpool.get_connection() as cnx3:
    with cnx3.cursor() as cursor3:
      if "loggedin" in session:
        select_message = ("SELECT member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id ORDER BY message.time DESC")
        cursor3.execute(select_message)
        messages = cursor3.fetchall()
        return render_template("member.html", name=session["name"], messages=messages)
      else:
        return redirect("/")

# Message sending
@app.route("/message", methods=["POST"])
def message():
  with cnxpool.get_connection() as cnx4:
    with cnx4.cursor() as cursor4:
      message = request.form["message"]
      if not message:
        return redirect("/member")
      else:
        insert = "INSERT INTO message(member_id, content) VALUES (%s, %s)"
        values = (str(session["id"]), message)
        cursor4.execute(insert, values)
        cnx4.commit()
        return redirect("/member")

# Login failed
@app.route("/error")
def error():
  errorMessage = request.args.get("message")
  return render_template("error.html", message=errorMessage)

# Sign out and back to homepage
@app.route("/signout")
def signout():
  session.pop("loggedin", None)
  session.pop("id", None)
  session.pop("name", None) 
  session.pop("username", None) 
  session.pop("password", None) 
  return redirect("/")

# Week7 Added: API for member information
@app.route("/api/member", methods=["GET"])
def get_member_data():
  username = request.args.get("username", None)
  with cnxpool.get_connection() as cnx5:
    with cnx5.cursor() as cursor5:
      select = "SELECT * FROM member WHERE username=%s"
      values = (username,)
      cursor5.execute(select, values)
      user = cursor5.fetchone()
      if session and user:
        return jsonify(
          {
            "data":{
              "id": user[0],
              "name": user[1],
              "username": user[2]
            }
          }
        ) 
      else: 
        return jsonify({"data": None})
  
# Week7 Added: API for revising user's name
@app.route("/api/member", methods=["PATCH"])
def revise_member_data(): 
  name = request.args["username"]
  if session and name != "":
    with cnxpool.get_connection() as cnx6:
      with cnx6.cursor() as cursor6:
        select = "UPDATE member SET name=%s WHERE username= %s"
        values = (name, session["username"])
        cursor6.execute(select, values)
        cnx6.commit()
    return jsonify({"ok": True}) 
  else: 
    return jsonify({"error": True})


app.run(port=3000, debug=True)