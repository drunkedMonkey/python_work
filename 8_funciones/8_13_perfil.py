def built_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = built_profile('Pepe', 'Ibañez', location='Spain', field='IT', age=33)

print(user_profile)
    