
class ProtectedObject:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            object.__setattr__(self, k, v)

    def __setattr__(self, attr, value):
        if attr[0] == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, attr, value)

    def __getattribute__(self, attr):
        if attr[0] == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, attr)

    def __delattr__(self, attr):
        if attr[0] == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, attr)




user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    del user._password
except AttributeError as e:
    print(e)



# user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
#
# try:
#     print(user._secret)
# except AttributeError as e:
#     print(e)
#
# try:
#     user._secret = 'PG'
# except AttributeError as e:
#     print(e)
#
# try:
#     del user._secret
# except Exception as e:
#     print(e)
