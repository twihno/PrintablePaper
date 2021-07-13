""""Generates the latex files, the pdfs and cleans the directories"""

import os
import shutil

TEMPLATE_DIR = 'templates'
RM_EXTENSIONS = ['.aux', '.latex', '.log', '.pdf']


def clean_templates():
    """Clean the templates directory"""
    for subdir, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in RM_EXTENSIONS:
                os.remove(os.path.join(subdir, file))


def generate_latex_files():
    """Generates the latex files from the latex_template templates"""
    for subdir, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if file == "compile_template.py":
                os.system("python3 \"" + os.path.join(subdir, file) + "\"")


def generate_pdf_files():
    """Generates the pdf files from the latex files"""
    last_subdir = ""

    for subdir, dirs, files in os.walk(TEMPLATE_DIR):
        #print("PATH", subdir, files, dirs)
        #print("SUBDIR0", os.path.abspath(subdir))
        for file in files:
            #print("SUBDIR1", os.path.abspath(subdir))
            ext = os.path.splitext(file)[-1].lower()
            if ext == '.latex':
                if(last_subdir != subdir):
                    last_subdir = subdir
                    os.chdir(os.path.abspath(subdir))
                #print("SUBDIR2", os.path.abspath(subdir))
                for i in range(0, 2):
                    os.system("xelatex \"" +
                              str(file) + "\"")
                    #print("xelatex \"" +
                    #str(file) + "\"")


def move_pdf_files():
    """Moves the generated pdf files to output"""
    for subdir, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext == '.pdf':
                src = os.path.abspath(os.path.join(subdir, file))
                dest = str(os.path.abspath(subdir)).replace(
                    "templates", "output")
                print("src: " + src)
                print("dest: " + dest)
                shutil.copy(src, dest)


if __name__ == "__main__":
    topleveldir = os.getcwd()

    print("Cleaning templates folder")
    clean_templates()

    print("Generating latex files")
    generate_latex_files()

    os.chdir(topleveldir)
    print("Generating pdf files")
    generate_pdf_files()

    os.chdir(topleveldir)
    print("Moving pdf files")
    move_pdf_files()

    print("Cleaning templates folder")
    clean_templates()
