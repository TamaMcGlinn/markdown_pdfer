#!/usr/bin/env python3
""" Turns markdown into an html page and a pdf """

import os
import tempfile
import pathlib
import glob
import shutil
import subprocess

import markdown

markdown_files = ['document.md']
output_pdf = pathlib.Path('document.pdf')
output_html = output_pdf.with_suffix('.html')

# List of supported extensions here: https://python-markdown.github.io/extensions/
markdown_extensions = ['tables',
                       'fenced_code',
                       'footnotes',
                       'codehilite']
markdown_input = ''
for filename in markdown_files:
    with open(filename, 'r') as f:
        markdown_input += f.read()

with open('html/html_prefix.html', 'r') as html_preamble:
    content = markdown.markdown(markdown_input, output_format='html5', extensions=markdown_extensions)
    html_text = html_preamble.read() + content

with open('html/html_postfix.html', 'r') as html_preamble:
    html_text += html_preamble.read()

with open(output_html, 'w') as html_file:
    html_file.write(html_text)

dirs_to_copy = ['images', 'css', 'html']
for dir_to_copy in dirs_to_copy:
    dst_dir = os.path.join(tempfile.gettempdir(), dir_to_copy)
    pathlib.Path(dst_dir).mkdir(parents=True, exist_ok=True)
    for image in glob.iglob(os.path.join(dir_to_copy, "*")):
        shutil.copy(image, dst_dir)

subprocess.run(['wkhtmltopdf', '--enable-local-file-access', 'document.html', 'document.pdf'])

