from flask import Flask, request, send_file, jsonify
from api.remotedesktop import RemoteDesktop
import subprocess
import os
app = Flask(__name__)
remoteDesktop = RemoteDesktop()

@app.route('/')
def index():
    return "Welcome to VIPTAM API"

@app.route('/shell')
def shell():
    return app.send_static_file('shell.html')
    
@app.route('/shell/get')
def shellGet():
    command = ""
    result = ""
    try:
        command = request.args.get("cmd")
        result = os.popen(command).read()
    except Exception,e:
        print str(e)
    return result

@app.route('/remote')
def remote():
    return app.send_static_file('remote.html')

@app.route('/remote/desktop.jpeg')
def remoteGetPic():
    pic = remoteDesktop.getPicture()
    return send_file(pic, mimetype='image/jpeg')

@app.route('/remote/leftClick')
def remoteLeftClick():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    except:
        return 'error'
    remoteDesktop.click(x, y, "left")
    return 'done'

@app.route('/remote/rightClick')
def remoteRightClick():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    except:
        return 'error'
    remoteDesktop.click(x, y, "right")
    return 'done'

@app.route('/remote/size')
def remoteSize():
    size = remoteDesktop.getSize()
    return jsonify(**{"width": size[0], "height": size[1]})

@app.route('/remote/typewrite')
def remoteTypewrite():
    try:
        data = request.args.get('data')
    except:
        return 'error'
    remoteDesktop.typewrite(data)
    return 'done'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
