ciudades = {
    'madrid': {
        'pais': 'españa',
        'poblacion': '3.3 millones',
        'curiosidad': 'Madrid es la capital de España.'
    },
    'paris': {
        'pais': 'francia',
        'poblacion': '2.1 millones',
        'curiosidad': 'París es la capital de Francia.'
    },
    'berlin': {
        'pais': 'alemania',
        'poblacion': '3.6 millones',
        'curiosidad': 'Berlín es la capital de Alemania.'
    },
}

for ciudad, informacion in ciudades.items():
    print(f"\nCiudad: {ciudad.title()}")
    pais = informacion['pais']
    poblacion = informacion['poblacion']
    curiosidad = informacion['curiosidad']
    print(f"\tPaís: {pais.title()}")
    print(f"\tPoblación: {poblacion}")
    print(f"\tCuriosidad: {curiosidad}")