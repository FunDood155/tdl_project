from flask import Flask, render_template, request, redirect
import better_sorce as db

app = Flask(__name__)


# ---------- DISPLAY PAGE ----------

@app.route("/", methods=["GET"])
def home():

    tasks = db.display_activity()

    return render_template("index.html", tasks=tasks)


# ---------- ADD TASK ----------

@app.route("/add", methods=["POST"])
def add():

    task = request.form["task"]

    db.add_activity(task)

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

    db.table_clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)