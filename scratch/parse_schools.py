import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_mark = 'escolas: ['
start_idx = content.find(start_mark)
if start_idx != -1:
    sub = content[start_idx + len('escolas: '):]
    bracket_count = 0
    end_pos = 0
    for i, char in enumerate(sub):
        if char == '[':
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_pos = i
                break
    
    json_str = sub[:end_pos+1]
    try:
        escolas = json.loads(json_str)
        print(f'Total de escolas extraídas do index.html: {len(escolas)}')
        for e in escolas[:5]:
            print('-', e.get('inep'), '|', e.get('nome'), '|', e.get('email'))
        with open('scratch/escolas_index.json', 'w', encoding='utf-8') as out:
            json.dump(escolas, out, ensure_ascii=False, indent=2)
        print('Salvo em scratch/escolas_index.json!')
    except Exception as e:
        print('Erro JSON:', e)
else:
    print('start_mark não encontrado')
