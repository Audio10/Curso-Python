
def busqueda(numbers, number,low,high):
    
    if low > high:
        return False

    mid = int( (low+high) / 2 )
    print(mid)

    if(numbers[mid] == number):
        return True
    elif(numbers[mid] > number):
        return busqueda(numbers, number,low, mid - 1)
    else:
        return busqueda(numbers, number, mid +1, high)

if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
    number = int(input('Que numero estas buscando: '))
    result = busqueda(numbers, number,0, len(numbers)-1)


    if result == True:
        print('El numero fue encontrado!')
    else:
        print('El numero no fue encontrado!')