from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='map_webapp')

@app.route('/')
def hello():
    print('HERE')
    print(os.listdir())
    return render_template('./main.html')

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')