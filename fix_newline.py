import re

file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the literal \n strings that were injected incorrectly
content = content.replace(',\\n    "extendedCapabilities"', ',\n    "extendedCapabilities"')
content = content.replace('\\n    "extendedCapabilities"', '\n    "extendedCapabilities"')
content = content.replace('],\\n', '],\n')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed literal newline escapes!")
