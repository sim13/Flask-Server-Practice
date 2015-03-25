# all the imports 
import sqlite3
from contextlib import closing 
from flask import Flask , request, session, g, redirect , url_for , \
abort, render_template, flash

#configuration

DATABASE = '/tmp/flaskr.db'
DEBUG = True 
SECRET_KEY = 'development key'
USERNAME ='admin'
PASSWORD = 'sunGAB1313'

app = Flask(__name__)
app.config.from_object(__name__)
@app.route('/')
def  render() :
	return app.send_static_file('simwahal.html')

@app.route('/<path:path>')
def  static_proxy(path) :
	 return app.send_static_file(path)
if __name__ == 'main' :
	app.run() 


def connect_db() :
	return sqlite3.connect(app.config['DATABASE'])
def init_db():
	with closing(connect_db()) as db :
		 with app.open_resource('schema.sql', mode = 'r') as f :
		 	db.cursor().executescript(f.read())
		 db.commit()
@app.before_request
def before_request() :
	g.db = connect_db() 
@app.teardown_request 
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None :
		db.close()
@app.route('/')
def show_entries():
	cur = g.db.execute('')


