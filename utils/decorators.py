
def named(name: str):
    def decorator(func):
        func._element_name = name
        return func
    return decorator