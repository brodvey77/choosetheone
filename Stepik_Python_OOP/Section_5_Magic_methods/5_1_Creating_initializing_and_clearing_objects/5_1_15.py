
class Config:
    _conf = None

    def __new__(cls, *args, **kwargs):
        if cls._conf is None:
            cls._conf = object.__new__(cls)
        return cls._conf

    def __init__(self, program_name='GenerationPy', environment='release', loglevel='verbose', version='1.0.0'):
        self.program_name = program_name
        self.environment = environment
        self.loglevel = loglevel
        self.version = version


config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.program_name = 'GenerationPy'
            cls._instance.environment = 'release'
            cls._instance.loglevel = 'verbose'
            cls._instance.version = '1.0.0'
        return cls._instance