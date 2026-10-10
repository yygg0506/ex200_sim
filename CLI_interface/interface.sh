#!/bin/bash

printf '%s\n%s\n%s\n' "Welcome to EX200-sim" "1) test1" "2) test2"

read -p "Please Choose one option: " ans
case $ans in
	1) echo "test1"; exit 0;;
	2) echo "test2"; exit 0;;
	*) echo "bad!"; exit 1;;
esac
