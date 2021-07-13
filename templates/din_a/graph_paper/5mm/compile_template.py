"""Generate latex files"""

import json
import os
from jinja2 import Environment, FileSystemLoader

if __name__ == "__main__":

    # Change working directory to this directory
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    os.chdir(dirname)

    # Load printablepaperlib parameters
    with open('./printablepaperlib.json') as f:
        parameters = json.load(f)

    # Load paperlib
    template_subdir = str(dirname).find(
        "/", str(dirname).find("templates/")+10)+1
    paperlib_path = str(dirname)[0:template_subdir] + "paperlib.json"

    with open(paperlib_path) as f:
        paperlib = json.load(f)

    # Load template

    env = Environment(loader=FileSystemLoader(dirname))
    template = env.get_template('template.latex_template')

    # printablepaperlib specific code

    for page_size, page_size_name in parameters["page_sizes"]:
        for orientation in parameters["orientations"]:
            #print(page_size, page_size_name, orientation)
            filename = "{}_{}_{}.latex".format(
                parameters["template_name"],
                page_size_name,
                orientation)

            with open(filename, "w") as f:
                f.write(template.render(
                    paperformat=page_size,
                    paperorientation=orientation,
                ))
