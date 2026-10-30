#!/usr/bin/env python3

import random
import pwd

import sys
from pathlib import Path
ENV_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ENV_DIR))

from lib import User, Group, Passwd

def g2_gen_identity_group(random_num):
    group_name_list = []
    group_id_list = []
    group_list = []

    for _ in range(0,random_num):
        new_group = Group(group_name_list, group_id_list)
        group_list.append(new_group)
    return group_list

def g2_gen_identity_user(random_num, group_list):
    user_name_list = []
    user_id_list = []
    user_list = []
    
    for _ in range(random_num):
        passwd = Passwd() #get Passwd()
        user = User(user_name_list, user_id_list, group_list, passwd)
        user_list.append(user)

    return user_list

def g2_gen_identity(random_num):
    group_list = g2_gen_identity_group(random_num)
    user_list = g2_gen_identity_user(random_num, group_list)

    return {
            "group_list": group_list, 
            "user_list": user_list,
            }

# test
if __name__ == "__main__":
    group_name_list = []
    group_id_list = []
    group_list = []
    for _ in range(5):
        group = Group(group_name_list, group_id_list)
        group_list.append(group)

    passwd = Passwd()

    result = g2_gen_identity_user(1, group_list, passwd)
    print(result)
