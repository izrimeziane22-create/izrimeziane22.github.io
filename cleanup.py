#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0

while i < len(lines):
    line = lines[i]
    
    # Check if we're at the start of a veille section
    if '<section id="veille">' in line:
        # Look ahead to see if there's another veille section after this one
        is_bad_section = False
        closing_pos = -1
        
        for j in range(i + 1, min(i + 30, len(lines))):
            if '</section>' in lines[j]:
                closing_pos = j
                # Check if the next section is also veille
                for k in range(j + 1, min(j + 3, len(lines))):
                    if '<section id="veille">' in lines[k]:
                        is_bad_section = True
                        break
                break
        
        if is_bad_section and closing_pos > 0:
            # Skip this bad section entirely (including the closing tag)
            i = closing_pos + 1
        else:
            # This is the good section, keep it
            new_lines.append(line)
            i += 1
    else:
        new_lines.append(line)
        i += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('File cleaned successfully!')
