#!/usr/bin/env python3
# general import
import random
import sys
from pathlib import Path
ENV_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENV_DIR))

# from lib
from identity.identity_user import g2_gen_identity
from lib import general_write

def g2_gen():

    t1_info = {}
    t2_info = {}
    random_num = 2


## identity ##
    id_list = g2_gen_identity(random_num)
    # group / gid / membership
    group_list = id_list["group_list"]
    group_dict_list = []
    for i in group_list:
        group_dict_list.append(i.to_dict())

    # user / uid
    user_list = id_list["user_list"]    
    user_dict_list = []
    for i in user_list:
        user_dict_list.append(i.to_dict())

    return {
            "group": group_dict_list,
            "user": user_dict_list
            }


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
    output_path = ENV_DIR / "G2_System_Resource" / "tmp_file" / "g2_result"
    general_write(output_path, result)
