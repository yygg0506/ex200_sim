#!/usr/bin/env python3

import randon

def g1_gen_network_ip():
    ip_templates = [
            "192.168.10",
            "172.16.10",
            "10.10.10",
            ]

    prefix = randon.choice(ip_templates)

    start = randon.randonint(10, 200)

    return {
            "node1": f"{prefix}.{start}",
            "node2": f"{prefix}.{start + 1}",
            "server": f"{prefix}.{start + 2}",
            "prefix_length": 24
            }
