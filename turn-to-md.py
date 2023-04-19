import os

file_names = os.listdir()
md = open('chapter4.md', 'w')
for file in file_names:
    if file.split('.')[1] != 'cpp':
        continue
    task_name = file.split('.')[0]
    f = open(file, 'r', encoding='utf-8')
    codes = f.read()
    md.write('## ' + task_name + '\n')
    md.write('```cpp\n' + codes + '\n```\n')
    f.close()
md.close()
    
