# Reto 2

cantidad = int(input ('¿Cuántos registros nuevos desea crear?: '))
if (cantidad > 0) :
    min, max, precision = 5, 50, 10
    registrado = 1
    while registrado <= cantidad:
        first_name = input('Ingrese su nombre(s): ') 
        if (len(first_name) > min and len(first_name) <= max):
            last_name = input('Ingrese sus apellidos: ')
            if (len(last_name) > min and len(last_name) <= max):
                email = input('Ingrese su correo electrónico: ')
                if (len(email) > min and len(email) <= max):
                    phone_number = int(input('Ingrese su número de teléfono: '))
                    if (len(str(phone_number)) == precision):
                        full_name = first_name + ' ' + last_name
                        print('Registro ' + str(registrado) + ': ' + full_name + '. Creado correctamente.')
                        registrado += 1
                    else:
                        print('El número de teléfono debe ser de 10 dígitos. Por favor, intente de nuevo.')
                else:
                    print('El correo electrónico debe ser mayor a cinco caracteres y menor a 50 caracteres.  Por favor, intente de nuevo.')
            else:
                print('El apellido debe ser mayor a cinco caracteres y menor a 50 caracteres.  Por favor, intente de nuevo.')
        else: 
            print('El nombre debe ser mayor a cinco caracteres y menor a 50 caracteres.  Por favor, intente de nuevo.')
else:
    print('El número de registros nuevos que desea crear no es válido.  Por favor, intente de nuevo.')