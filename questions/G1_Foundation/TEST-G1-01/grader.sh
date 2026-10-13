#!/bin/bash

repo_id="$1"
excepted_url="$2"

actual_url=$(
    dnf repo info "$repo_id" 2>/dev/null |
        awk '/Base Url/ {
            sub(/^[^:]*:[[:space:]]*/, "")
            print
            exit
        }'
    )

if [[ "${actual_url%/}" == "${excepted_url%/}" ]]; then
    echo "[PASS] Repository URL"
else
    echo "[FAIL] repository URL"
    echo "Expected: $expected_url"
    echo "Actual: $actual_url"
fi

if dnf --disablerepo='*' --enablerepo="$repo_id" --refresh makecache > /dev/null 2>&1 ;then
    echo "[PASS] Repository fuctional"
else
    echo "[FAIL] repository fuctional"
fi
