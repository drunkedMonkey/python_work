current_users = ['juan', 'pedro', 'maria', 'luis', 'ana']

new_users = ['paco', 'pedro', 'sam', 'luis', 'blanca']

for new_user in new_users:
    if new_user in current_users:
        print(f"El nombre de usuario {new_user} ya está en uso, por favor elige otro.")
    else:
        print(f"El nombre de usuario {new_user} está disponible.")