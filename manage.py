import pymongo
from flask import Flask, request, render_template, flash, redirect
import repository
import config


if __name__ == "__main__":
    mongo_client = pymongo.MongoClient(config.MONGODB_HOST)
    r = repository.ToDoRepository(mongo_client, config.MONGODB_DATABASE, config.MONGODB_COLLECTION)
    app = Flask(__name__)
    app.secret_key = "gci"

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == "POST":
            title = request.form['title']
            req = repository.ToDo(title)
            r.create(req)
            flash("Activity has been added successfuly")
            return redirect('/')
        if request.method == "GET":
            activities = r.find_all()
            print(activities)
            return render_template('index.html', activities = activities)

    app.run(host='0.0.0.0')

