import os
from flask import Flask, request, jsonify, render_template
from model import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

UPLOAD_FOLDER = os.path.join('static','uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    caption= predict(f)
    #caption = "test_caption"
    #return redirect(url_for('hello', caption=caption))
    return render_template('index.html', caption=caption, image_path=f)
    
if __name__ == "__main__":
    app.run(debug=True)
