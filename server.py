#jinja is for templating{{python code}}
# footer should be updated to current year
from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)

@app.route('/')
def homeroute():
    random_number = random.randint(1, 10)
    year=datetime.datetime.now().year
    return render_template("index.html",random_number=random_number,year=year)
@app.route("/<int:value>")
def fun(value):
    random_number = random.randint(1, value)
    year=datetime.datetime.now().year
    return render_template("index.html",random_number=random_number,year=year)


if __name__ == "__main__":
    app.run(debug=True)
