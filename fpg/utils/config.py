"""
Configuration utilities
"""

import box
import yaml
import os


def load_config(config_path: str = os.path.join(os.getcwd(), "config")) \
        -> box.Box:
    """
    Load multiple configuration files in same box instance

    Returns: box instance of configuration files

    """

    config_dict = {}

    # Programmatically reads all yml configuration files in repo without .eg. in name
    files = os.listdir(config_path)

    for config_fname in files:
        if (config_fname.split(".")[-1].lower() == "yml") & (".eg" not in config_fname):
            # save dict in dictionary object
            with open(os.path.join(config_path, config_fname)) as fp:
                # save name without yml
                save_name = config_fname.replace(".yml", "")
                config_dict[save_name] = yaml.safe_load(fp)

    # convert as box object
    config = box.Box(config_dict)

    return config
