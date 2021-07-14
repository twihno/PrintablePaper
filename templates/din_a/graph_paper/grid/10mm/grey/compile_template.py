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
    TEMPLATE_SUBDIR = str(dirname).find(
        "/", str(dirname).find("templates/")+10)+1
    PAPERLIB_PATH = str(dirname)[0:TEMPLATE_SUBDIR] + "paperlib.json"

    try:
        with open(PAPERLIB_PATH) as f:
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
            FILENAME = "{}_{}_{}.latex".format(
                parameters["template_name"],
                page_size_name,
                orientation)

            horizonzal_count = int(
                paperlib[page_size][orientation]["width"])-int(
                paperlib[page_size][orientation]["width"] % 10)

            # Remove lines on the page borders
            if horizonzal_count == round(paperlib[page_size][orientation]["width"]):
                horizonzal_count -= 10

            vertical_count = int(
                paperlib[page_size][orientation]["height"])-int(
                paperlib[page_size][orientation]["height"] % 10)

            # Remove lines on the page borders
            if vertical_count == round(paperlib[page_size][orientation]["height"]):
                vertical_count -= 10

            with open(FILENAME, "w") as f:
                f.write(template.render(
                    paperformat=page_size,
                    paperorientation=orientation,
                    horizontal_5mm_count=horizonzal_count,
                    vertical_5mm_count=vertical_count,
                ))
