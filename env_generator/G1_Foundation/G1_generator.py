#!/usr/bin/env python3

from software.dnf_repourl.dnf_repourl import g1_gen_dnf
from network.network_ip.network_ip import g1_gen_network_ip

def g1_gen():
    network_ip = g1_gen_network_ip()
    t1_network_ip_prefix = network_ip["ip_prefix"]

    for ip in network_ip:

        dnf = g1_gen_dnf(ip)

    return {
            "ip": ip,
            "dnf": dnf,
            }

if __name__ == "__main__":
    result = g1_gen()
    print(result)
