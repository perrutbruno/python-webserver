import os


class OSCheck:
    @staticmethod
    def check_os():
        if os.name == 'nt':
            return 'windows'
        else:
            return 'posix'

    def build_path(oper_sys):
        if oper_sys == 'windows':
            return r"C:\pages"
        else:
            return "/pages"
