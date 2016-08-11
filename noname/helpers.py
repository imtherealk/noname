def unescape_string(s):
    """
    Unescape backslash-escaped string.
    """
    return s.encode('utf-8').decode('unicode-escape')
