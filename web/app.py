"""
Author: Ilse den Brok
Date: 11 June 2020
Function: calls the html templates and handles the file
"""

from flask import Flask, render_template, request
from werkzeug import secure_filename
from web import search_db

app = Flask(__name__)


@app.route("/", endpoint='func1')
def func1():
    """
    the first page you see
    :return: the template for our home page
    """
    return render_template('home.html')


@app.route("/results", endpoint='func2')
def func2():
    """
    the results page of our application
    :return: the template for our results page
    """
    return render_template('results.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    """
    handles the upload- and send file button
    :return:
    """
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        search_db.main()
    return 'file uploaded successfully'


#if __name__ == "__main__":
    #app.run()
    # return render_template('results.html')
