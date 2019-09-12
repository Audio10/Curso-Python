PASSWORD = '12345'


def password_requeried(func):
    def wrapper():
        password = input('cual es tu contraseña')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta')
    
    return wrapper


# RECIBE SAY_MY_NAME
def upper(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)

        return result.upper()

    return wrapper


@upper
def say_my_name(name):
    return 'Hola {}'.format(name)


@password_requeried
def needs_password():
    print('La contraseña es correcta')


if __name__ == '__main__':
    print( say_my_name(input('cual es tu nombre ')) )