import sys
def log(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} ',end='')
        for arg in args:
            print(f'{arg} ',end='')
        return func(*args, **kwargs)
    return wrapper

def log_to(file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                open(file, 'a')
            except FileNotFoundError:
                sys.touch(file)
            with open(file, 'a') as f:
                f.write(f'{func.__name__} ')
                for arg in args:
                    f.write(f'{arg} ')
                f.write('\n')
            return func(*args, **kwargs)
        return wrapper
    return decorator