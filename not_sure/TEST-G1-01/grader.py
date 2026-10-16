#!/usr/bin/env python3

import subprocess

expected_urls = [
        "http://192.168.100.10/BaseOS",
        "http://192.168.100.10/AppStream",
]

repos = []
result = subprocess.run(
        ["dnf", "repolist", "--enabled", "-q"],
        capture_output=True,
        text=True
)

if result.returncode != 0:
    raise RuntimeError(result.stderr)

for repo_id in result.stdout.splitlines()[1:]:

    repo_id = repo_id.split()[0]

    info = subprocess.run(
            ["dnf", "repo", "info", repo_id],
            capture_output=True,
            text=True
    )
    
    if info.returncode != 0:
        continue

    for line in info.stdout.splitlines():
        if line.strip().startswith("Base URL"):
            url = line.split(":", 1)[1].strip()

            repos.append({
                "id": repo_id,
                "url": url
                })

            break

for expected_url in expected_urls:

    matched = False

    for repo in repos:

        if repo["url"].rstrip("/") == expected_url.rstrip("/"):
            print(f"[PASS] {expected_url} ({repo['id']})")
            matched = True
            break
    if not matched:
        print(f"[FAIL] {expected_url}")

