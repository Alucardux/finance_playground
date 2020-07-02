"""
Setup logger
"""

# import dependencies
import logging
import logging.config


def setup_logger(config) -> None:
    """
    Setup logger

    Args:
        config: configuration bject

    Returns: None

    """

    # configure logging module
    logging.config.dictConfig(config.logging.logging.to_dict())

    # # create logger
    # logger = logging.getLogger('clp_logger')
    #
    # # todo clean below
    # # create console handler and set level to debug
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    #
    # # add formatter to ch
    # # ch.setFormatter(formatter)
    #
    # # add ch to logger
    # logger.addHandler(ch)

    return None
