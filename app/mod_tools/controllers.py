from flask import Blueprint, request, send_file, jsonify
from app.mod_tools.api.helpers import *
import app.mod_tools.tools as tools
mod_tools = Blueprint("tools", __name__, url_prefix="/tools")

for function in getFunctions(tools):
    print function

@mod_tools.route('/')
def remote():
    return render_template('remote/remote.html')
