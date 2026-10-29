#!/usr/bin/env python3

import random

class Passwd:
    def __init__(self):
        self.gen_passwd()

    def gen_passwd(self):
        #min/max_change
        passwd_min = random.randint(1,10)
        passwd_max = random.randint(11,30)

        self.min = passwd_min
        self.max = passwd_max

        #warn_days
        passwd_warn = random.randint(1,10)
        self.warn = passwd_warn

        #inactive_days
        passwd_inac = random.randint(1,10)
        self.inac = passwd_inac

        #expire_date
        passwd_exp = random.randint(1,10)
        self.exp = passwd_exp

    def to_dict(self):
        return {
                "min": self.min,
                "max": self.max,
                "warn": self.warn,
                "inactive": self.inac,
                "expire": self.exp,
                }

    def __repr__(self):
        return f"{self.to_dict}"
# test
if __name__ == "__main__":
    result = Passwd()
    print(result)
