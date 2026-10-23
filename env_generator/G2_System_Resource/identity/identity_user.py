#!/usr/bin/env python3

import random
import pwd

import sys
from pathlib import Path
ENV_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ENV_DIR))

from lib import general_write

def g2_gen_identity_user(random_num, grp_name_list):
    ## (random_num) -> loop -> user_detial() -> return [dict]user_profile ##
    user_profile = []
    uid_list = []
    usr_name_list = []
    name_prefix_list = [ "rhel", "test", "exam", "user", "employee" ]
    

    # user_detial: -> user_profile[list]
    def user_detail(uid_list, name_list, name_prefix_list):
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
                pwd.getpwnam(user_name)
                continue
            except KeyError:
                break
        name_list.append(user_name)

        # shell: '/bin/bash' or '/usr/sbin/nologin'
        shell_list = [ "/bin/bash", "/usr/sbin/nologin", ]
        shell = random.choice(shell_list)

        # home_dir: [random path]
        home_dir = f"/home/{user_name}"

        # group: [primery] [supply]
        grp_primery = user_name
        grp_supply = random.choice(grp_name_list)
        group = {
                "primery": grp_primery,
                "supply": grp_supply,
                }

        return {
                "user_name": user_name,
                "uid": uid,
                "shell": shell,
                "home_dir": home_dir,
                "group": group,
                }



    for i in range(0, random_num):
        user_profile.append(user_detail(uid_list, usr_name_list, name_prefix_list))

    # output #
    return {
            "user_profile": user_profile,
            "usr_name_list": usr_name_list,
            }

# test # 
if __name__ == "__main__":
    result = g2_gen_identity_user(5)
    output_path = ENV_DIR / "G2_System_Resource" / "tmp_file" / "user_result"
    general_write(output_path, result)
