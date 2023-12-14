# -*- coding: utf-8 -*- 
from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from app import app
import os

# UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads')
os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)
ALLOWED_EXTENSIONS = {'txt', 'doc', 'docx', 'docm'}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Here you should save the file
        # file.save(path_to_save_file)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) не работает
        file.save(os.path.join(app.instance_path, 'uploads', filename))
        flash('Файл ({}) был успешно загружен на сервер'.format(filename))
        # flash(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    
    flash('Ошибка при загрузке файла ({})'.format(filename))
    return redirect(url_for('index'))