from probar_codigo.ciudad import formatted_city_country


def test_ciudad_pais():
    resultado = formatted_city_country('santiago', 'chile')
    assert resultado == 'Santiago, Chile'

    resultado = formatted_city_country('santiago', 'chile', 5000000)