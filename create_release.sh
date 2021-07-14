#!/bin/bash

print_return_value () {
    if test $1 -eq 0; then
        echo -e "\n  ✅ \e[32m\e[1mDONE\e[0m"
    else
        echo -e "\n  ❌ \e[31m\e[1mFAILED\e[0m"
        exit 1
    fi
}

# Checking/generating build name
echo -e "\n\e[32m\e[1m*** Checking/generating build name ***\e[0m"

# Get build_name
build_name=$1

if [ -z ${build_name} ]; then
    build_name="dev$(date +'%Y-%m-%d-%H:%M')"
    echo -e "\nGenerated build_name: $build_name"
    echo -e "\n  ✅ \e[32m\e[1mGENERATED BUILD NAME\e[0m"
else
    echo -e "\nFound build_name: $build_name"
    echo -e "\n  ✅ \e[32m\e[1mBUILD NAME FOUND\e[0m"
fi

# Create pdf files
echo -e "\n\e[32m\e[1m*** Run build.sh ***\e[0m"
./build.sh
build_return=$?
echo "--------------------"
echo "⬆ Run build.sh"
print_return_value $build_return

# Create release notes
echo -e "\n\e[32m\e[1m*** Create release notes ***\e[0m"
python3 ./generate_release_notes.py
print_return_value $?

# Create zip file
echo -e "\n\e[32m\e[1m*** Create zip file ***\e[0m"
cd output
zipname="PrintablePaper_$build_name.zip"
zipname="${zipname//$'/'/'_'}" # Remove / from zipname
zip -r $zipname *
print_return_value $?

# Move zip file
echo -e "\n\e[32m\e[1m*** Move zip file ***\e[0m"
mv "$zipname" ..
print_return_value $?
echo "Current path: $PWD"
echo "File: $zipname"
cd ..
echo "New path: $PWD"
