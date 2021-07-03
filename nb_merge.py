#https://gist.github.com/fperez/e2bbc0a208e82e450f69

#!/usr/bin/env python
# Note, updated version of
# https://github.com/ipython/ipython-in-depth/blob/master/tools/nbmerge.py
"""
usage:
python nbmerge.py A.ipynb B.ipynb C.ipynb > merged.ipynb
"""

import io
import os
import sys

from IPython import nbformat

def merge_notebooks(filenames):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            # TODO: add an optional marker between joined notebooks
            # like an horizontal rule, for example, or some other arbitrary
            # (user specified) markdown cell)
            merged.cells.extend(nb.cells)
    if not hasattr(merged.metadata, 'name'):
        merged.metadata.name = ''
    merged.metadata.name += "_merged"
    print(nbformat.writes(merged))

if __name__ == '__main__':
    notebooks = sys.argv[1:]
    if not notebooks:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    merge_notebooks(notebooks)

#extend notebooks
#https://github.com/jupyter/nbformat/issues/176
nb = nbf.read('eda_new.ipynb', as_version=4)
text = """\
# Manual EDA with automatic notebook genration"""

code = """\
%pylab inline
hist(normal(size=2000), bins=50);"""

cells = [nbf.v4.new_markdown_cell(text), nbf.v4.new_code_cell(code)]
nb['cells'].extend(cells)

nbf.write(nb, 'eda_new.ipynb')



def merge_notebooks(filenames):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            # TODO: add an optional marker between joined notebooks
            # like an horizontal rule, for example, or some other arbitrary
            # (user specified) markdown cell)
            text = """\
            # End of file """+str(fname)
            new_cells = [nbf.v4.new_markdown_cell(text)]
            merged.cells.extend(new_cells)
            merged.cells.extend(nb.cells)
    if not hasattr(merged.metadata, 'name'):
        merged.metadata.name = ''
    merged.metadata.name += "_merged"
    print(nbformat.writes(merged))
