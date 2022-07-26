#!/bin/bash

for (( i = 0; i < 29; i++ )); do
    if [[ i -eq 19 ]]; then
        touch 19-copy_list.py
    else
        touch $i-answer.txt
    fi
done
