#!/bin/bash
FILE=./.git/hooks/prepare-commit-msg
GIT_CODE=./git_hook_code

if test -f "$FILE"; then
    echo "$FILE has already existed."
else
    cat $GIT_CODE >> $FILE
    echo "Git Hook is created."
fi

chmod +x $FILE
