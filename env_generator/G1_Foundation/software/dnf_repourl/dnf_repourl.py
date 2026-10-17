#!/usr/bin/env python3

def g1_gen_dnf(ip):
    baseos = f"http://{ip}/BaseOS"
    appstream = f"http://{ip}/AppStream"

    return {
            "t1": {
                "baseos_url": baseos,
                "appstream_url": appstream
                }
            }
