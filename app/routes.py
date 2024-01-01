# -*- coding: utf-8 -*- 
from flask import render_template, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from app import app
import os
import time
#from app import GraduateWorkFormatter
from GraduateWorkFormatter import formatter

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
        timetemp = str(time.time()).split(".")
        coded_filename = timetemp[0]+timetemp[1]+"$"+filename
        # Here we save the file with coded name
        # file.save(path_to_save_file)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], coded_filename)
        file.save(file_path)
        flash('Файл ({}) был успешно загружен на сервер'.format(filename))
        formatter.Edit(file_path, coded_filename);
        flash('Файл ({}) был успешно отредактирован'.format(filename))
        ed_filename = "edited_" + filename
        return render_template('download.html', coded_name="edited_"+coded_filename, name=ed_filename, title='Download')
    
    flash('Ошибка при загрузке файла ({})'.format(filename))
    return redirect(url_for('index'))

@app.route('/download/<name>+<coded_name>')
def download_file(name, coded_name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], coded_name, download_name=name, as_attachment=True)