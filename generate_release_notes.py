"""Generates the release notes from the library json files"""

import json
import os
from datetime import date

TEMPLATE_DIR = "templates"

if __name__ == "__main__":
    # Load paperlibgroups
    paperlibgroups = []

    for subdir, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if file == "paperlibgroup.json":
                with open(os.path.join(subdir, file), "r") as f:
                    paperlibgroup_dict = json.load(f)
                paperlibgroups.append(
                    [paperlibgroup_dict["group_name"], subdir, paperlibgroup_dict["description"]])

    paperlibgroups.sort()

    # Load paperlibcategories
    paperlibcategories = []

    for subdir, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if file == "paperlibcategory.json":
                with open(os.path.join(subdir, file), "r") as f:
                    paperlibcategories_dict = json.load(f)
                paperlibcategories.append(
                    [paperlibcategories_dict["category_name"],
                     subdir,
                     paperlibcategories_dict["description"]])

    paperlibcategories.sort()

    with open("./output/README.md", "w") as f:
        f.write("Version {}\n\n---\n\n".format(date.today().strftime("%Y-%m-%d")))
        f.write("# Included templates\n")

        for lib in paperlibgroups:
            f.write("\n## {}\n{}\n".format(
                lib[0],
                lib[2]
            ))

            for cat in paperlibcategories:
                if not(cat[1].startswith(lib[1]+"/")):
                    break

                f.write("\n### {}\n{}\n\n".format(
                    cat[0],
                    cat[2]
                ))

                for subdir, dirs, files in os.walk(TEMPLATE_DIR):
                    print(subdir, dirs, files)
                    for file in files:
                        if file == "printablepaperlib.json":
                            if subdir.startswith(lib[1]+"/") and subdir.startswith(cat[1]+"/"):
                                print(subdir)
                                with open(os.path.join(subdir, file), "r") as j:
                                    printablepaperlib_dict = json.load(j)
                                f.write(
                                    "- {} (v{})\n".format(
                                        printablepaperlib_dict["template_name"].replace(
                                            "_", "\\_"),
                                        printablepaperlib_dict["version"]
                                    ))
