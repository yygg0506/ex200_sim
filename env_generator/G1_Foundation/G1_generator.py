#!/usr/bin/env python3

from software.dnf_repourl.dnf_repourl import g1_gen_dnf
from network.network_ip.network_ip import g1_gen_network_ip

def g1_gen():
    t1_info = []
    t2_info = []

    network_ip = g1_gen_network_ip()
    t1_info.append(network_ip["t1"])

    dnf = g1_gen_dnf(network_ip["t2"]["server"])

    return {
            "t1_info",
            "t2_info",
            "ip": ip,
            "dnf": dnf,
            }

if __name__ == "__main__":
    result = g1_gen()
    print(result)
