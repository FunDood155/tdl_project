from flask import Flask, render_template, request, redirect, session
import better_source as db

app = Flask(__name__)
app.secret_key = "tdl_secret"


# ---------- DISPLAY PAGE ----------

@app.route("/", methods=["GET"])
def home():

    user_id = 1
    tasks = db.display_activity(user_id)

    return render_template("index.html", tasks=tasks)


# ---------- ADD TASK ----------

@app.route("/add", methods=["POST"])
def add():

    task = request.form["task"]
    
    if task != "":
        user_id = 1
        db.add_activity(task, user_id)

    return redirect("/")


# ---------- MARK DONE ----------

@app.route("/done/<int:id>", methods=["POST"])
def done(id):

    db.mark_done(id)

    return redirect("/")


# ---------- DELETE TASK ----------

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    db.remove_activity(id)

    return redirect("/")


# ---------- CLEAR TABLE ----------

@app.route("/clear", methods=["POST"])
def clear():

    user_id = 1
    db.table_clear(user_id)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)