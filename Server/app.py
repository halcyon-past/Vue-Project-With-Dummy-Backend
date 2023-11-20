from flask import Flask, request, send_file
from GPTmodel import giveResults, initialize
from flask_cors import CORS
import pandas as pd
import shutil
import os

app = Flask(__name__)
CORS(app, methods=['GET', 'POST'])
app.config['JSON_SORT_KEYS'] = False

path=['',]

@app.route("/", methods=['GET'])
def home():
    return "The Server is running"

@app.route("/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            # Save the file to a temporary location
            upload_folder = 'path'
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)
            path[0]=file_path
            initialize()
            return "File uploaded successfully"
        else:
            return 'No file uploaded'
        
@app.route("/download/<filetype>", methods=['GET'])
def download_file(filetype):
    if os.path.exists("path\\"+filetype+"_results.txt"):
        return send_file("path\\"+filetype+"_results.txt", mimetype='*/*', as_attachment=True)
    else:
        return 'No Such File Exists'
        
@app.route("/response", methods=['GET'])
def get_response():
    return giveResults(path[0])

@app.route("/cleardata", methods=['GET'])
def clear_data():
    if os.path.exists('path'):
        shutil.rmtree('path')
        return "Data Cleared"
    else:
        return "No Data to Clear"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=3000)
