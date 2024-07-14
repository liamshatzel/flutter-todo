from flask import jsonify

def add_task(title, body, db):
    db.execute('INSERT into task (title, body) VALUES (?, ?)', (title, body))
    db.commit()

def get_tasks(db):
    rows_list = [dict(row) for row in db.execute('SELECT * FROM task').fetchall()]
    for row in db.execute('SELECT * FROM task').fetchall(): print (row)
    for row in rows_list: print(row)
    return jsonify(rows_list)
