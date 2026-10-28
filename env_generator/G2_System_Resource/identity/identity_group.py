#!/usr/bin/env python3
import sys
from pathlib import Path
ENV_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ENV_DIR))

import grp
import random
from lib import Group, general_write

def g2_gen_identity_group(random_num):
    group_name_list = []
    group_id_list = []
    group_list = []

    for _ in range(0,random_num):
        new_group = Group(group_name_list, group_id_list)
        group_list.append(new_group)
    print(group_list)

# test #
if __name__ == "__main__":
    result = g2_gen_identity_group(5)
    output_path = ENV_DIR / "G2_System_Resource" / "tmp_file" / "group_result"
    general_write(output_path, result)
