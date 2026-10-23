#!/usr/bin/env python3

import random
import pwd

def g2_gen_identity_user(random_num):
    random_num = 1

    ## (random_num) -> loop -> user_detial() -> return [dict]user_profile ##
    user_profile = {
            "t1": [],
            }
    uid_list = []
    name_list = []
    name_prefix_list = [ "rhel", "test", "exam", "user", "enpolyee" ]
    shell_list = [ "/bin/bash", "/usr/bin/nologgin", ]
    

    # user_detial: -> user_profile["t1"][dict]
    def user_detail(uid_list, name_list, shell_list, name_prefix_list):
        # uid: [>1000, ramdon]
        while True:
            uid = random.randint(1000, 2500)
            if uid in uid_list:
                continue
            try: 
                pwd.getpwuid(uid)
                continue
            except KeyError:
                break
        uid_list.append(uid)
               
        # user_name: [name_prefix]+[user_name_num]
        while True:
            user_name_prefix = random.choice(name_prefix_list)
            user_name_num = random.randint(1, 1000)
            user_name = f"{user_name_prefix}-{user_name_num}"
            if user_name in name_list:
                continue
            try: 
                pwd.getpwname(user_name)
                continue
            except KeyError:
                break
        name_list.append(user_name)

        # group: [main] "[support]"

        # shell: '/bin/bash' or '/usr/bin/nologgin'
        # home_dir: [random path]
        # password / aging: [not_sure]

    for i in range(0, random_num):
        user_profile["t1"].append(user_detail(uid_list, name_list, shell_list, name_prefix_list))

    return user_profile
