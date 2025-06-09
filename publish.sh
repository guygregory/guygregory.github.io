#!/bin/bash
pelican content -s publishconf.py

if [ ! -f docs/CNAME ]; then
    echo "pedanticjournal.com" > docs/CNAME
fi