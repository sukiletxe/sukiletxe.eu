import os
def remove_path_and_ext(path):
    """ Removes path and extension from comment identifier, leaving only the post slug"""
    return os.path.splitext(os.path.split(path)[1])[0]
