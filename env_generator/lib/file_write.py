#!/usr/bin/env python3

import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "file"

def t1_write(info):
    with open(OUTPUT_DIR / "t1_info", "w") as file:
        json.dump(info, file, indent=4)

def t2_write(mechine, info):
    with open(OUTPUT_DIR / F"t2_{mechine}", "w") as file:
        json.dump(info, file, indent=4)

def general_write(file_path, info):
    with open(file_path, "w") as file:
        json.dump(info, file, indent=4)
