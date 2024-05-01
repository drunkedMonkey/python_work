mountains = [ 'Lhotse', 'Makalu','Everest', 'K2', 'Kangchenjunga']

print(mountains)
print(len(mountains))

print(sorted(mountains))
print(sorted(mountains, reverse=True))

mountains.sort()
print(mountains)

mountains.sort(reverse=True)

print(mountains)

mountains.reverse()
print(mountains)

mountains.append('Annapurna')
print(mountains)

mountains.insert(1, 'Manaslu')
print(mountains)

del mountains[0]
print(mountains)

mountains.remove('K2')
print(mountains)

mountains.pop()
print(mountains)