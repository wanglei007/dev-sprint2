# This is whre you can start you python file for your week1 web app
# Name: Lei Wang

import flask, flask.views
import os
import functools

app = flask.Flask(__name__)

app.secret_key = "nonono"

users = {'Lei':'1234'}

class Main(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		if 'logout' in flask.request.form:
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for('index'))
		required = ['username', 'passwd']
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required.", format(r))
				return flask.redirect(flask.url_for('index'))
		username = flask.request.form['username']
		passwd = flask.request.form['passwd']
		if username in users and users[username]== passwd:
			flask.session['username'] = username
		else:
			flask.flash("username does not exist or incorrect password")
		return flask.redirect(flask.url_for('index'))

def login_required(method):
	@functools.wraps(method)
	def wrapper(*args, **kwargs):
		if 'username' in flask.session:
			return method(*args, **kwargs)
		else:
			flask.flash("A login is required ot see the page!")
			return flask.redirect(flask.url_for('index'))
	return wrapper

class  Remote(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('remote.html')

	@login_required
	def post(self):
		result = eval (flask.request.form['expression'])
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))

class  Music(flask.views.MethodView):
	@login_required
	def get(self):
		songs = os.listdir('static/music')
		return flask.render_template('music.html', songs = songs)

class  ShowFiles(flask.views.MethodView):
	@login_required
	def get(self):
		files = os.listdir('templates')
		return flask.render_template('show_files.html', files = files)

	@login_required
	def post(self):
		filename = flask.request.form['expression']
		fd = os.open(filename,os.O_RDWR)

		result = os.read(fd,100)
		os.close(fd)
		
		flask.flash(result)
		return flask.redirect(flask.url_for('showfiles'))

app.add_url_rule('/', view_func=Main.as_view('index'),
					methods=['GET', 'POST'])
app.add_url_rule('/remote/', view_func=Remote.as_view('remote'), 
					methods=['GET', 'POST'])
app.add_url_rule('/music/', view_func=Music.as_view('music'), 
					methods=['GET'])
app.add_url_rule('/show_files/', view_func=ShowFiles.as_view('showfiles'), 
					methods=['GET'])

app.debug = True
app.run(port=5001)