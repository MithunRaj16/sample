from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    "Mithun": "123",
    "aadin": "234",
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.get(username) == password:
            return redirect(url_for('login_success'))
        else:
            return redirect(url_for('login_failed'))
    return render_template("login.html")

@app.route("/login_success")
def login_success():
    return render_template("result.html", message="Login Successful", message_class="success")

@app.route("/login_failed")
def login_failed():
    return render_template("result.html", message="Login Failed", message_class="error")

if __name__ == "__main__":
    app.run(port=8000)
