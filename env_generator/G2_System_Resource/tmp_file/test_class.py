#!/usr/bin/env python3

import json
import random
import grp

with open("user_result", "r") as file:
    user_data = json.load(file)
with open("group_result", "r") as file:
    group_data = json.load(file)

# Group
grp_name_list = []
gid_list = []
group_info_list = []

class Group:
    def __init__(self, gid_list, grp_name_list):
        name_prefix = ["test", "exam", "rhel", "ops", "dev"]
        self.gen_group_name(name_prefix, grp_name_list)
        self.gen_group_id(gid_list)

    # group_name
    def gen_group_name(self, name_prefix, grp_name_list):
        while True:
            group_name_prefix = random.choice(name_prefix)
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
    def gen_group_id(self, gid_list):
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
        self.id = group_id

    def __repr__(self):
        return f"Group(id={self.id}, name={self.name})"

for i in range(5):
    group = Group(gid_list, grp_name_list)
    group_info_list.append(group)
    
print(group_info_list)
