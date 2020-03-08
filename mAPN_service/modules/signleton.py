class Singleton(object):
    '''Ref: https://stackoverflow.com/a/6798042
    '''

    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(
                cls, *args, **kwargs
            )
        return cls._instances[cls]

