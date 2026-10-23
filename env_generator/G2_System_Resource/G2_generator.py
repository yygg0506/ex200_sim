#!/usr/bin/env python3

import random
from identity.identity_group import g2_gen_identity_group

def g2_gen():

    t1_info = {}
    t2_info = {}
    random_num = random.randint(1, 5)


    ## identity ##
    # user / uid
    id_group = {}
    id_user = {}

    id_group = g2_gen_identity_group(random_num)
    id_user = g2_gen_identity_user(random_num, id_group)       

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
result = g2_gen()
print(result)
