"""Generates the release notes from the library json files"""

import json
import os

TEMPLATE_DIR = "templates"

if __name__ == "__main__":
    paperlibgroups = []

    for subdir, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if file == "paperlibgroup.json":
                with open(os.path.join(subdir, file), "r") as f:
                    paperlibgroup_dict = json.load(f)
                paperlibgroups.append(
                    [paperlibgroup_dict["group_name"], subdir, paperlibgroup_dict["description"]])

    paperlibgroups.sort()

    with open("./output/README.md", "w") as f:
        f.write("# Included templates\n")

        for lib in paperlibgroups:
            f.write("\n## {}\n{}\n".format(
                lib[0],
                lib[2]
            ))

            for subdir, dirs, files in os.walk(TEMPLATE_DIR):
                for file in files:
                    if file == "printablepaperlib.json":
                        if subdir.startswith(lib[1]):
                            with open(os.path.join(subdir, file), "r") as j:
                                printablepaperlib_dict = json.load(j)
                            f.write(
                                "- {} (v{})\n".format(
                                    printablepaperlib_dict["template_name"],
                                    printablepaperlib_dict["version"]
                                ))