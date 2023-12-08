from flask import *

app = Flask(__name__, template_folder="template")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login1", methods=["POST", "GET"])
def login1():
    NAME = request.form.get("NAME", False)
    EMAIL = request.form.get("EMAIL", False)
    if NAME == "jk" and EMAIL == "jk@gmail.com":
        return "welcome to portel"
    else:
        return render_template("register.html")


@app.route("/register1", methods=["POST", "GET"])
def register1():
    NAME = request.form.get("NAME", False)
    EMAIL = request.form.get("EMAIL", False)
    PASSWORD = request.form.get("PASSWORD", False)
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
