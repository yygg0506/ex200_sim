#!/usr/bin/env python3

import json
from software.dnf_repourl.dnf_repourl import g1_gen_dnf
from network.network_ip.network_ip import g1_gen_network_ip

def g1_gen():
    t1_info = {}
    t2_info = {}

    network_ip = g1_gen_network_ip()
    t1_info["network"] = network_ip["t1"]
    t2_info["network"] = network_ip["t2"]

    dnf = g1_gen_dnf(network_ip["t2"]["server"])

    result = {
            "t1_info": t1_info,
            "t2_info": t2_info,
            "dnf": dnf,
            }

    with open("test.json", "w") as file:
        json.dump(result, file, indent=4)

    return result

if __name__ == "__main__":
    result = g1_gen()
    print(result)
