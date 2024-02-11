# Reto 4

users = []
MIN, MAX, PRECISION = 5, 50, 10
MESSAGE_CARACTERES = 'El dato capturado debe ser mayor a cinco caracteres y menor a 50 caracteres.  Por favor, intente de nuevo.'
MESSAGE_DIGITOS = 'El dato capturado debe ser de 10 dígitos. Por favor, intente de nuevo.'


while True:
    print('Selecciona una opción: \n1 - Registrar usuarios \n2 - Listar IDs de todos los usuarios registrados \n3 - Consultar información de un usuario \n4 - Editar un usuario por id \n5 - Salir' )
    opcion = input('Selecciona una opción: ')
    match opcion:
        case '1':
            print('Registro de usuarios')
            cantidad = int(input('¿Cuántos registros nuevos desea crear?: '))
            if (cantidad > 0) :
                contador = 1
                while contador <= cantidad:
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
                    print('Usuario ' + str(contador) + ': ' + full_name + '. Registrado correctamente.')
                    users.append({'id': contador, 'name': full_name,  'correo':  email,  'telefono': phone_number})
                    contador += 1
                print('Total de registros guardados: ', len(users))
            else:
                print('El número de registros nuevos que desea crear no es válido.  Por favor, intente de nuevo.')  
        case '2':
            print('Lista de ids:')
            if(len(users) > 0):
                for user in users:
                    print('id: ', user['id'])
            else:
                print('La lista de usuarios se encuentra vacía.')
        case '3':
            print('Consulta de usuario')
            id = int(input('Ingresa el id del usuario a consultar: '))
            if (len(users) > 0 ):
                for user in users:
                    if (user['id'] == id):
                        print(tuple(user.values()))
            else:
                print('La lista de usuarios se encuentra vacía.')
        case '4':
            print('Editar de usuario')
            id = int(input('Ingresa el id del usuario a editar: '))
            if (len(users) > 0 ):
                for user in users:
                    if (user['id'] == id):
                        print('Ingrese los datos del usuario: ')
                        while True:
                            first_name = input('Edite su nombre(s): ') 
                            if (len(first_name) > MIN and len(first_name) <= MAX):
                                break
                            else: 
                                print(MESSAGE_CARACTERES)
                        while True:
                            last_name = input('Edite sus apellidos: ')
                            if (len(last_name) > MIN and len(last_name) <= MAX):
                                break
                            else:
                                print(MESSAGE_CARACTERES)
                        while True:
                            email = input('Edite su correo electrónico: ')
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
                        user['name'] =full_name
                        user['correo'] = email
                        user['telefono'] = phone_number
                        print('Usuario editado')
            else:
                print('La lista de usuarios se encuentra vacía.')
        case '5':
            print('Salir')
            print('Ha salido del menú.')
            break




