import re


def check_email(email):
    if email is not None and re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None:
        return True
    else:
        return False
