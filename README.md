<div align="center">

<img src="https://raw.githubusercontent.com/twihno/PrintablePaper/main/branding/logo.svg" alt="PrintablePaper" width="500"/>


[![Release](https://img.shields.io/github/v/release/twihno/PrintablePaper)](https://github.com/twihno/PrintablePaper/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/twihno/PrintablePaper/blob/main/LICENSE)
[![Compile](https://github.com/twihno/PrintablePaper/actions/workflows/compile.yml/badge.svg?branch=main)](https://github.com/twihno/PrintablePaper/actions/workflows/compile.yml)
[![Last Commit](https://img.shields.io/github/last-commit/twihno/PrintablePaper)](https://github.com/twihno/PrintablePaper/commits)
[![Open Issues](https://img.shields.io/github/issues-raw/twihno/PrintablePaper)](https://github.com/twihno/PrintablePaper/issues)

---

<div align="center">

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/twihno/PrintablePaper)

</div>


</div>

## About this project
The goal of this project is to deliver high quality and free to use print templates for various page sizes.

To achieve this goal it uses LaTex (XeLaTex) and Jinja2 which results in standard pdf files.

The pdf files are auto-generated and [released]((https://github.com/twihno/PrintablePaper/releases)) on GitHub.

## Contributing

Thank you for your interest! Everyone is invited to add their own templates or improve existing templates.

The code was developed and tested on Ubuntu.
It should run on every Linux distribution with XeLaTex and Python 3 support.

### Project structure

```
..
├ various files and folders (self-explaining or described below)
└ templates
  └ groups (by paper size, e.g. DIN A)
    ├ paperlibgroup.json (metadata)
    └ categories (by template category, e.g. graph paper or lined paper)
      ├ paperlibcategory.json (metadata)
      └ template
        └ template_variations (optional)
          └ template_color_variations (optional)
            ├ compile_template.py
            ├ printablepaperlib.json
            └ template.latex_template
```

Every template needs its own folder and three files:

- ```compile_template.py``` (this file generates the different latex files for the various page sizes)
- ```printablepaperlib.json``` (this file contains the name, the version and the supported paper sizes and orientations of the template)
- ```template.latex_template``` (this file contains the the latex (jinja template) file used to generate the pdf files)

When implementing a new template you can reference ```templates/din_a/graph_paper/5mm```

New templates are automatically picked up by the build process.

## Build scripts

### ```build.sh```
- (re)creates the output directory
- creates the paper libraries (paperlib.json) which includes the measurements of all available paper formats
- creates the pdf files by calling ```generate_pdf.py```

### ```create_release.sh```
- calls ```build.sh```
- creates the release notes/README file
- bundles the pdf files in a zip archive

### GitHub Actions
- used to compile and build the releases
