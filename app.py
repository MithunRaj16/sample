from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    "Mithun": "123",
    "aadin": "234",
}
@app.route("/", methods=["GET", "POST"])
def login():
    message = ""  # Initialize an empty message
    message_class = ""  # Initialize an empty class for styling
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.get(username) == password:
            message = "Login successful"
            message_class = "success"  # Apply "success" class for green color
        else:
            message = "Login failed"
            message_class = "error"  # Apply "error" class for red color
    return render_template("login.html", message=message, message_class=message_class)



if __name__ == "__main__":
    app.run(port=8000)
