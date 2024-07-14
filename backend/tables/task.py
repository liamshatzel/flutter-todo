
def add_task(title, body, db):
    db.execute('INSERT into tasks (title, body) VALUES (?, ?)', (title, body))
    db.commit()

def get_tasks(db):
    return db.execute('SELECT * FROM tasks').fetchall()
