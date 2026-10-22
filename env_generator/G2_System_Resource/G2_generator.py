#!/usr/bin/env python3

import random

def g2_gen():

    t1_info = {}
    t2_info = {}
    random_num = random.randint(1, 5)


    ## identity ##
        # user / uid
        id_group = {}
        id_user = {}

        id_group = g2_gen_identity_group(random_num)
        id_user = g2_gen_identity_user(random_num)       
        g2_gen_identity_proc(id_group, id_user)       

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
