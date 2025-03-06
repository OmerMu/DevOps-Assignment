@echo off
for /F "tokens=1,2 delims==" %%A in (.env) do (
    setx %%A %%B /M
    echo Set %%A=%%B
)
echo ✅ Environment variables loaded system-wide!
