#!/usr/bin/env python3

import json

with open("user_result", "r") as file:
    data = json.load(file)

user_profile = data[0]
class User:
    pass
user = User()
print(user)
print(type(user))
print(data[1])
print(type(data))
print(user_profile)
print(type(user_profile))
