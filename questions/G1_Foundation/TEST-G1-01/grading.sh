#!/bin/bash

target="/srv/examdata"

[[ -d "$target" ]] || exit 1

owner=$(stat -c '%u' "$target")
group=$(stat -c '%g' "$target")
permission=$(stat -c '%a' "$target")

[[ "$owner" == "0" ]] || exit 1
[[ "$group" == "0" ]] || exit 1
[[ "$permission" == "755" ]] || exit 1

exit 0
