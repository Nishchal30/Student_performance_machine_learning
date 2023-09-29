import sys


def error_message(error, error_msg:sys):
    error_detail = error_msg.exc_info()
    filename = error_detail.tb_frame.f_code.co_filename
    error_desc = "Error occured in python script name [{0}] at line number [{1}] with error [{2}]".format(filename, error_detail.tb_lineno, str(error))

    return error_desc


class CustomException(Exception):
    def __init__(self, error_desc, error_msg:sys):
        super().__init__(error_desc)
        self.error_desc = error_message(error_desc,error_msg)

    
    def __str__(self):
        return self.error_desc