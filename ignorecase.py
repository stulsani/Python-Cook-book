import re

text = 'UPPER PYTHON, lower python, Mixed Python'

newtext = re.findall('python', text, flags = re.IGNORECASE)

print(newtext)
