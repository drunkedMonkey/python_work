rios = {
    'nilo': 'egipto',
    'amazonas': 'brasil',
    'ganges': 'india',
}

for rio, pais in rios.items():
    print(f"El {rio.title()} corre por {pais.title()}.")

for rio in rios.keys():
    print(rio.title())

for pais in rios.values():
    print(pais.title())
