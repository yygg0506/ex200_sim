#!/usr/bin/env python3

import sys
import grp
import random

from pathlib import Path
ENV_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ENV_DIR))

from lib import general_write

def g2_gen_identity_group(random_num):
    ## (random_num) -> loop -> group_detail() -> return [dict]group_profile
    
    gid_list = []
    grp_name_list = []
    name_prefix = [
            "test", "exam", "rhel", "ops", "dev"
            ]
    group_profile = []

    # group_detail() -> group_profile["t1"][dict]
    def group_detail(gid_list, prefix, grp_name_list):

    # GID: [>1000]
        while True:
            gid = random.randint(1000, 2000) 
            if gid in gid_list:
                continue
            try:
                grp.getgrgid(gid)
                continue
            except KeyError:
                break

        gid_list.append(gid)

    # group_name: [name_prefix]+[number]
        while True:
            name_prefix = random.choice(prefix)
            grp_name_num = random.randint(0, 100)
            group_name = f"{name_prefix}-{grp_name_num}" 
            if group_name in grp_name_list:
                continue
            try:
                grp.getgrnam(group_name)
                continue
            except KeyError:
                break
            
        grp_name_list.append(group_name)

        return {
                "gid": gid,
                "group_name": group_name,
                }

    for i in range(0, random_num):
        group_profile.append(group_detail(gid_list, name_prefix, grp_name_list))

    return group_profile

# test #
if __name__ == "__main__":
    result = g2_gen_identity_group(5)
    output_path = ENV_DIR / "G2_System_Resource" / "tmp_file" / "result"
    general_write(output_path, result)
