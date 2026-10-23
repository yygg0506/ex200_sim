#!/usr/bin/env python3

import random

def g2_gen_identity_user(random_num):
    random_num = 1

    ## (random_num) -> loop -> user_detial() -> return [dict]user_profile ##
    user_profile = {
            "t1": [],
            }
    uid_list = []
    name_list = []
    shell_list = [
            "/bin/bash", "/usr/bin/nologgin", 
            ]
    

    # user_detial: -> user_profile["t1"][dict]
    def user_detail(uid_list, name_list, shell_list):
        # uid: [>1000, ramdon]
        while True:
            uid = random.randint(1000, 2500)
            if uid in uid_list:
                continue
            #try: #[not_sure]
               
        # user_name: [name_prefix]+[user_name_num]
        user_name_prefix = [
                "rhel", "test", "exam", "user", "enpolyee"
                ]
        user_name_num = random.randint(1, 1000)
        while True:
            user_name = f"{user_name_prefix}-{user_name_num}"
            if user_name in user_list:
                continue
            #try: #[not_sure]

        # group: [main] "[support]"

        # shell: '/bin/bash' or '/usr/bin/nologgin'
        # home_dir: [random path]
        # password / aging: [not_sure]

    for i in range(1, random_num):
        user_profile["t1"].append(user_detail(uid_list, name_list, shell_list))

    return user_profile
