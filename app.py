from flask import Flask, jsonify, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import subprocess


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = "./data"
app = Flask(__name__)

def allowed_file(filename):
    """
    Checks whether or not the extension name is allowed.

    filename<str>:The name of the image file. 
    """
    return '.' in filename and filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS


@app.route('/predict-image', methods=['GET','POST'])
def upload_file():
    """
    This function routes to a page where a user can upload an image through
    the HTML form or just immediately call the POST request.
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(UPLOAD_FOLDER + "/"+ filename)
           return runModel(UPLOAD_FOLDER + "/" + filename)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

def runModel(filename,cfgFile="cfg/yolov3.cfg yolov3.weights", weightsFile="yolov3.weights"):
    """
    This function runs the darknet detec command on a single image and returns the predicted
    objects as a string.

    filename<str>: the path to the image file.
    cfgFile<str>: the path the configuration file.
    weightsFile<str>.: the path the the weights file of the model.
    """
    t = subprocess.run(["./darknet detect {} {} {}".format(cfgFile,weightsFile,filename)],shell=True,stdout=subprocess.PIPE)
    result = t.stdout.decode('utf-8').strip()
    sepIndex = result.find("Predicted in")
    return result[sepIndex:]

# The following is for running command `python app.py` in local development.
if __name__ == "__main__":
    print("* Starting web server... please wait until server has fully started")
    app.run(host='0.0.0.0', threaded=False)
