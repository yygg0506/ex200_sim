#!/usr/bin/env python3

from pathlib import Path
import sys
import json

ENV_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENV_DIR))

from lib import t1_info_proc, t2_info_proc, t1_write, t2_write
from software.dnf_repourl.dnf_repourl import g1_gen_dnf
from network import g1_gen_network_ip, g1_gen_network_hostname

def g1_gen():
    t1_info = {}
    t2_info = {}

    ## network_ip ##
    network_ip = g1_gen_network_ip()
    t1_info_proc(t1_info, "network_ip", network_ip)
    t2_info_proc(t2_info, "network_ip", network_ip)

    network_hostname = g1_gen_network_hostname()
    t2_info_proc(t2_info, "network_hostname", network_hostname)

    ## dnf_url ##
    dnf_repo_url = g1_gen_dnf(t2_info["server"]["network_ip"])
    t1_info_proc(t1_info, "dnf_repourl", dnf_repo_url)

    ## info_proc ##
    result = {
            "t1_info": t1_info,
            "t2_info": t2_info,
            }

    t1_write(t1_info)
    for mechine, info in t2_info.items():
        t2_write(mechine, info)
    with open(f"/root/clilab/ex200_sim/env_generator/file/t2_info", "w") as file:
        json.dump(t2_info, file, indent=4)

    return result

# test #
if __name__ == "__main__":
    result = g1_gen()
    print(result)
