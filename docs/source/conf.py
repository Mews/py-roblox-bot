#Tell sphinx and rtd where to find source code
import sys, pathlib
sys.path.append((pathlib.Path(__file__).parent.parent.parent / "src").resolve().as_posix())

#from pyrobloxbot import literals

#autodoc_type_aliases = {
  #'KEYBOARD_KEYS': literals.KEYBOARD_KEYS,
  #'WALK_DIRECTIONS': literals.WALK_DIRECTIONS
#}
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
autodoc_mock_imports = ["pydirectinput", "win32gui", "pygetwindow"]
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx_rtd_theme", "sphinx.ext.autosummary"]
pygments_style = "sphinx"
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
