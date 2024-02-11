# Reto 5

users = []
MIN, MAX, PRECISION = 5, 50, 10
MESSAGE_CARACTERES = 'El dato capturado debe ser mayor a cinco caracteres y menor a 50 caracteres.  Por favor, intente de nuevo.'
MESSAGE_DIGITOS = 'El dato capturado debe ser de 10 dígitos. Por favor, intente de nuevo.'

# Leer datos ingresados
def leer_datos(contador):
        print('Ingrese los datos del usuario: ', contador)
        while True:
            first_name = input('Ingrese su nombre(s): ') 
            if (len(first_name) > MIN and len(first_name) <= MAX):
                break
            else: 
                print(MESSAGE_CARACTERES)
        while True:
            last_name = input('Ingrese sus apellidos: ')
            if (len(last_name) > MIN and len(last_name) <= MAX):
                break
            else:
                print(MESSAGE_CARACTERES)
        while True:
            email = input('Ingrese su correo electrónico: ')
            if (len(email) > MIN and len(email) <= MAX):
                break
            else:
                print(MESSAGE_CARACTERES)
        while True:    
            phone_number = int(input('Ingrese su número de teléfono: '))
            if (len(str(phone_number)) == PRECISION):
                break
            else:
                print(MESSAGE_DIGITOS)
        full_name = first_name + ' ' + last_name
        return   {'id': contador, 'name': full_name,  'correo':  email,  'telefono': phone_number}

# Agregar un nuevo usuario
def new_user():
    print('Registro de usuarios')
    cantidad = int(input('¿Cuántos registros nuevos desea crear?: '))
    if (cantidad > 0) :
        contador = 1
        while contador <= cantidad:
            user = leer_datos(contador)
            print('Usuario ' + str(user['id']) + ': ' + user['name'] + '. Registrado correctamente.')
            users.append(user)
            contador += 1
        print('Total de registros guardados: ', len(users))
    else:
        print('El número de registros nuevos que desea crear no es válido.  Por favor, intente de nuevo.')  

# Consultar un usuario
def show_user():
     print('Consulta de usuario')
     id = int(input('Ingresa el id del usuario a consultar: '))
     if (len(users) > 0 ):
         for user in users:
             if (user['id'] == id):
                print(tuple(user.values()))
     else:
        print('La lista de usuarios se encuentra vacía.')

# Editar un usuario
def edit_user():
    print('Editar de usuario')
    id = int(input('Ingresa el id del usuario a editar: '))
    if (len(users) > 0 ):
        for user in users:
            if (user['id'] == id):
                user_editado = leer_datos(id);
                user['name'] = user_editado['name']
                user['correo'] = user_editado['correo']
                user['telefono'] = user_editado['telefono']
                print('Usuario editado', user)
    else:
        print('La lista de usuarios se encuentra vacía.')

# Eliminar un usuario
def delete_user():
    print('Eliminar un usuario')
    id = int(input('Ingresa el id del usuario a eliminar: '))
    if (len(users) > 0 ):
        for user in users:
            if (user['id'] == id):
               users.remove(user)
               print('Usuario eliminado', user)
    else:
        print('La lista de usuarios se encuentra vacía.')

# Mostrar lista de usuarios
def list_users():
    print('Lista de ids:')
    if(len(users) > 0):
        for user in users:
            print('id: ', user['id'], ' nombre completo: ', user['name'], ' correo: ', user['correo'], ' telefono: ', user['telefono'] )
    else:
        print('La lista de usuarios se encuentra vacía.')

# Opciones
while True:
    print('Selecciona una opción: \n1 - Registrar usuarios \n2 - Consultar información de un usuario \n3 - Editar un usuario por id  \n4 - Eliminar un usuario  \n5 - Listar usuarios registrados \n6 - Salir' )
    opcion = input('Selecciona una opción: ')
    match opcion:
        case '1':
            new_user()
        case '2':
            show_user()  
        case '3':
           edit_user()
        case '4':
           delete_user()
        case '5': 
            list_users()
        case '6':
            print('Salir')
            print('Ha salido del menú.')
            break
