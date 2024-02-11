# Reto 3

MIN, MAX, PRECISION = 5, 50, 10
MESSAGE_CARACTERES = 'El dato capturado debe ser mayor a cinco caracteres y menor a 50 caracteres.  Por favor, intente de nuevo.'
MESSAGE_DIGITOS = 'El dato capturado debe ser de 10 dígitos. Por favor, intente de nuevo.'

users = []
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
        users.append({'id: ': contador,  'name': full_name,  'correo':  email,  'teléfono': phone_number})
        contador += 1
else:
    print('El número de registros nuevos que desea crear no es válido.  Por favor, intente de nuevo.')

print('Total de registros guardados: ', len(users))

for user in users:
     print(user)