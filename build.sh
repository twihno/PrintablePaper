#!/bin/bash

echo "Creating paperlib.json"
./create_din_a_paper_lib.py

cat templates/paperlib.json
