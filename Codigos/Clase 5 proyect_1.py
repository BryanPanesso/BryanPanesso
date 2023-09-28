# CRUD
# My Project Pharmacy

clients = "BRYAN, MATEO,"  # variable of type string


def create_client(client_name):
    global clients
    if client_name not in clients: #El in sirve para preguntar si algo esta o no en otro
        clients += client_name
    else:
        print("Client already is in the Client's list")


def read_client(client_name):
    global clients
    if client_name in clients:
        print("Find user")
    else:
        print("not find user")

def update_client(client_name):
    global clients
    if client_name in clients: 
        new_name = _get_client_name()
        clients = clients.replace(client_name, new_name)
        print(f"Updated {client_name} to {new_name}")
    else:
        print("Client not found")

def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ",", "")  # Remove the client name and the trailing comma
        print(f"Deleted {client_name}")
    else:
        print("Client not found")

def list_clients():  # Devuelve la lista de clientes actualizada
    global clients
    print(clients)


def _print_welcome():
    print("Welcome to the Pharmacy Univalle Tuluá")
    print("*" * 60)
    print("What would you like to do today")
    print("[C]reate client")
    print("[R]ead client")
    print("[U]pdate client")
    print("[D]elete client")


def _get_client_name():
    return input("Enter your name: ").upper()


if __name__ == '__main__':

    _print_welcome()

    option = input("Type your option:").upper()
    print(option)
    if option == 'C':
        client_name = _get_client_name()  # se obtiene el nombre del cliente
        create_client(client_name)  # se envia el nombre del cliente
        list_clients()
    elif option == 'R':
        client_name = _get_client_name()
        read_client(client_name)
        list_clients()
        pass
    elif option == 'U':
        client_name = _get_client_name()
        update_client(client_name)
        list_clients()
    elif option == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    else:
        print("Invalid Command")
