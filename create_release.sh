#!/bin/bash

print_return_value () {
    if test $1 -eq 0; then
        echo -e "\n  ✅ \e[32m\e[1mDONE\e[0m"
    else
        echo -e "\n  ❌ \e[31m\e[1mFAILED\e[0m"
        exit 1
    fi
}

# Create pdf files
echo -e "\n\e[32m\e[1m*** Run build.sh ***\e[0m"
./build.sh
echo "--------------------"
print_return_value $?

# Create release notes
echo -e "\n\e[32m\e[1m*** Create release notes ***\e[0m"
python3 ./generate_release_notes.py
print_return_value $?

# Create zip file
echo -e "\n\e[32m\e[1m*** Create zip file ***\e[0m"
zipname="PrintablePaper_$1.zip"
cd output
zip -r $zipname *
mv $zipname ..
cd ..
print_return_value $?