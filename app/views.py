from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def Flask_index_page():
    return "İndex Page"

@app.route("/hello_flask")
def hello_flask():
    return render_template("Hello_flask.html")

@app.route("/hello_admin")
def hello_admin():
    return render_template("Hello_admin.html")

@app.route("/hello_user/<name>")
def hello_user (name):
    if name.lower() == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return render_template("Hello_user.html", username=name)

@app.route("/hello_add")
def hello_add():
    number1 = int(request.args["number1"])
    number2 = int(request.args["number2"])
    #/?number1=12&number2=22
    calculation_result = number1 + number2
    return render_template("Hello_add.html", numberone=number1, numbertwo=number2, result=calculation_result)

@app.route("/hello_login", methods=["POST","GET"])
def hello_login():
    if request.method == "POST":
        username = request.form["user_name"]
        return redirect(url_for("hello_user", name=username))
    else:
        return render_template("Hello_login.html")

@app.route("/hello_student")
def hello_student():
    return render_template("Hello_student.html")

@app.route("/hello_result", methods = ["POST", "GET"])
def Result ():
    ContextData = {
        "name" : request.form["name"],
        "mathematics" : request.form["mathematics"],
        "physics" : request.form["physics"],
        "chemistry" : request.form["chemistry"],
        "biology" : request.form["biology"]
    }

    return render_template("student_result.html", **ContextData)
