# -*- coding: utf-8 -*-

def foreing_exchange_calculator(ammount):
    mex_to_col_rate = 145.97
    return ammount * mex_to_col_rate

def run():
    print('CALCULADORA DE DIVISAS')
    print('Comvierte pesos mexicanos a pesos colombianos.')
    print('')

    ammount = float(input('Ingresa la cantidad de pesos mexicanos que quieres convertir:'))
    result = foreing_exchange_calculator(ammount)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))


if __name__ == '__main__':
    run()
