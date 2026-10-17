#!/usr/bin/env python3

from software.dnf_repourl.dnf_repourl import g1_gen_dnf
from network.network_ip.network_ip import g1_gen_network_ip

def g1_gen():
    ip = g1_gen_network_ip()

    dnf = g1_gen_dnf(ip)

    return {
            "ip": ip,
            "dnf": dnf,
            }

if __name__ == "__main__":
    result = g1_gen()
    print(result)
