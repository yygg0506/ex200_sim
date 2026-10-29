#!/usr/bin/env python3

import random
import pwd

import sys
from pathlib import Path
ENV_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ENV_DIR))

from lib import User, Group

def g2_gen_identity_user(random_num, group_list):
    user_name_list = []
    user_id_list = []
    user_list = []
    
    for _ in range(random_num):
        user = User(user_name_list, user_id_list, group_list)
        user_list.append(user)

    return user_list

# test
if __name__ == "__main__":
    group_name_list = []
    group_id_list = []
    group_list = []
    for _ in range(5):
        group = Group(group_name_list, group_id_list)
        group_list.append(group)

    print(group_list)

    g2_gen_identity_user(group_list)
