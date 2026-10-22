#!/usr/bin/env python3

import grp
import random

def g2_gen_identity_group(random_num):
    ## (random_num) -> loop -> group_detail() -> return [dict]group_profile
    
    gid_list = []
    grp_num = random.randint(0, 100)
    name_prefix = [
            "test", "exam", "rhel", "ops", "dev"
            ]
    group_profile = {
            "t1": [],
            }

    # group_detail() -> group_profile["t1"][dict]
    def group_detail(gid_list, prefix, grp_num):

    # GID: [>1000]
        while True:
            gid = random.randint(1000, 2000) 
            if old_gid in gid_list:
                continue
            if grp.getgrgid(old_gid):
                continue
            break

    # group_name: [name_prefix]+[number]
        name_prefix = random.choice(prefix)
        group_name = f"{name_prefix}-{grp_num}" 

        gid_list.append(gid)

        return {
                "gid": gid,
                "group_name": group_name,
                }

    for i in range(0, random_num):
        group_profile["t1"].append(group_detail(gid_list, name_prefix, grp_num))

