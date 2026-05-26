def obrat(s):
    if len(s) <= 1:
        return s

    return obrat(s[1:]) + s[0]