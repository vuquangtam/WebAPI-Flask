from flask import Blueprint, request, render_template
from app.mod_shell.api.shell import cmd

mod_shell = Blueprint("shell", __name__, url_prefix="/shell")

@mod_shell.route('/')
def shell():
    return render_template('shell/shell.html')
    
@mod_shell.route('/get')
def shellGet():
    command = ""
    result = ""
    try:
        command = request.args.get("cmd")
        result = cmd(command)
    except Exception, e:
        print str(e)
    return result
