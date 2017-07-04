def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

text = 'Hello There How are you doing, hope you are doing good!!!'

for part in combine(text,5):
    print(part)
