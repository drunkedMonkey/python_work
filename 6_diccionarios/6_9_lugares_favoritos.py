lugares_favoritos= {
    'jose': ['casa', 'parque', 'cine'],
    'maria': ['casa', 'parque', 'cine'],
    'juan': ['casa', 'parque', 'cine'],
}

for nombre, lugares in lugares_favoritos.items():
    print(f"\nLos lugares favoritos de {nombre.title()} son:")
    for lugar in lugares:
        print(f"\t{lugar.title()}")