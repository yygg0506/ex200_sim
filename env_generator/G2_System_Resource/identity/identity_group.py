#!/usr/bin/env python3

import grp
import random

def g2_gen_identity_group(random_num):
    ## (random_num) -> loop -> group_detail() -> return [dict]group_profile
    
    gid_list = []
    grp_num = random.randind(0, 100)
    name_prefix = [
            "test", "exam", "rhel", "ops", "dev"
            ]
    group_profile = {
            "t1": [],
            }

    # group_detail() -> group_profile["t1"][dict]
    def group_detail(gid_list, name_prefix, grp_num + 1):
        

        for gid in gid_list:
            if grp.getgrgid(gid):
                continue

        gid = random.randint(1000, 2000) # GID: [>1000]
        group_name = name_prefix - grp_num # group_name: [name_prefix]+[number]

        gid_list.append(gid, name_prefix)

        return {
                "gid": gid,
                "group_name": group_name,
                }

    for i in range(0, random_num):
        group_profile["t1"].append(group_detail(gid_list, name_prefix, grp_num))

