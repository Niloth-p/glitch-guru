# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "GlitchGuruDocs"
copyright = "2023, Niloth"
author = "Niloth"
release = "1.0.0"

sys.path.insert(0, os.path.abspath("../.."))
os.environ["DJANGO_SETTINGS_MODULE"] = "GlitchGuru.settings"
import django
django.setup()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
                'sphinx.ext.autodoc',
                'sphinx.ext.coverage',
                'sphinx.ext.viewcode',
                'sphinx.ext.todo',
                'sphinx.ext.autosummary',
                'sphinx.ext.autosectionlabel',
                'sphinx_last_updated_by_git',
                'notfound.extension',
                'sphinx-prompt',
                'sphinx_favicon',
                'sphinx.ext.napoleon',
                'sphinx_toolbox.shields',
              ]

templates_path = ["_templates"]
exclude_patterns = ['**/migrations/*']
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = '_static/Wmf-ico-48px.png'
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = [
    'css/custom.css',
]
html_js_files = [
]

github_username = 'Niloth-p'
github_repository = 'glitch-guru'
