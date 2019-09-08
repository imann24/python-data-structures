#!/bin/bash

title=$1
title_length=${#title}

function print_spacer() {
    printf "*%.0s" $(seq 1 "$title_length")
    echo
}

print_spacer
print_spacer
echo "$title"
print_spacer
print_spacer
