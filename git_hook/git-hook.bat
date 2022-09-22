set "FILE=%cd%\.git\hooks\prepare-commit-msg"
set "GIT_CODE=%cd%\git_hook\git_hook_code"

if exist %FILE% (
    echo "%FILE% has already existed."
)
else (
    type %GIT_CODE% >> %FILE%
    echo "Git Hook is created succesfully!"
)
