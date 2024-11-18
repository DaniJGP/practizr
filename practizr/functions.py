def is_empty(username=None, password=None):
    if username is None:
        return "Username required."
    if password is None:
        return "Password required."
    return None