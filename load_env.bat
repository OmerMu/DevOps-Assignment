@echo off
for /F "tokens=1,2 delims==" %%A in (.env) do (
    set %%A=%%B
    echo Setting %%A=%%B
)
