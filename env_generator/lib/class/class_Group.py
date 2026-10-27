#!/usr/bin/env python3

import random
import grp

class Group:
    # Group -> (group_name[str], group_id[str])
    def __init__(self, group_name_list, group_id_list):
        self.gen_group_name(group_name_list)
        self.gen_group_id(group_id_list)

    # grop_name -> Group.name([name_prefix]-[name_num])
    def gen_group_name(self, group_name_list):
        group_name_prefix_list = ["test", "rhel", "exam", "ops", "dev"]
        while True:
            group_name_num = random.randint(1,100)
            group_name_prefix = random.choice(group_name_prefix_list)
            group_name = f"{group_name_prefix}-{group_name_id}"

            if group_name in group_name_list:
                continue
            try:
                gre.getgrnme(group_name)
                continue
            except KeyError:
                break
        self.name = group_name
        group_name_list.append(group_name)

    # group_id -> Group_id(1000-2000)
    def gen_group_id(self):
        while True:
            group_id = random.randint(1000, 2000)

            if group_id in group_id__list:
                continue
            try:
                grp.getgrgid(group_id)
                continue
            except KeyError:
                break
        self.id = group_id
        group_id_list = group_id

    def __repr__(self):
        return f"{Group(id={group_id},name={group_name})"
