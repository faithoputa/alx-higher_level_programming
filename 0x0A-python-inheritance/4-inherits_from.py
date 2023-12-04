#!/usr/bin/python3
def inherits_from(obj, a_class):
    for baseclass in a_class.__bases__:
        if isinstance(obj, obj):
            return True
    return False

