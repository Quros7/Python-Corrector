# -*- coding: utf-8 -*- 
#import sys
#sys.path.append("../GraduateWorkFormatter")
from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from app import app
#from app import GraduateWorkFormatter
import os
from GraduateWorkFormatter import formatter
#from formatter import Edit

# UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads')
# os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', extentions=app.config['ALLOWED_EXTENSIONS'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Here you should save the file
        # file.save(path_to_save_file)
        # РАБОТАЕТ file.save(os.path.join(app.instance_path, 'uploads', filename))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        flash('Файл ({}) был успешно загружен на сервер'.format(filename))
        # formatter(file_path) не работает
        # exec("python test");
        formatter.Edit(file_path, filename);
        flash('Файл ({}) был успешно отредактирован'.format(filename))
        return redirect(url_for('index'))
    
    flash('Ошибка при загрузке файла ({})'.format(filename))
    return redirect(url_for('index'))