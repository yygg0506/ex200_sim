#!/usr/bin/env python3
# general import
import random
import sys
from pathlib import Path
ENV_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENV_DIR))

# from lib
from identity.identity_group import g2_gen_identity_group
from identity.identity_user import g2_gen_identity_user
from lib import general_write

def g2_gen():

    t1_info = {}
    t2_info = {}
    random_num = random.randint(1, 10)


    ## identity ##
    # user / uid
    # group / gid / membership
    id_user = {}

    id_group_list = g2_gen_identity_group(random_num)
    id_group_dict_list = []
    for i in id_group_list:
        id_group_dict_list.append(i.to_dict())

    print(f"id_group_list=\n\t{id_group_list},\nid_group_dict_list=\n\t{id_group_dict_list}")
    return id_group_dict_list

    id_user = g2_gen_identity_user(random_num, id_group_list)       

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
