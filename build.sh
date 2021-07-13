#!/bin/bash

print_return_value () {
    if test $1 -eq 0; then
        echo -e "\n  ✅ \e[32m\e[1mDONE\e[0m"
    else
        echo -e "\n  ❌ \e[31m\e[1mFAILED\e[0m"
        exit 1
    fi
}

if [ -d "output" ]
    then
        echo -e "\n\e[32m\e[1m*** Removing existing output dir ***\e[0m"
        rm -rf output
        print_return_value $?
fi

echo -e "\n\e[32m\e[1m*** Creating output dir ***\e[0m"
mkdir output
rsync -av -f"+ */" -f"- *" "templates/" "output"
print_return_value $?

echo -e "\n\e[32m\e[1m*** Creating metric paperlib.json ***\e[0m"
python3 ./templates/din_a/create_din_a_paper_lib.py
print_return_value $?

echo -e "\n\e[32m\e[1m*** Generating pdfs ***\e[0m"
python3 ./generate_pdf.py
print_return_value $?
