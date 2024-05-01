pizzas = ['pepperoni', 'cheese', 'hawaiian', 'veggie', 'meat lovers']
friend_pizzas = pizzas[:]

pizzas.append('mushroom')
friend_pizzas.append('sausage')

print('Mis pizzas favoritas son:')
for pizza in pizzas:
    print(pizza)

print('Las pizzas favoritas de mi amigo son:')
for pizza in friend_pizzas:
    print(pizza)