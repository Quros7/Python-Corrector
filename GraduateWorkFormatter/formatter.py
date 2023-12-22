from docx import Document
import os
from app import app

from GraduateWorkFormatter import main_req_formatter
from GraduateWorkFormatter import source_links_formatter
import argparse

def Edit(inp_path, inp_filename):
    # parser = argparse.ArgumentParser()
    # parser.add_argument('path_to_docx', type=str, help='Path to docx file')
    # args = parser.parse_args()
    args = inp_path

    if not os.path.exists(args) or not os.path.isfile(args):
        print('Введен неверный путь до файла')
        exit(1)

    try:
        doc = Document(args)
    except ValueError:
        print('Документ должен быть типа docx')
        exit(1)

    main_req_formatter.MainRequirementsFormatter.format_document(doc)
    main_req_formatter.MainRequirementsFormatter.change_title_page_year(doc, '2023')
    source_links_formatter.SourceLinksFormatter.check_for_links_presence(doc)
    
    n_name = "edited_" + inp_filename
    n_path = os.path.join(app.config['UPLOAD_FOLDER'], n_name)
    doc.save(n_path)


#if __name__ == '__main__':
#    main()
