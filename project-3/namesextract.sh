#!/bin/bash

cat actualsorting.py | tail -n +33 | head -n +56 | cut -d"'" -f2 > names.txt
