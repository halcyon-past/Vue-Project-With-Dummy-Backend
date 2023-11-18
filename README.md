# RFQ Splitter Dummy - ```Vue + VITE```

- To run the programme go to Server Folder First and type
  ```
  cd Server
  ```
- Then Install all dependencies by typing
  ```
  pip install -r requirements.txt
  ```
- Then Run the flask server by
  ```
  python app.py
  ```
- Then return to the root directory
  ```
  cd ..
  ```
- Then go to the Client folder
  ```
  cd Client
  ```
- Then install all the dependencies by typing
  ```
  npm i
  ```
- Then start the Vite Server by
  ```
  npm run dev
  ```
  
  
- Then Check the website at your https://localhost:5173
- To Check the API go to https://localhost:3000

## Details

- This is the Frontend and a supporting dummy backend for a project of RFQ Splitter
- To Update the backend just modify the [GPTmodel.py](https://github.com/halcyon-past/Vue-Project-With-Dummy-Backend/blob/main/Server/GPTmodel.py) file inside the server folder

## Technologies Used
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Frontend
![image](https://github.com/halcyon-past/Vue-Project-With-Dummy-Backend/assets/70253408/cde297c2-f6cd-4d73-ad0c-6a6b7d974dc4)
Created with VUE JS + VITE
- choose a file to upload
- upload the file using the ```upload``` button
- then generate response using the ```generate``` button
- then download the generated responses seperately using ```download``` button under each generated section
- clear everything using the ```clear``` button


## Backend

### Machine Learning Model
I am not making the model but if it is made it can be used in the [GPTmodel.py](https://github.com/halcyon-past/Vue-Project-With-Dummy-Backend/blob/main/Server/GPTmodel.py) file by modifying it

### Flask API

The API is built on FLASK and has 4 endpoints
- ```/upload```
  ```python
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
  ```
  - This end point basically supports the upload feature in the frontend by storing the file uploaded in a path folder which if doesn't exist it creates automatically
  - To add any functionality while uploading the file for easier generation add that to the ```initialize()``` function in the  [GPTmodel.py](https://github.com/halcyon-past/Vue-Project-With-Dummy-Backend/blob/main/Server/GPTmodel.py)

- ```/response```
  ```python
  @app.route("/response", methods=['GET'])
  def get_response():
      return giveResults(path[0])
  ```
  - This generates the Response that needs to be shown in the frontend as well as creates .txt files which can be downloaded by calling the download endpoint
  - To modify anything in this response, modify the ```getResults()``` function in the [GPTmodel.py](https://github.com/halcyon-past/Vue-Project-With-Dummy-Backend/blob/main/Server/GPTmodel.py)
  

- ```/download/<filetype>```
  ```python
  @app.route("/download/<filetype>", methods=['GET'])
  def download_file(filetype):
      if os.path.exists("path\\"+filetype+"_results.txt"):
          return send_file("path\\"+filetype+"_results.txt", mimetype='*/*', as_attachment=True)
      else:
          return 'No Such File Exists'
  ```
  This Returns the generated files for download

- ```/cleardata```
  ```python
  @app.route("/cleardata", methods=['GET'])
  def clear_data():
      shutil.rmtree('path')
      return "Data Cleared"
  ```
  This endpoint deletes the ```path``` folder after all operations has been performed


