import os
import sys

class HousingException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message

    @staticmethod
    def get_detail_error_message(error_message:Exception,error_detail:sys)->str:

        '''
        error_message:Exception object
        error_details: object of sys module
        '''
        _,_,exac_tb = error_detail.exc_info()

        line_number = exac_tb.tb_frame.f_lineno
        file_name = exac_tb.tb_frame.f_code.co_filename
        error_message = f"Errro occured in script:[{file_name}] at line number :[{line_number}] error message is :[{error_message}]"

        return error_message
    
    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()
        