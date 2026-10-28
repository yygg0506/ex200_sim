#!/usr/bin/env python3

import random
import pwd

class User:
    def __init__(self, user_name_list, user_id_list, group_list):
        self.gen_user_name(user_name_list)
        self.gen_user_id(user_id_list)

    #user_name -> [prefix] + [number]
    def gen_user_name(self, user_name_list):
        user_name_prefix_list = [ "rhel", "test", "exam", "user", "employee" ]
        user_name_prefix = random.choice(user_name_prefix_list)
        user_name_num = random.randint(1,100)
        user_name = f"{user_name_prefix}-{user_name_num}"

        if user_name in user_name_list:
            continue
        try:
            pwd.getpwnam(user_name)
            continue
        except KeyError:
            break

        User.name = user_name
        user_name_list.append(user_name)

    #user_id -> [1000-2000]
    def gen_user_id(self, user_id_list)
        user_id = random.randint(1000,2000)
        
        if user_id in user_id_list:
            continue
        try:
            pwd.getpwpid(user_id)
            continue
        except KeyError:
            break

        User.id = user_id
        user_id_list.append(user_id)

    #shell
    def gen_user_shell(self):
        shell_list = [ "/bin/bash", "/usr/sbin/nologin", ]
        shell = random.choice(shell_list)

    #user's group
    def gen_user_group(self, group_list):
        group_supp = random.choice(group_list).name
        group_primary = self.name

    #home_dir

    def __repr__(self):
