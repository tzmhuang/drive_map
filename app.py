from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__, template_folder='map_webapp')

@app.route(app.static_folder+'/<path:filename>')
def serve_video(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/upload', methods=["GET", "POST"])
def file_upload():
    print('HERERRERERR')
    return render_template("./upload.html")

@app.route('/')
def hello():
    print(os.listdir())
    return render_template('./main.html')

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')