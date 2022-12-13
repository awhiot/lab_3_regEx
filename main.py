import re

with open('input.txt', 'r', encoding='utf-8') as file:
    reg = file.readlines()

with open('output.txt', 'w', encoding='utf-8') as file:

    for i in range(0, len(reg)):
        if re.search(r'(https?:(/{2})(www\.)?youtu((\.be)|(be\.com))/watch\?v=.{11})', reg[i]) is not None:
            key = reg[i].split('=')[1]
            file.write(key)
