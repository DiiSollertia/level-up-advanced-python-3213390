import functools


def arg_checker(*arg_types):
    '''An argument checker decorator that checks both:
        - The number of variables that you use for a function
        - The type of each variable.
       Raises a TypeError if either of these fail'''
    def decorator(func):
        @functools.wraps(func)
        def check(*args):
            if len(args) != len(arg_checker) or any(not isinstance(x, arg_types[i]) for i, x in enumerate(args)):
                raise TypeError
            return func(*args)
        return check
    return decorator
