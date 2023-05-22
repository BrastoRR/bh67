def country(city):
    mydict = {'Belarus': ('Minsk', 'Brest', 'Grodno', 'Mogilev'), 'Russia': ('Moskva', 'Smolensk', 'Piter')}
    return [i for i in mydict if set(mydict[i]) & {city}]

print(country(input('Введите город: ')))
