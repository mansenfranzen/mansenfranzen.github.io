"""This module converts a jupyter notebook to html"""

import sys
import os

import nbconvert.resources
import nbformat
from nbconvert import HTMLExporter

import config as cfg
import helper

def convert(file_path):
    # get notebook path
    notebook_file = os.path.join(cfg.dir_nb, file_path + ".ipynb")
    print(notebook_file)
    nb = nbformat.reads(open(notebook_file, 'r').read(), as_version=4)

    # load notebook into html
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(nb)

    # Remove ipython builtin bootstrap
    sheet_filename = os.path.join(
        os.path.dirname(nbconvert.resources.__file__), 'style.min.css')

    with open(sheet_filename, encoding='utf-8') as f:
        body = body.replace(f.read(), "")

    # include navbar and header
    read_navbar = open(os.path.join(cfg.dir_tpl, "navbar.txt"), 'r').read()
    read_pre = open(os.path.join(cfg.dir_tpl, "pre_header.txt"), 'r').read()
    read_post = open(os.path.join(cfg.dir_tpl, "post_header.txt"), 'r').read()

    body = body.replace("<body>", "<body>\n" + read_navbar)
    body = body.replace("<head>", "<head>\n" + read_pre)
    body = body.replace("</head>", read_post + "\n</head>")

    # other modifications
    body = body.replace("custom.css", "../../templates/css/custom.css")


    # save notebook
    html_file = file_path + ".html"

    if os.path.basename(file_path) in cfg.pages:
        html_file = os.path.join(cfg.dir_static_pages, html_file)
    else:
        html_file = os.path.join(cfg.dir_static, html_file)

    helper.make_sure_path_exists(html_file)
    html_file_writer = open(html_file, 'w')
    html_file_writer.write(body)
    html_file_writer.close()


if __name__ == "__main__":
    file_path = sys.argv[1]
    convert(file_path)