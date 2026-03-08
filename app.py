from flask import Flask, render_template, request, redirect 
import better_sorce as db

app=Flask(__name__)

@app.route("/")
def home():
    task=db.display_activity()
    return render_template("index.html",tasks=task)

@app.route("/add",methods=["POST"])
def add():
    task=request.form["task"]
    db.add_activity(task)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    db.remove_activity(id)
    return redirect("/")

@app.route("/clear")
def clear():
    db.table_clear()
    return redirect("/")

@app.route("/done/<int:id>")
def done(id):
    db.mark_done(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)