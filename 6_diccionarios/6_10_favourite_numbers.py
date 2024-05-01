favourite_numbers={
    'Ivan': [10, 11, 12, 13, 14, 15],
    'Sami': [13, 14, 15, 16, 17, 18],
    'Blanca':{7, 8, 9, 10, 11, 12}
}

for name, numbers in favourite_numbers.items():
    print(name + "'s favourite numbers are:")
    for number in numbers:
        print("\t" + str(number))