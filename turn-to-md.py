file_names = ['4-8', '4-9', '4-10', '4-11+', '4-19', '4-20']
md = open('chapter4.md', 'w')
for file in file_names:
    full_name = file + '.cpp'
    f = open(full_name, 'r', encoding='utf-8')
    codes = f.read()
    md.write('## ' + file + '\n')
    md.write('```cpp\n' + codes + '\n```\n')
    f.close()
md.close()
    