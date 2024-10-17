from flask import Flask, request, redirect, url_for ,render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('fileupload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form action="" method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''
    
if __name__ == '__main__':
    app.run(debug=True)