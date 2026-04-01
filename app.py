from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import better_sorce as db

app = Flask(__name__)
app.secret_key = "tdl_secret"


# ---------- DISPLAY PAGE ----------

@app.route("/", methods=["GET"])
def home():

    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]
    tasks = db.display_activity(user_id)

    return render_template("index.html", tasks=tasks)

# ---------- ADD TASK ----------

@app.route("/add", methods=["POST"])
def add():

    # ✅ ADD THIS CHECK
    if "user_id" not in session:
        return redirect("/login")

    task = request.form["task"]
    
    if task != "":
        user_id = session["user_id"]
        db.add_activity(task, user_id)

    return redirect("/")


# ---------- MARK DONE ----------

@app.route("/done/<int:id>", methods=["POST"])
def done(id):
    if "user_id" not in session:
        return redirect("/login")

    db.mark_done(id, session["user_id"])
    return redirect("/")


# ---------- DELETE TASK ----------

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    if "user_id" not in session:
        return redirect("/login")

    db.remove_activity(id, session["user_id"])
    return redirect("/")


# ---------- CLEAR TABLE ----------

@app.route("/clear", methods=["POST"])
def clear():
    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]
    db.table_clear(user_id)

    return redirect("/")


@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)
        db.register_user(username, hashed_password)

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = db.get_user(username)

        if user and check_password_hash(user[2], password):

            session["user_id"] = user[0]
            session["username"] = user[1].upper()   # ✅ ADD THIS LINE
            return redirect("/")

        flash("Account not found. Please register first.")
        return redirect("/register")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/login')

    user = db.get_user_by_id(session['user_id'])

    return render_template("profile.html", user=user)

@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]

    tasks = db.display_activity(user_id)

    total = len(tasks)
    done = len([t for t in tasks if t[3] == "done"])
    pending = total - done

    return render_template("dashboard.html",total=total,done=done,pending=pending)







if __name__ == "__main__":
    app.run(debug=True)