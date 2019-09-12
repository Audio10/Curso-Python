import random

def run():
    number_fount = False
    limit = int(input('Ingresa el numero limite: '))
    random_number = random.randint(0,limit)

    while not number_fount:
        number = int(input('Intenta un numero: '))

        if number == random_number:
            print('Felicidades. Encontraste el numero')
            number_fount = True
        elif number > random_number:
            print('El numero es mas pequeño')
        else:
            print('El numero es mas grande')

if __name__ == '__main__':
    run()