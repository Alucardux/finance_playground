"""
File system utilities methods
"""

import os
import box


def get_path(config: box.Box, folder: str) -> str:
    """
    Get paths for input from intrinsic file system structure

    Args:
        config: configuration box instance
        folder: can only be one of the following ['raw', 'preprocessed', 'interim', 'output']

    Returns: string with location for data files

    """

    # Save in strings absolute paths
    path = os.path.join(config.settings.storage.preprocessed.path,
                           config.etl_mode.mode, folder)

    # if not present create such directory
    if os.path.exists(path) is False:
        os.makedirs(path)

    return path
