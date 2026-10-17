#!/usr/bin/env python3

import random

def g1_gen_network_ip():
    ip_templates = [
            "192.168.10",
            "172.16.10",
            "10.10.10",
            ]

    prefix = random.choice(ip_templates)

    start = random.randint(10, 200)

    return {
            "t1" = {
                "ip_prefix": f"{prefix}",
                "prefix_length": 24,
            }
            "node1": f"{prefix}.{start}",
            "node2": f"{prefix}.{start + 1}",
            "server": f"{prefix}.{start + 2}",
            }
