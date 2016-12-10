from flask import Blueprint, request, jsonify, render_template
from app.mod_matmanangcao.api.matmanangcao import modular_sqrt, elliptic
mod_matmanangcao = Blueprint("matmanangcao", __name__, url_prefix="/matmanangcao")

@mod_matmanangcao.route('/')
def index():
    return render_template('matmanangcao/matmanangcao.html')

@mod_matmanangcao.route('/aaa')
def index2():
    return render_template('matmanangcao/matmanangcao.html')


@mod_matmanangcao.route('/api/modular_sqrt/')
def modular_sqrt_api():
    try:
        p = int(request.args.get('p'))
        a = int(request.args.get('a'))
        return jsonify(**{"status" : 200, "data" : modular_sqrt(a, p)})
    except Exception, e:
        print str(e)
        return jsonify(**{"status" : 500, "msg" : "Invalid request"})

@mod_matmanangcao.route('/api/elliptic/')
def elliptic_api():
    min_m = int(request.args.get('min_m'))
    max_m = int(request.args.get('max_m'))
    p = int(request.args.get('p'))
    A = int(request.args.get('A'))
    B = int(request.args.get('B'))
    return jsonify(**{"status" : 200, "data" : elliptic(p, A, B, [min_m, max_m])})
