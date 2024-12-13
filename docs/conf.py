""" Configuration file for the Sphinx documentation builder. """

# -- Gestion des fichiers à ajouter ------------------------------------------

import os
import shutil
import sys

# Ajout du chemin vers le dossier palm_tracer
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath("../mon_module"))

# -- Project information -----------------------------------------------------

project = "Python CI with monitoring Template"
copyright = "2024, Thibaut Monseigne"
author = "Thibaut Monseigne"
language = "fr"

# -- General configuration ---------------------------------------------------

extensions = [
		"sphinx.ext.autodoc",
		"sphinx.ext.autosummary",
		"sphinx.ext.autosectionlabel",
		"sphinx.ext.napoleon",
		"sphinx.ext.todo",
		"sphinx.ext.viewcode",
		"sphinxcontrib.jquery",
		]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

# Autoriser l'inclusion de contenu HTML brut
html_context = {"allow_html_in_rst": True}

# -- Automatisation ----------------------------------------------------------

autosummary_generate = True
autodoc_default_options = {
		"members":          True,
		"undoc-members":    True,
		"show-inheritance": True,
		}
autodoc_member_order = "bysource"

todo_include_todos = True

suppress_warnings = ["autosectionlabel.*"]
