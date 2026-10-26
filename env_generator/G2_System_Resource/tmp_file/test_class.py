#!/usr/bin/env python3

import json
import random
import grp

with open("user_result", "r") as file:
    data = json.load(file)

# Group
grp_name_list = []
gid_list = []

class Group:
    name_prefix = ["test", "exam", "rhel", "ops", "dev"]
    group_id = random.randint(1,1000)

    def __init__(self, gid_list, grp_name_list):

    # group_name
    def gen_group_name(self):
        while True:
            group_name_prefix = name_prefix.choice()
            group_name_num = random.randint(1,100)
            group_name = f"{group_name_prefix}-{group_name_num}"

            if group_name in grp_name_list:
                continue
            try:
                grp.getgrnam(group_name)
                continue
            except KeyError:
                break

        grp_name_list.append(group_name)
        self.name = group_name


    # group_id
    def gen_group_id(self):
        while True:
            group_id = random.randint(1,1000)
            
            if group_id in gid_list:
                continue
            try:
                grp.getgrgid(group_id)
                continue
            except KeyError:
                break

        gid_list.append(group_id)
        self.id = group.id

