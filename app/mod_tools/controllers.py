from flask import Blueprint, request, send_file, jsonify
from app.mod_tools.api.helpers import *
import app.mod_tools.tools as tools

mod_tools = Blueprint("tools", __name__, url_prefix="/tools")
view_pool = {}

for module in getModule("./app/mod_tools/tools"):
    functions = getFunctions(module)
    for function in functions:
        view = lambda func=function[1]: func(**request.values.to_dict())
        view.__name__ = function[0]
        view_pool[function[0]] = view

for key in view_pool:
    value = view_pool[key]
    mod_tools.add_url_rule("/" + key, view_func=value, methods=["GET", "POST"])

@mod_tools.route("/")
def index():
    return "Welcome to Tools"
