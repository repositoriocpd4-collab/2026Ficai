import json, re

path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('escolas: [')
if pos != -1:
    sub = content[pos + len('escolas: '):]
    bracket_count = 0
    end_pos = -1
    for idx, c in enumerate(sub):
        if c == '[':
            bracket_count += 1
        elif c == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_pos = idx + 1
                break
    if end_pos != -1:
        data = json.loads(sub[:end_pos])
        print(f"Total de escolas extraídas: {len(data)}")
        with open(r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\scratch\escolas.json', 'w', encoding='utf-8') as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
        print("Salvo em scratch/escolas.json!")
