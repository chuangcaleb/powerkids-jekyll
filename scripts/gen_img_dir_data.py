import os
from typing import Dict
import pprint
import yaml


def traverse_subdir(base_path: str, dir: str) -> str:
    return base_path + "/" + dir


def get_rcs_dir(dict_obj: Dict, rel_path: str, curr_dir: str) -> Dict:

    new_dir = traverse_subdir(rel_path, curr_dir)

    dir_list = os.listdir(new_dir)

    dir_contents = []

    for item in dir_list:

        # If item is a file
        if "." in item:
            dir_contents.append(item)

        # If item is a file, recurse
        else:
            get_rcs_dir(dict_obj, new_dir, item)

        dict_obj[curr_dir] = dir_contents

    return dict_obj


# Get the list of all files and directories
base_path = "./assets"
output_path = "./_data/img_dir/"

# Get dir data recursively
# dir_data = get_recursive_dir(base_path, "images")

print("Files and directories in '", base_path, "' :")

output_dir = {}

img_dir_data = get_rcs_dir(output_dir, base_path, "images")

# Prints all files
# pprint.pprint(dir_data)

# Dump to yaml
for dir, contents in img_dir_data.items():

    with open(output_path + dir + ".yml", 'a') as file:
        yaml.dump(contents, file)


# # Dump
# with open(output_path, 'w+') as file:
#     yaml.dump(dir_data, file)
