"""Generate latex files"""

import json
import os
import traceback
import sys
from jinja2 import Environment, FileSystemLoader

if __name__ == "__main__":

    # Change working directory to this directory
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    os.chdir(dirname)

    # Load printablepaperlib parameters
    try:
        with open('./printablepaperlib.json') as f:
            parameters = json.load(f)
    except FileNotFoundError:
        traceback.print_exc()
        sys.exit(1)

    # Load paperlib
    template_subdir = str(dirname).find(
        "/", str(dirname).find("templates/")+10)+1
    paperlib_path = str(dirname)[0:template_subdir] + "paperlib.json"

    try:
        with open(paperlib_path) as f:
            paperlib = json.load(f)
    except FileNotFoundError:
        traceback.print_exc()
        sys.exit(1)

    # Load template

    env = Environment(loader=FileSystemLoader(dirname))
    template = env.get_template('template.latex_template')

    # printablepaperlib specific code

    for page_size in parameters["page_sizes"]:
        page_size_name = paperlib[page_size]["displayname"]
        for orientation in parameters["orientations"]:
            filename = "{}_{}_{}.latex".format(
                parameters["template_name"],
                page_size_name,
                orientation)

            with open(filename, "w") as f:
                f.write(template.render(
                    paperformat = page_size,
                    paperorientation = orientation,
                    horizontal_5mm_count = round(paperlib[page_size][orientation]["width"]),
                    vertical_5mm_count = round(paperlib[page_size][orientation]["height"]),
                ))
