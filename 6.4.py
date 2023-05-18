def text_str(text):
    count = 0
    for i in range(len(text)):
        if isinstance(text[i], str):
            text[count] = text[i]
            count += 1
    del text[count:]
    return text


print(text_str(['London', 123, -6, 'Hello', True, 12, -3.14, 'python']))
