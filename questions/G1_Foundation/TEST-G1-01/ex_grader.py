#!/usr/bin/env python3

import subprocess

expected_urls = [
        "http://192.168.100.10/BaseOS",
        "http://192.168.100.10/AppStream",
        ]

dnf_target_info = ()

dnf_repolist = subprocess.run(
        ["dnf", "repolist", "--enabled", "-q"],
        capture_output = True,
        text = True,
        )

for dnf_repoid in dnf_repolist.stdout.splitlines()[1:]:
    dnf_repoid = dnf_repoid.split()[0]

    dnf_repoinfo = subprocess.run(
            ["dnf", "repo", "info", dnf_repoid],
            capture_output = True,
            text = True,
            ]

    for dnf_repoinfo_line in dnf_repoinfo:
        if dnf_repoinfo_line.startswith("Base URL"):
            dnf_url = dnf_repoinfo_line.split(":", 1)[1]

        dnf_target_info.append({
            "id": dnf_repoid,
            "url": dnf_url,
            })

        break

for expected_url in expected_urls:

    result = False

    for target_info in dnf_target_info:
        if expected_url.rsplit("/") == target_info["url"].rsplit("/"):
            print(f"[PASS] {expected_url} {target_info['id']}")
            result = True

    if not result:
        print(f"[FAIL] {expected_url}")
