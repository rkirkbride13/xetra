"""
Custom Exceptions
"""


class WrongFormatException(Exception):
    """
    WrongFormatException class

    Exception that can be raised when the format type
    given as an arguement is not supported
    """


class WrongMetaFileException(Exception):
    """
    WrongMetaFileException class

    Exception that can be raised when the meta file format is not correct
    """
