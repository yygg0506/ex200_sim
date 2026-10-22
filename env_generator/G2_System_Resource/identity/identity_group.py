#!/usr/bin/env python3

import grp

def g2_gen_identity_group(random_num):
    ## (random_num) -> loop -> group_detail() -> return [dict]group_profile
    
    group_profile = {
            "t1": [],
            }

    # group_detail() -> group_profile["t1"][dict]
    def group_detail(gid_list):
        
        gid_list = []

        for gid in gid_list:
            if grp.getgrgid(gid):
                continue

        gid =  # GID: [>1000]
        group_name = # group_name: [name_prefix]+[number]

        return {
                "gid": gid,
                "group_name": group_name,
                }

    for i in range(0, random_num):
        group_profile["t1"].append(group_detail(gid_list))

