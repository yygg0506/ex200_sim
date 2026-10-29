#!/usr/bin/env python3

import random
import pwd

import sys
from pathlib import Path
ENV_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ENV_DIR))

from lib import User

def g2_gen_identity_user(group_list):
    user_name_list = []
    user_id_list = []
    result = User(user_name_list, user_id_list, group_list)

    print(result)
