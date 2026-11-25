"""Lê a pasta cifras/ e gera o arquivo cifras.json que o site usa."""
import json
from pathlib import Path

pasta = Path("cifras")
extras = {}
if Path("tags.json").exists():
    extras = json.loads(Path("tags.json").read_text(encoding="utf-8"))

lista = []
for p in pasta.rglob("*"):
    if not p.is_file() or p.suffix.lower() != ".pdf":
        continue
    rel = p.relative_to(pasta)
    tags = list(rel.parts[:-1])                       # nomes das subpastas viram tags
    tags += extras.get(p.name, []) + extras.get(rel.as_posix(), [])
    vistas, unicas = set(), []
    for t in tags:
        if t.lower() not in vistas:
            vistas.add(t.lower()); unicas.append(t)
    lista.append({"titulo": p.stem, "arquivo": "cifras/" + rel.as_posix(), "tags": unicas})

lista.sort(key=lambda c: c["titulo"].lower())
Path("cifras.json").write_text(json.dumps(lista, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(lista)} cifras encontradas")
