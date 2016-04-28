import sys

sys.path.insert(0, '../')

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.viewcode',
              'sphinx.ext.autosummary', 'sphinx.ext.intersphinx']
templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'

project = 'tdns'
copyright = '2016, Gavin M. Roy'

import tdns
release = tdns.__version__
version = '.'.join(release.split('.')[0:1])
exclude_patterns = ['_build']
pygments_style = 'sphinx'

intersphinx_mapping = {'tornado': ('http://www.tornadoweb.org/en/stable/', None),
                       'pycares': ('http://pycares.readthedocs.io/en/stable/', None),
                       'python': ('https://docs.python.org/3/', None)}

html_static_path = ['_static']
#autodoc_member_order = 'bysource'
