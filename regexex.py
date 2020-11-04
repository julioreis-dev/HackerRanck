import re

pattern = re.compile(r'\d{1,}')
string = 'regex is awesome'
result = pattern.search(string)
print(result.group(0))
