def je_palindrom(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return je_palindrom(s[1:-1])