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

for i in data:
    i["user_name"] = User(i["uid"], i["user_name"], i["shell"], i["home_dir"])

    print(i["user_name"])
    print(i["user_name"].uid)
    print(i["user_name"].name)
    print(i["user_name"].shell)
    print(i["user_name"].home_dir)
    print(type(i["user_name"]))
