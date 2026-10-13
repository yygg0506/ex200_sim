#!/bin/bash

expected_url="$1"

G1_01_check_ans(){
    if [[ "${actual_url%/}" == "${excepted_url%/}" ]]; then
        return 0
    else
        return 1
    fi

    if dnf --disablerepo='*' --enablerepo="$repo_id" --refresh makecache > /dev/null 2>&1 ;then
        return 0
    else
        return 2
    fi
}

G1_01_echo(){
    local result="$1"

    if [[ "$result" -eq 0 ]]; then
        echo "[PASS] Repository URL"
    else
        echo "[FAIL] repository URL"
        echo "Expected: $expected_url"
        echo "Actual: $actual_url"
    fi

    if [[ "$result" -eq 0 ]]; then
        echo "[PASS] Repository fuctional"
    else
        echo "[FAIL] repository fuctional"
    fi
}

while read -r repo_id; do
    actual_url=$(
        dnf repo info "$repo_id" 2>/dev/null |
            awk '/Base URL/ {
                sub(/^[^:]*:[[:space:]]*/, "")
                print
                exit
            }'
        )
done < <(
    dnf repolist --enabled -q|
        awk 'NR > 1 {print $1}'
    )

