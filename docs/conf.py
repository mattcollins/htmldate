# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

import htmldate


# -- Project information -----------------------------------------------------

project = 'htmldate'
copyright = '2022, <a href="https://adrien.barbaresi.eu/">Adrien Barbaresi</a>'
author = 'Adrien Barbaresi'

# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
version = htmldate.__version__
# The full version, including alpha/beta/rc tags.
release = htmldate.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = None

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode']
#'sphinx.ext.autosummary', 
#autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "show_powered_by": False,
    "github_user": "adbar",
    "github_repo": "htmldate",
    "github_banner": True,
    "show_related": False,
    "analytics_id": "G-5BS735G6BB",
#    "note_bg": "#FFF59C",
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


intersphinx_mapping = {
#    "datetime": ("https://docs.python.org/3/library/datetime.html", None), # objects.inv
    "python": ("https://docs.python.org/3/", None),
}
