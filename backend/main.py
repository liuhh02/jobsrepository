import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfhandler import gettxt
import json
from classifyjob import classifyjob, clean_text
import pandas as pd
from jobs_connect import search_jobs
from similarity import calculate_similarity, find_similarity

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'docx', 'doc', 'rtf'}

app = Flask(__name__)

def clean_html(text):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    text = re.sub(cleanr, '', text)
    return text

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def createPDFDoc(fpath):
    fp = open(fpath, 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser, password='')
    # Check if the document allows text extraction. If not, abort.
    return document.is_extractable
	
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
            if createPDFDoc(file_path):
                data = gettxt(file_path)
                if len(json.loads(data)) > 0:
                    job_title = classifyjob(data)
                    jobs = search_jobs(job_title)
                    df = pd.DataFrame(jobs)
                    df['title'] = df['title'].apply(clean_html)
                    df['description'] = df['description'].apply(clean_html)
                    jobs_dict = find_similarity(df, data)
                    return jobs_dict

                else:
                    return "Couldn't find any skills or certifications on your resume, sorry"
            else:
                return 'No extractrable text found.'
    else:
        return redirect('http://resumatch.online')
		
if __name__ == '__main__':
   app.run(debug = True)
