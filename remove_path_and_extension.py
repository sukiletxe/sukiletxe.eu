import os
def remove_path_and_ext(path):
    """ Removes  extension and 'cache/' from comment identifier, leaving only '/path/to/post' + the post slug"""
    return os.path.splitext(path.replace('cache/', ''))[0]
