def unescape_string(s):
    """
    Unescape backslash-escaped string.
    """
    return s.encode('utf-8').decode('unicode-escape')


def escape_string(s):
    """
    Backslash-escape string.
    """
    return s.encode('unicode-escape').decode('utf-8').replace('"', '\\"')
