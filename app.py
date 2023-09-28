import os
import json

from flask import Flask, flash, render_template, request, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_VID_DIR = '/volumn/uploads/vids'
UPLOAD_META_DIR = '/volumn/uploads/meta'

ALLOWED_EXTENSIONS = {'mp4', 'json'}
REQUIRED_EXTENSIONS = {'mp4', 'json'}

app = Flask(__name__, template_folder='map_webapp')
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1000 * 1000
app.config['UPLOAD_VID_DIR'] = UPLOAD_VID_DIR
app.config['UPLOAD_META_DIR'] = UPLOAD_META_DIR


UPLOAD_META_DB = 'upload_data.json'



app.config['UPLOAD_META_DB'] = os.path.join(app.static_folder,UPLOAD_META_DB)
print('@'*20)
print(app.static_folder)
print(UPLOAD_META_DB)
print(app.config['UPLOAD_META_DB'])

app.secret_key = "secret-key-placeholder"

# setup directories
if not os.path.exists(app.config['UPLOAD_VID_DIR']):
    os.makedirs(app.config['UPLOAD_VID_DIR'], exist_ok=True)

if not os.path.exists(app.config['UPLOAD_META_DIR']):
    os.makedirs(app.config['UPLOAD_META_DIR'], exist_ok=True)
    


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_valid_upload(files):
    if len(files) != 2:
        return False
    
    if not all([allowed_file(f.filename) for f in files]):
        return False

    exts = [f.filename.rsplit('.', 1)[1].lower() for f in files]
    for ext in REQUIRED_EXTENSIONS:
        if ext not in exts:
            return False
    
    return True


def register_meta(meta_path, vid_path):
    with open(meta_path, 'r') as f:
        meta = json.load(f)
    
    meta['video_path'] = vid_path.rsplit('/', 1)[-1]

    with open(app.config['UPLOAD_META_DB'], 'r') as f:
        db = json.load(f)


    db.append(meta)
    with open(app.config['UPLOAD_META_DB'], 'w') as f:
        json.dump(db, f, indent=2)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        # file = request.files['file']
        file = request.files.getlist("file")
        
        print('-'*20)
        print(file)
        print('-'*20)        

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if len(file)==0 or any([f.filename=='' for f in file]): #file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        # only allow json and video
        if not is_valid_upload(file):
            flash('Please upload .json and .mp4 files')
            return redirect(request.url)


        # handle uploads
        filenames = [secure_filename(f.filename) for f in file]
        file_map = dict(zip(filenames, file))

        for filename, f in file_map.items():
            if filename.rsplit('.', 1)[1] == 'mp4':
                vid_path = os.path.join(app.config['UPLOAD_VID_DIR'], filename)
                f.save(vid_path)
            else:
                meta_path = os.path.join(app.config['UPLOAD_META_DIR'], filename)
                f.save(meta_path)

        # add to existing dataset        
        register_meta(meta_path, vid_path)
        


        return redirect(url_for('main'))
    return render_template("./upload.html")


@app.route(app.static_folder+'/<path:filename>')
def serve_video(filename):
    return send_from_directory(app.static_folder, filename)


@app.route('/')
def main():
    print(os.listdir())
    return render_template('./main.html')

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')