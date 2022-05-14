class IAM_Register():
    def __init__(self, **kwargs) -> None:
        self.fname = kwargs["fname"]
        self.lname = kwargs["lname"]
        self.ph_no = kwargs["ph_no"]
        self.email = kwargs["email"]
        self.passwd = kwargs["passwd"]
        self.re_passwd = kwargs["re_passwd"]
        self.role = kwargs["role"]