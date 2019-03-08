#!/bin/bash
setupATLAS
lsetup "root 6.02.05-x86_64-slc6-gcc48-opt"
local_python
python promptleptonveto.py
