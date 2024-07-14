import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.get("/test")
    def test():
        from .task import get_tasks, add_task
        from .db import get_db
        db = get_db()
        add_task("test", 'dodo', db)
        add_task("test2", 'liam', db)
        add_task("test3", 'payton', db)
        return get_tasks(db)

    from . import db
    db.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()

