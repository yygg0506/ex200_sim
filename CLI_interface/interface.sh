#!/bin/bash

printf '%s\n%s\n%s\n%s\n' "Welcome to EX200-sim" "1) Generator" "2) Grader" "3) Record"

read -r -p "Please Choose one option: " ans
case $ans in
	1) echo "Generator"; exit 0;;
	2) echo "Grader"; exit 0;;
	3) echo "Record"; exit 0;;
	*) echo "bad!"; exit 1;;
esac
