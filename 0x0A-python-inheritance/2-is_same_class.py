#!/usr/bin/python3
def is_same_class(obj, a_class):
   
    if isinstance(obj, a_class):
        return True
    elif isinstance(obj, a_class.__base__):
        return True
    else:
        return False

