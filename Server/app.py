from flask import Flask, request, send_file
from GPTmodel import giveResults
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app, methods=['GET', 'POST'])

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

            data = pd.read_excel(file_path)
            return send_file(file_path, mimetype='application/vnd.ms-excel', as_attachment=True)
        else:
            return 'No file uploaded'
        
@app.route("/response", methods=['GET'])
def get_response():
    return giveResults()

if __name__ == "__main__":
    app.run()
