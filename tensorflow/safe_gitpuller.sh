#!/bin/bash

# Gitpuller can prevent a user pod from starting if it encounters an error. This wrapper
#   sends any errors to a status document and continues without blocking pod startup.

# Check if we have exactly 3 arguments
if [ $# -ne 3 ]; then
    echo "Usage: $0 <repository> <branch> <folder>"
    exit 1
fi

# Define the error file
ERROR_FILE="/home/jovyan/GITPULLER_ERROR_$3.txt"

# Clean up the error file if it exists
rm -f "$ERROR_FILE"

# Run gitpuller and capture output and exit status
if OUTPUT=$(gitpuller "$1" "$2" "$3" 2>&1); then
    # Command succeeded - no op
    :
else
    # Command failed - write timestamp and error message
    echo "$(date): gitpuller failed to sync" > "$ERROR_FILE"
    echo "$OUTPUT" >> "$ERROR_FILE"
fi