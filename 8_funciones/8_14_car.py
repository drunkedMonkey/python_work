def make_car(marca, modelo, **car_info):
    car_info['marca'] = marca
    car_info['modelo'] = modelo
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)