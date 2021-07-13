#!/bin/bash

if [ -d "output" ]
    then
        echo "*** Removing existing output dir ***"
        rm -rf output
        echo "  ✔ done"
fi

echo "*** Creating output dir ***"
mkdir output
rsync -av -f"+ */" -f"- *" "templates/" "output"
echo "  ✔ done"

echo ""
echo "*** Creating metric paperlib.json ***"
#python3 ./templates/metric/create_din_a_paper_lib.py
echo "  ✔ done"

echo ""
echo "*** Generating pdfs ***"
python3 ./generate_pdf.py
echo "  ✔ done"
