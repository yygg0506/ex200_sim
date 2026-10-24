#!/usr/bin/env python3

import json

with open("user_result", "r") as file:
    data = json.load(file)

user_profile = data[0]
class User:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

user = User(1000, "test")
print(user)
print(user.uid)
print(user.name)
print(type(user))
