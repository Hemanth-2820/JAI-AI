file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the double comma syntax error
content = content.replace('],,', '],')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed syntax error!")
