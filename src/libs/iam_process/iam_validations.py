import logging


class IAM_Register():
    def __init__(self, **kwargs) -> None:
        self.fname = kwargs["fname"]
        self.lname = kwargs["lname"]
        self.ph_no = kwargs["ph_no"]
        self.email = kwargs["email"]
        self.passwd = kwargs["passwd"]
        self.re_passwd = kwargs["re_passwd"]
        self.role = kwargs["role"]
    
    def validate_data_type(self):
        logging.info(f"dict_values={self.__dict__.items()}")
        for i,j in self.__dict__.items():
            if type(j) != "str":
                return False
        return True