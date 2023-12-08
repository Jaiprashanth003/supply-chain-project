from flask import *
import ibm_db

conn = ibm_db.connect(
    "DATABASE = bludb;HOSTNAME = b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT = 32304;SECURITY = SSL;SSLServerCertificate = DigiCertGlobalRootCA.crt;UID = kkr03620 ; PWD = oX8UGWmWiJLF78Zy",
    "",
    "",
)
print(conn)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login1", methods=["POST"])
def login1():
    NAME = request.form["NAME"]
    EMAIL = request.form["EMAIL"]
    sql = "SELECT * FROM  REGISTER WHERE NAME =? AND EMAIL =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, NAME)
    ibm_db.bind_param(stmt, 1, EMAIL)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    print(account)
    print(NAME, EMAIL)

    if account:
        return render_template("login.html", pred="login successful")
    else:
        return render_template(
            "register.html", pred="login unsuccesfull invalid password"
        )


@app.route("/register1", methods=["POST"])
def rigister1():
    x = [x for x in request.form.values()]
    print(x)
    NAME = [0]
    EMAIL = [1]
    PASSWORD = [2]
    sql = "SELECT * FROM REGISTER WHERE EMAIL =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, EMAIL)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    print(account)
    if account:
        return render_template("login.html", pred="you already logged in")
    else:
        insert_sql = "INSERT INTO REGISTER VALUES(?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, NAME)
        ibm_db.bind_param(prep_stmt, 2, EMAIL)
        ibm_db.bind_param(prep_stmt, 3, PASSWORD)
        ibm_db.execute(prep_stmt)
        return render_template("login.html", pre="registration succesful")


if __name__ == "__main__":
    app.run(debug=True, port=1111)
