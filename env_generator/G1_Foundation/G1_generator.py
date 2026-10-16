#!/usr/bin/env python3

from dnf.dnf_repourl.dnf_repourl import generate_dnf

def generator_g1():
    ip = "192.168.100.10"

    dnf = generator_dnf(ip)

    return {
            "ip": ip,
            "dnf": dnf,
            }

if __name__ == "__main__":
    result = generate_g1()
    print(result)
