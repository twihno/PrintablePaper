#!/bin/bash

echo "current directory"
ls -la

echo "Creating paperlib.json"
python3 ./create_din_a_paper_lib.py

cat templates/paperlib.json
