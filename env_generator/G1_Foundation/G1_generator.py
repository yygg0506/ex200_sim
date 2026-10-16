#!/usr/bin/env python3

from dnf.dnf_repourl.dnf_repourl import G1_gen_dnf

def g1_gen():
    ip = "192.168.100.10"

    dnf = g1_gen_dnf(ip)

    return {
            "ip": ip,
            "dnf": dnf,
            }

if __name__ == "__main__":
    result = g1_gen()
    print(result)
