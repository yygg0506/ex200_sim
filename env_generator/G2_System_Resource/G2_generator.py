#!/usr/bin/env python3

import random
from identity.identity_group import g2_gen_identity_group
from identity.identity_user import g2_gen_identity_user

import sys
from pathlib import Path
ENV_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENV_DIR))

from lib import general_write

def g2_gen():

    t1_info = {}
    t2_info = {}
    random_num = random.randint(1, 5)


    ## identity ##
    # user / uid
    id_group = {}
    id_user = {}

    id_group = g2_gen_identity_group(random_num)
    id_user = g2_gen_identity_user(random_num, id_group["grp_name_list"])       

    return {
            "id_group": id_group,
            "id_user": id_user,
            }
        #id_result = g2_gen_identity_proc(id_group, id_user)       

        # group / gid / membership
        # password / passwd aging

    ## storage ##
        # disk partion
        # lvm
        # swap

    ## filesystem ##
        # fs type
        # UUID / label
        # persistent mount / fstab

    ## file_resource ##
        # dir / file
        # owner /group
        # permission

    ## resource_policy ##
        # ACL / default ACL
        # umask

# test # 
if __name__ == "__main__":
    result = g2_gen()
    output_path = ENV_DIR / "tmp_file" / "g2_result"
    general_write(output_path, result)
