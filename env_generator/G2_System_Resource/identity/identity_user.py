#!/usr/bin/env python3

def g2_gen_identity_user(input_num):
    # (input_num) -> user_profile(num) -> user_detial()
    # user_detial: ( looping ) -> user_profile["t1"][dict]
        # uid: [>1000, ramdon]
        # group: [main] "[support]"
        # name: [name_prefix]+[number]
        # shell: '/bin/bash' or '/usr/bin/nologgin'
        # home_dir: [random path]
        # password / aging: [not_sure]
