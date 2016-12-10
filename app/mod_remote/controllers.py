from flask import Blueprint, request, send_file, jsonify, render_template
from app.mod_remote.api.remotedesktop import RemoteDesktop

mod_remote = Blueprint("remote", __name__, url_prefix="/remote")
remoteDesktop = RemoteDesktop()

@mod_remote.route('/')
def remote():
    return render_template('remote/remote.html')

@mod_remote.route('/desktop.jpeg')
def remoteGetPic():
    pic = remoteDesktop.getPicture()
    return send_file(pic, mimetype='image/jpeg')

@mod_remote.route('/leftClick')
def remoteLeftClick():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    except:
        return 'error'
    remoteDesktop.click(x, y, "left")
    return 'done'

@mod_remote.route('/rightClick')
def remoteRightClick():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    except:
        return 'error'
    remoteDesktop.click(x, y, "right")
    return 'done'

@mod_remote.route('/size')
def remoteSize():
    size = remoteDesktop.getSize()
    return jsonify(**{"width": size[0], "height": size[1]})

@mod_remote.route('/typewrite')
def remoteTypewrite():
    try:
        data = request.args.get('data')
    except:
        return 'error'
    remoteDesktop.typewrite(data)
    return 'done'
