#!/usr/bin/env python3

import subprocess

expected_urls = [
        "http://192.168.100.10/BaseOS",
        "http://192.168.100.10/AppStream",
        ]

dnf_target_info = []

dnf_repolist = subprocess.run(
        ["dnf", "repolist", "--enabled", "-q"],
        capture_output = True,
        text = True
        )

if dnf_repolist.returncode != 0:
    raise RuntimeError(dnf_repolist.stderr)

for dnf_repoid in dnf_repolist.stdout.splitlines()[1:]:
    
    dnf_repoid = dnf_repoid.split()[0]

    dnf_repoinfo = subprocess.run(
            ["dnf", "repo", "info", dnf_repoid],
            capture_output = True,
            text = True,
            )

    for dnf_repoinfo_line in dnf_repoinfo.stdout.splitlines():
        if dnf_repoinfo_line.strip().startswith("Base URL"):
            dnf_url = dnf_repoinfo_line.split(":", 1)[1].strip()

            dnf_target_info.append({
                "id": dnf_repoid,
                "url": dnf_url,
                })

            break

for expected_url in expected_urls:

    matched = False

    for target_info in dnf_target_info:
        if expected_url.rstrip("/") == target_info["url"].rstrip("/"):
            print(f"[PASS] {expected_url} {target_info['id']}")
            matched = True
            break
    if not matched:
        print(f"[FAIL] {expected_url}")

