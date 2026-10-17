#!/usr/bin/env python3


def t1_info_proc(t1_info, sector, output_file):
    t1_info[sector] = output_file["t1"]

def t2_info_proc(t2_info, sector, output_file):
    for mechine, info in output_file["t2"].items():
        t2_info.setdefault(mechine, {})[sector] = info
