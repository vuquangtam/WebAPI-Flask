# Import flask and template operators
from flask import Flask, render_template, redirect

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
# db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_remote.controllers import mod_remote as remote_module
from app.mod_shell.controllers import mod_shell as shell_module
from app.mod_auth.controllers import auth

@app.before_request
@auth.login_required
def auth():
    pass
  
@app.route('/')
def index():
    return "Welcome to VIPTAM API"


# Register blueprint(s)
app.register_blueprint(remote_module)
app.register_blueprint(shell_module)

# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()