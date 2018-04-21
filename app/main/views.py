# coding: utf-8

from . import main
from flask import render_template
from flask import redirect
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import os


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/upload', methods=['POST'])                    # 很成功呀， 很棒.
def upload_file():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_dir = os.path.join(base_dir, 'upload')
    f = request.files['upload_file']

    f.save(os.path.join(file_dir, f.filename))
    return render_template('upload_results.html')


@main.route('/history')
def history_files():
    return render_template('history.html')




