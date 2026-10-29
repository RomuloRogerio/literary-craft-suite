import glob

for filepath in glob.glob("**/*.json", recursive=True):
    with open(filepath, "rb") as f:
        content = f.read()
    # Remove o marcador UTF-8 BOM se ele existir no início do binário
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
        with open(filepath, "wb") as f:
            f.write(content)
        print(f"[Corrigido] BOM removido de: {filepath}")
    else:
        print(f"[OK] Sem BOM em: {filepath}")