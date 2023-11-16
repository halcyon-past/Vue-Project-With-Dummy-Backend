from flask import Flask, request, send_file
from GPTmodel import giveResults, initialize
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app, methods=['GET', 'POST'])
app.config['JSON_SORT_KEYS'] = False

path=['',]

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
        
@app.route("/download", methods=['GET'])
def download_file():
    if len(path[0])>0:
        return send_file(path[0], mimetype='*/*', as_attachment=True)
    else:
        return 'No file uploaded yet'
        
@app.route("/response", methods=['GET'])
def get_response():
    return giveResults(path[0])

if __name__ == "__main__":
    app.run(debug=True)
