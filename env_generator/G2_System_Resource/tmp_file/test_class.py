#!/usr/bin/env python3

import json

with open("user_result", "r") as file:
    data = json.load(file)

for i in data:
    print(i)
    print(type(i))
print(type(data))
