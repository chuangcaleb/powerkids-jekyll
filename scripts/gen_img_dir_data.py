import os
from typing import Dict, List
import pprint
import yaml


def get_dir(current_path: str, dir: str) -> Dict:
    """
    Recursively get a list of pathnames of all files
    """

    dir_list = os.listdir(current_path + "/" + dir)

    return {
        dir: [
            item if "." in item
            else get_dir(current_path + "/" + dir, item)
            for item in dir_list
        ]
    }


# Get the list of all files and directories
base_path = "./assets/"
output_path = "./_data/img_dir_data.yml"

# Get dir data recursively
dir_data = get_dir(base_path, "images")

print("Files and directories in '", base_path, "' :")

# Prints all files
pprint.pprint(dir_data)

# Dump
with open(output_path, 'w+') as file:
    yaml.dump(dir_data, file)
