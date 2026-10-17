#!/usr/bin/env python3

import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "file"

def t1_write(info):
    with open("/root/clilab/ex200_sim/env_generator/file/t1_meta", "w") as file:
        json.dump(info, file, indent=4)

def t2_write(mechine, info):
    with open(f"/root/clilab/ex200_sim/env_generator/file/t2_{mechine}", "w") as file:
        json.dump(info, file, indent=4)
