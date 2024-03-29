
clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients+= client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list ')


def delete_client(client_name):
    global clients

    clients += client_name
    _add_comma()


def list_clients():
    global clients
    print(clients)

def update_client(client_name,updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name +',')
    else:
        print("Client is not in clients list ")
        

def _add_comma():
    global clients
    clients+=','


def _print_welcome():
    print('Welcome to platzi venta ')
    print('*' * 50)
    print('what would you like to do today? ')
    print('[C]reate client')
    print('[U]reate client')
    print('[D]elete client')


def _get_client_name():
    return input("Wha is the cient name? ")


if __name__ == '__main__':
    _print_welcome()
    
    command = input()
    command = command.upper()
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input("What is the updated client name: ")
        update_client(client_name, update_client_name)
        list_clients()
    elif command == 'D':
        delete_client()
    else:
        print('Invalid command')


