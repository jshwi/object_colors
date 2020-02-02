import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import object_colors  # noqa


project = object_colors.__project__
# noinspection PyShadowingBuiltins
copyright = object_colors.__copyright__
author = object_colors.__author__
release = object_colors.__release__
maintainer = object_colors.__maintainer__
email = object_colors.__email__
version = object_colors.__version__
# noinspection PyShadowingBuiltins
license = object_colors.__license__

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.imgmath',
    'sphinx.ext.doctest'
]

source_suffix = ['.rst']
master_doc = 'index'
exclude_patterns = ['_build']
templates_path = ['_templates']
todo_include_todos = True

pygments_style = 'monokai'
autoclass_content = "both"
autodoc_member_order = 'bysource'
autodoc_default_options = {"members": None}
imgmath_latex_preamble = r'''
\usepackage{xcolor}
\definecolor{offwhite}{rgb}{238,238,238}
\everymath{\color{offwhite}}
\everydisplay{\color{offwhite}}
'''

html_theme = 'graphite'
html_theme_path = ['_themes']
html_static_path = ['_static']
html_logo = '_static/oc.png'
html_favicon = "_static/oc.ico"
html_sidebars = {
    '**': [
        'globaltoc.html',
        'searchbox.html'
    ]
}

# # -- Options for HTML output -------------------------------------------
html_domain_indices = True
html_use_index = True
htmlhelp_basename = "ObjectColorsDoc"
html_show_sourcelink = True
logo = "_static/logo.png"
add_function_parentheses = True
add_module_names = True
html_show_sphinx = False

# # -- Options for LaTeX output ------------------------------------------
latex_elements = {
    "papersize": "",
    "fontpkg": "",
    "fncychap": "",
    "maketitle": "\\cover",
    "pointsize": "",
    "preamble": "",
    "releasename": "",
    "babel": "",
    "printindex": "",
    "fontenc": "",
    "inputenc": "",
    "classoptions": "",
    "utf8extra": "",
}
latex_additional_files = ["mfgan-bw.sty", "mfgan.sty", logo]
latex_documents = [("index", "object-colors.tex", project, author, "manual")]
latex_show_pagerefs = False
latex_domain_indices = False
latex_use_modindex = False
latex_logo = None

# -- Options for Epub output --------------------------------------------------
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_theme = "epub2"
epub_scheme = ""
epub_identifier = ""
epub_uid = ""
epub_cover = (logo, "epub-cover.html")
epub_pre_files = []
epub_post_files = []
epub_exclude_files = [
    "_static/opensearch.xml",
    "_static/doctools.js",
    "_static/jquery.js",
    "_static/searchtools.js",
    "_static/underscore.js",
    "_static/basic.css",
    "search.html",
    "_static/websupport.js",
]
epub_tocdepth = 2
epub_tocdup = False

# -- Options for Mobi output -------------------------------------------
mobi_theme = "mobi"
mobi_title = u"Object Colors"
mobi_author = u"Stephen Whitlock"
mobi_publisher = u"Stephen Whitlock"
mobi_copyright = u"2019, Stephen Whitlock"
mobi_scheme = ""
mobi_identifier = ""
mobi_uid = ""
mobi_cover = "_static/logo.png"
mobi_pre_files = []
mobi_post_files = []
mobi_exclude_files = [
    "_static/opensearch.xml",
    "_static/doctools.js",
    "_static/jquery.js",
    "_static/searchtools.js",
    "_static/underscore.js",
    "_static/basic.css",
    "search.html",
    "_static/websupport.js",
]
mobi_tocdepth = 2
mobi_tocdup = False
mobi_add_visible_links = False

# -- Options for Code Examples output ----------------------------------
code_example_dir = "code-example"
code_add_python_path = ["../py"]

