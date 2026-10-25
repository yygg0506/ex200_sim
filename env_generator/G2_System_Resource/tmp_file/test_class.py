#!/usr/bin/env python3

import json
import random
import grp

with open("user_result", "r") as file:
    data = json.load(file)

class User:
    def __init__(self, uid, name, shell, home_dir):
        self.uid = uid
        self.name = name
        self.shell = shell
        self.home_dir = home_dir

    def show_info(self):
        print(f"=== start ===\n{self.uid}\n{self.name}\n{self.shell}\n{self.home_dir}\n=== end ===\n")

class Group:
    name_prefix = ["test", "exam", "rhel", "ops", "dev"]
        
    # group_detail() -> group_profile[list]
    def group_detail(self, gid_list, grp_name_list):

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
        self.gid = gid

    # group_name: [name_prefix]+[number]
        while True:
            name_prefix = random.choice(name_prefix)
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
        self.grp_name = grp_name

    def __init__(self, gid_list, grp_name_list):
        self.group_detail(self, gid_list, grp_name_list)

users = {}
for i in data:
    users[i["user_name"]] = User(i["uid"], i["user_name"], i["shell"], i["home_dir"])

for i in users:
    users[i].show_info()

gid_list = []
grp_name_list = []

group = Group(gid_list, grp_name_list)
print(group.gid)
print(group.grp_name)
