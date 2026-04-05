def check_password(password, chars="$%!?@#"):
    if len(password) >= 8:
        for i in password:
            if i in chars:
                return True
        return False
    else:
        return False


print(check_password("5657dfgfh098A!@#"))