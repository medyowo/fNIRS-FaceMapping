@echo off
setlocal enabledelayedexpansion

for /R %%f in (*.TXT) do (
	set str=%%f
	Echo.%%f | FIND /I "experience">Nul && (Echo.%%f) | FIND /I "temoin">Nul && (set str=!str:temoin=experience!)

	for %%N in ("!str!") do set txtname=%%~nxN
	echo "Modifying %%f to "!txtname!"
	ren "%%f" "!txtname!"
)

for /R %%c in (*.csv) do (
	set str2=%%c
	Echo.%%c | FIND /I "experience">Nul && (Echo.%%c) | FIND /I "temoin">Nul && (set str2=!str2:temoin=experience!)
	
	for %%M in ("!str2!") do set name=%%~nxM
	echo "Modifying %%c to "!name!"
	ren "%%c" "!name!"
)
pause