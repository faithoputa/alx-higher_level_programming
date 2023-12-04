#!/usr/bin/python3
def is_kind_of_class(obj, a_class):

    classtype = type(obj)
    while classtype != a_class and classtype is not a_class.__base__:
        if classtype is a_class.__base__:
            classtype = classtype.__base__
        elif classtype.__name__ == 'object':
            break
        else:
            classtype = classtype.__base__
    return True

