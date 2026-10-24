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

users = {}
for i in data:
    users[i["user_name"]] = User(i["uid"], i["user_name"], i["shell"], i["home_dir"])
    
print(users)
