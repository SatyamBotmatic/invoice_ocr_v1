import os
from flask import Flask, render_template, request, url_for, redirect

# import our OCR function
from ocr_core import ocr_core
from train_ocr import train_ocr_core

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the home page
@app.route('/')
def home_page():
    return  redirect('/upload')

# route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        templatefile = request.form.get('templatefilename')
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_text = ocr_core(file,templatefile)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

@app.route('/train',methods=['GET','POST'])
def train_page():
    if request.method == 'POST':
        regularex1 = request.form.get('regex1')
        regularex2 = request.form.get('regex2')
        regularex3 = request.form.get('regex3')
        regularex4 = request.form.get('regex4')
        templatename=request.form.get('templatename')
        regularex5=request.form.getlist('regex5[]')
        regularex6=request.form.getlist('regex6[]')



        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('train.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('train.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_train_text = train_ocr_core(file,regularex1,regularex2,regularex3,regularex4,templatename,regularex5,regularex6)

            # extract the text and display it
            return render_template('train.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_train_text,
                                   img_src=UPLOAD_FOLDER + file.filename)

    elif request.method == 'GET':
        return render_template('train.html')


if __name__ == '__main__':
    app.run(debug=True,port=8108)