# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import json


project = "Project"
copyright = "2023"
author = "RMT"
release = "0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
exclude_patterns = [".git", ".venv", "build/modules", "**/.venv"]
#include_patterns = ["**/doc"]


# mermaid config - @see https://pypi.org/project/sphinxcontrib-mermaid/
extensions.append("sphinxcontrib.mermaid")

# sphinx_needs
extensions.append("sphinx_needs")

# sphinxcontrib-test-reports
extensions.append("sphinxcontrib.test_reports")
tr_report_template = "doc/test_report_template.txt"

# The suffix of source filenames.
source_suffix = [".rst"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    source[0] = rendered


def setup(app):
    app.connect("source-read", rstjinja)


with open('build/Flv1/Sys1/docs/config.json', 'r') as file:
    html_context = json.load(file)
