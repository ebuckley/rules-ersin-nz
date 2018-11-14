from flask import current_app, g
import records

def get_db():
    if 'db' not in g:
        g.db = records.Database(current_app.config['DATABASE'])
    return g.db