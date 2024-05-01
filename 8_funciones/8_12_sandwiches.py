def prepare_sandwich(*ingredients):
    print("Preparando un sandwich con los siguientes ingredientes:")
    for ingredient in ingredients:
        print("- " + ingredient)

prepare_sandwich('jamon', 'queso', 'lechuga', 'tomate')