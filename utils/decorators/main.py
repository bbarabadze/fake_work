import os


def file_exists_decorator(func):
    def wrapper(filename, *args, **kwargs):
        if os.path.exists(filename):
            return func(filename, *args, **kwargs)
        else:
            raise FileNotFoundError("File doesn't exist.")

    return wrapper