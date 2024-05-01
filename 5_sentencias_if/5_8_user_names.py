# user_names = ['admin', 'user', 'guest', 'root', 'pepe']
user_names = []

if user_names:
    for user in user_names:
        if(user == 'admin'):
            print('Hola admin, ¿quieres ver un reporte de estado?')
        else:
            print(f"Hola {user}, gracias por volver a entrar.")
else:
    print('Necesitamos encontrar a algún usuario.')