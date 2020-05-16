import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import textract

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'docx', 'doc', 'rtf'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'no file there mate'
        if file and allowed_file(file.filename):
            file_path = 'uploads/{}'.format(secure_filename(file.filename))
            file.save(file_path)
            return textract.process(file_path)
    else:
        return render_template('index.html')
		
if __name__ == '__main__':
   app.run(debug = True)