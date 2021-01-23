# Yet another document standard?

Not really; markdown_pdfer uses existing standards, markdown, git, html and css
and puts them together to achieve the best document collaboration tool known to me. 

The only weakness currently would be the need to learn git for version control. However,
there is no simpler system that achieves the full functionality necessary for
simultaneous editing of files and seamless merging of the end result. So the bottom line is
that programmers can start using markdown_pdfer immediately, and everyone else should learn
to use git and will then be perfectly comfortable using markdown_pdfer.

# Why not LaTeX / Word / plain txt?

LaTeX is too complex to install and to write content in, and does
not properly achieve the separation of styling from content. Word / LibreOffice
documents usually suffer from the same problem and additionally their binary format makes 
it impossible to merge changes.

For instance, if one person edits the styling of a document, while another adds
a paragraph at the end, and yet another changes every paragraph of the existing content,
all at the same time, and then all these changes need to be merged together, this
is a nightmare in LaTeX / Word or any other desktop publishing software.

With markdown_pdfer, this will just work out of the box, as will reverting,
rebasing, octopus merges, and even Continuous Integration to check for typos,
grammar mistakes, or broken internet links.

# High level goals:

- Easy to use
- Easy to merge changes
- Separate style from content
- Offload as much as possible of the work to existing systems

# How?

[Markdown](https://www.markdownguide.org/getting-started/) is a very simple format.
Also, programmers are already used to it 
as the standard way of writing readme files on programming projects. Seeing how 
markdown, with its unobtrusive syntax still generates a fine frontpage for 
programming projects, and git tracks
changes in these files and allows all versioning operations you could wish for,
markdown_pdfer takes that one small step further by integrating wkhtmltopdf
to get to a general purpose document generator that can use the 
markdown/git combination that is so well suited to collaboration on documents.

# Prerequisites

You need [the markdown python package:](https://pypi.org/project/Markdown/#description)

```
pip3 install markdown
```

And you must install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html).

On linux:

```
sudo apt install wkhtmltopdf
```

On windows, run the installer and then put `C:\Program Files\wkhtmltopdf\bin` in your PATH environment variable.

# Make a pdf

Running `./build.py` will build both an html and pdf version of document.md.
Make your content edits as needed to document.md.
If you need/want more files, edit build.py at the top, expanding the list of markdown files to look at, e.g.:

```
markdown_files = ['chapter1.md, chapter2.md, chapter3.md']
```

If you need footnotes in multiple places, I advise you to generate separate pdfs
and concatenate them. Currently, you would need to make major edits to build.py
to do that.

# Styling

Styling is done with CSS; you can edit styles.css to change any styling you want.
This repository comes with a set of defaults so that you can include code listings,
tables, images and footnotes. If you examine the intermediate html file
to see the classes and structure and know how to customize the document using CSS,
anything is possible.

# Share your document

Just clone this repository and then make subsequent edits to whatever you need to edit,
including `html_postfix.html`, `html_prefix.html`, `styles.css` and even `build.py`.

Please give your new repository a new name,
especially if you use github to collaborate on the document,
and please don't use the 'fork' button on github, unless you
want to contribute back to this project itself rather than
create a document.

```
git clone git@github.com:TamaMcGlinn/markdown_pdfer document_name
cd document_name
git remote remove origin
vim document.md
./build.py
```

