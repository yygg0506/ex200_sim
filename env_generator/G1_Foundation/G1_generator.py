#!/usr/bin/env python3

import json
from software.dnf_repourl.dnf_repourl import g1_gen_dnf
from network.network_ip.network_ip import g1_gen_network_ip

def t1_write(info):
    with open("/root/clilab/ex200_sim/env_generator/file/t1_meta", "w") as file:
        json.dump(info, file, indent=4)

def t2_write(mechine, info):
    with open(f"/root/clilab/ex200_sim/env_generator/file/t2_{mechine}", "w") as file:
        json.dump(info, file, indent=4)

def info_proc(t1_info, t2_info, sector, output_file):
    t1_info["sector"] = output_file["t1"]
    for mechine, info in output_file.items():
        t2_info[mechine] = {
                sector: info
                }

def g1_gen():
    t1_info = {}
    t2_info = {}

    ## network_ip ##
    network_ip = g1_gen_network_ip()

    info_proc(t1_info, t2_info, "network_ip", network_ip)

    ## dnf_url ##
    dnf_repo_url = g1_gen_dnf(network_ip["t2"]["server"])
    t1_info["dnf_repo_url"] = dnf_repo_url

    ## info_proc ##
    result = {
            "t1_info": t1_info,
            "t2_info": t2_info,
            "dnf_repo_url": dnf_repo_url,
            }

    t1_write(t1_info)
    for mechine, info in t2_info.items():
        t2_write(mechine, info)

    return result

if __name__ == "__main__":
    result = g1_gen()
    print(result)
