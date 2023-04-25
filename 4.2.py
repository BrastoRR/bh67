text = input('Введите текст: ')
text = text.replace(' ', '')
symbols = list(text)
numbers = [symbols.count(symbols[i]) for i in range(len(symbols))]
data = {symbols[i]: numbers[i] for i in range(len(symbols))}
print(data)
