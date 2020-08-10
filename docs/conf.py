import os
import sys
sys.path.insert(0, os.path.abspath('..'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

html_theme_options = {
    'nosidebar': True
}
# The name of the entry point, without the ".rst" extension.
# By convention this will be "index"
master_doc = "index"
# This values are all used in the generated documentation.
# Usually, the release and version are the same,
# but sometimes we want to have the release have an "rc" tag.
project = "PreferredPictures"
copyright = "2020, PreferredPictures"
author = "Preferred Pictures <contact@preferred.pictures>"
version = release = "0.3"
