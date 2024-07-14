import os

from flask import (
    Flask,
    request
)

DATABASE = "todo.db"

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return 'Index Page'

if __name__ == "__main__":
    app.run()
