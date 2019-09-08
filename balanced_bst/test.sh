#!/bin/bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "${DIR}"/test_balanced_bst.py
