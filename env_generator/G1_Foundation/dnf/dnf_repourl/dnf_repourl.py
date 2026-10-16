#!/usr/bin/env python3

def g1_gen_dnf(ip):
    baseos = f"http://{ip}/BaseOS"
    appstream = f"http://{ip}AppStream"

    return {
            "base_url": baseos,
            "appstream": appstream
            }
