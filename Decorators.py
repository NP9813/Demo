# #Decorators using function
# def decorator_func(original_func):
#     def wrapper_func(*args,**kwargs):
#         print(f"wrapper function executed {original_func.__name__} with args {args}")
#         return original_func(*args,**kwargs)
#     return wrapper_func
#
# #Decorators using class
# class decorator_class():
#     def __init__(self,original_func):
#         self.original_func = original_func
#
#     def __call__(self, *args, **kwargs):
#         print(f"call method executed {self.original_func.__name__} with args {args}")
#         return self.original_func(*args, **kwargs)
#
#
# @decorator_func
# def display():
#     print("Display func ran")
#
# @decorator_func
# def display_info(name,age):
#     print(f"display info ran with arguments {name} {age}")
#
# display_info("Nikhil",26)
#
# display()
# display = decorator_func(display)
#
# display()


#Logging using decortors
# def my_logger(original_func):
#     import logging
#     logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.DEBUG)
#     def wrapper(*args, **kwargs):
#         logging.info(f"Ran with args-{args}, kwargs-{kwargs}")
#         return original_func(*args,**kwargs)
#     return wrapper
#
# @my_logger
# def display_info(name,age):
#     print(f"display info ran with arguments {name} {age}")
#
# display_info("Nikhil",26)

#Multiple Decorators on one func
from functools import wraps
def my_logger(original_func):
    import logging
    logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.DEBUG)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args-{args}, kwargs-{kwargs}")
        return original_func(*args,**kwargs)
    return wrapper

def my_timer(original_func):
    import time

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args,**kwargs)
        t2 = time.time() - t1
        print(f"{original_func.__name__} function ran in {t2} ")
    return wrapper

@my_logger
@my_timer
def display_info(name,age):
    print(f"display info ran with arguments {name} {age}")

display_info("Nikhil",26)