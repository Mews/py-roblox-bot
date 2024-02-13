from src.pyrobloxbot.literals import KEYBOARD_KEYS, WALK_DIRECTIONS

autodoc_type_aliases = {
  'KEYBOARD_KEYS': KEYBOARD_KEYS,
  'WALK_DIRECTIONS': WALK_DIRECTIONS
}
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme
project = 'pyrobloxbot'
copyright = '2024, Mews'
author = 'Mews'
release = '1.0.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx_rtd_theme"]
pygments_style = "sphinx"
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
