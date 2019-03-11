#!/usr/bin/env bash

mkdir Result Unsorted

if [[ -z "$(ls -A Unsorted)" ]]; then
    echo "No images in the Unsorted folder!"
else
    docker run -it -v $(pwd)/Result:/Result -v $(pwd)/Unsorted:/Unsorted imagesorter
fi 
