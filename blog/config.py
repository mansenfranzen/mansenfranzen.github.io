"""This module contains config properties"""

import os

root = os.path.dirname(__file__)

dir_nb = os.path.join(root, "notebooks")
dir_pages = os.path.join(root, "pages")
dir_static = os.path.join(root, "static")
dir_static_nb = os.path.join(dir_static, "notebooks")
dir_static_pages = os.path.join(dir_static, "pages")
dir_tpl = os.path.join(root, "templates")

dir_css = os.path.join(dir_tpl, "css")
dir_js = os.path.join(dir_tpl, "js")

pages = ["Blog"]