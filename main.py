import flask

app = flask.Flask("To_do_app")
AllTasks = ["Wash the dishes","Finish homework"]

@app.route("/Tasks", methods=["POST", "GET"])
def Tasks():
    if flask.request.method == "POST":
        Task = flask.request.form.get("Task")
        print(Task)
        AllTasks.remove(Task)
    return flask.render_template ("Tasks.html",AllTasks = AllTasks)
@app.route("/Addtasks", methods=["POST", "GET"])
def addTasks():
    if flask.request.method == "POST":
        Task = flask.request.form.get("Task")
        print(Task)
        AllTasks.append(Task)
    return flask.render_template ("Addtasks.html")
#app.run()