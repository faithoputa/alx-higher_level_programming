def lookup(obj):
    result = []
    for name, value in obj.__dict__.items():
        if isinstance(value, (int, float, str, bool, list, tuple, dict, set, any, typ, ...)):
            result.append(name)
    return result

