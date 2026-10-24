#!/usr/bin/env python3

import json

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

users = {}
for i in data:
    users[i["user_name"]] = User(i["uid"], i["user_name"], i["shell"], i["home_dir"])

for i in users:
    users[i].show_info()
