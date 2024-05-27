from docx import Document
import os
from app import app

from GraduateWorkFormatter import main_req_formatter
from GraduateWorkFormatter import source_links_formatter
import argparse


def Edit(inp_path, inp_filename):
    args = inp_path

    if not os.path.exists(args) or not os.path.isfile(args):
        print('Введен неверный путь до файла')
        exit(1)

    try:
        doc = Document(args)
    except ValueError:
        print('Документ должен быть одного из типов: txt, doc, docx, docm')
        exit(1)

    changes =[]
    
    main_req_formatter.MainRequirementsFormatter.change_title_page_year(doc, '2024', changes)
    source_links_formatter.SourceLinksFormatter.check_for_links_presence(doc, changes)
    main_req_formatter.MainRequirementsFormatter.format_document(doc, changes)
    
    n_name = "edited_" + inp_filename
    n_path = os.path.join(app.config['UPLOAD_FOLDER'], n_name)
    doc.save(n_path)
    
    log_path = os.path.join(app.config['UPLOAD_FOLDER'], "changelog_" + n_name + ".txt")
    changes_file = open(log_path, "w+")
    for item in changes:
        changes_file.write("%s\n" % item)
    changes_file.close()
