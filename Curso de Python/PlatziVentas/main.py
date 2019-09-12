import sys
import csv
import os

CLIENT_TABLE = '.clients.css'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    temp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(temp_table_name, mode='w') as f:
        writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        
    os.rename(temp_table_name,CLIENT_TABLE)


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)  
    else:
        print('Client already is in the clients\' list')


def update_client(client_name):
    global clients
    idx = search_client(client_name)
    if idx != None:
        client = _get_new_client()
        clients[idx].update(client)

    else:
        _client_not_found()


def delete_client(idx):
    global clients
    
    if not None:
        clients.pop(idx)
    else:
        _client_not_found()
        

def search_client(client_name):
    global clients
    for idx, client in enumerate(clients):
        if(client['name']!= client_name):
            continue
        else:
            return idx


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        # print('{}: {}'.format(idx, client['name']))
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid= idx,
            name = client['name'],
            company=client['company'],
            email= client['email'],
            position= client['position']
        ))


def _print_welcome():
    print('*' * 50)
    print('           WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]erch client')
    print('[L]ist clients')
    print('[E]xit')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client\'s name? ')
        
        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _client_not_found():
    return print('Client is not in the client\'s list ')


def _get_new_client():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


if __name__ == '__main__':
    _initialize_clients_from_storage()
    command =''

    while command != 'E':
        _print_welcome()
        command = input('').upper()

        if command == 'C':
            client = _get_new_client()
            # client_name = _get_client_name()
            create_client(client)
        elif command == 'D':
            client_name = _get_client_name()
            found = search_client(client_name)
            delete_client(found)
        elif command == 'U':
            client_name = _get_client_name()
            update_client(client_name)
        elif command == 'L':
            list_clients()
        elif command == 'S':
            client_name = _get_client_name()
            found = search_client(client_name)

            if not None:
                print('The client is in the client\'s list')
            else:
                print('The client: {} is not in our client\' list'.format(client_name))
            
            print('')
        elif command == 'E':
            print('Bye')
        else:
            print('Invalid command')
        print('')

    _save_clients_to_storage() 
