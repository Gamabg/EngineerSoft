bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0] = 'bmx'
print(bicycles)
print(bicycles[3])

bicycles.append('Aro')
print(bicycles)

del bicycles[1]
print(bicycles)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles.pop())

print(bicycles)

cars = ['bmw','audi','toyota','subaru']

cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)

tracks = ['breath', 'on the run', 'time', 'the great gig in the sky', 'money',
'us and then', 'any colour you like', 'brain damage', 'eclipse']
lista = tracks
print(lista)

tracks.remove('breath')
tracks.remove('on the run')
print(lista)