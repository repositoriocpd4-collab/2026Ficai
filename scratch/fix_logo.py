import re

path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find full logo base64 in Page 1 (around line 9467)
match = re.search(r'src="(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG4AAACH[^"]+)"', content)
if match:
    full_logo = match.group(1)
    print(f"Full logo found! Length: {len(full_logo)}")
    
    truncated = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG4A…e7KwgGhN7/Sk8ww9S/j8rC2j1oCLQOwAAAABJRU5ErkJggg=='
    if truncated in content:
        print("Found truncated logo in content. Replacing...")
        new_content = content.replace(truncated, full_logo)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated index.html!")
    else:
        print("Truncated logo string not found! Let's check page-2 img tag...")
        # Search page-2 logo src
        page2_match = re.search(r'(<div class="print-page page-2">.*?<img class="p-crest"\s+src=")([^"]+)(")', content, re.DOTALL)
        if page2_match:
            current_src = page2_match.group(2)
            print(f"Current Page 2 src length: {len(current_src)}")
            if len(current_src) < len(full_logo):
                print("Replacing Page 2 src with full_logo...")
                new_content = content[:page2_match.start(2)] + full_logo + content[page2_match.end(2):]
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print("Successfully updated index.html via regex replacement!")
else:
    print("Full logo not matched.")
