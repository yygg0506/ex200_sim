#!/usr/bin/env python3

import random
import pwd

class User:
    def __init__(self, user_name_list, user_id_list, group_list, passwd):
        self.gen_user_name(user_name_list)
        self.gen_user_id(user_id_list)
        self.gen_user_shell()
        self.gen_user_home_dir()
        self.gen_user_group(group_list)
        self.gen_passwd(passwd)

    #user_name -> [prefix] + [number]
    def gen_user_name(self, user_name_list):
        user_name_prefix_list = [ "rhel", "test", "exam", "user", "employee" ]

        while True:
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

        self.name = user_name
        user_name_list.append(user_name)

    #user_id -> [1000-2000]
    def gen_user_id(self, user_id_list):
        
        while True:
            user_id = random.randint(1000,2000)
            if user_id in user_id_list:
                continue
            try:
                pwd.getpwuid(user_id)
                continue
            except KeyError:
                break

        self.id = user_id
        user_id_list.append(user_id)

    #shell
    def gen_user_shell(self):
        shell_list = [ "/bin/bash", "/usr/sbin/nologin", ]
        shell = random.choice(shell_list)
        self.shell = shell

    #user's group
    def gen_user_group(self, group_list):
        group_supp = random.choice(group_list)
        group_primary = self.name
        group = {
                "group_primary": group_primary,
                "group_supp": group_supp.name,
                }
        self.group = group

    #home_dir
    def gen_user_home_dir(self):
        home_dir = f"/home/{self.name}"
        self.home_dir = home_dir

    #passwd
    def gen_passwd(self, passwd):
        self.passwd = passwd

    #to_dict
    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "shell": self.shell,
                "group": self.group,
                "home_dir": self.home_dir,
                "passwd": self.passwd.to_dict(),
                }

    def __repr__(self):
        return f"User({self.to_dict()!r})"

