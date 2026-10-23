# Równania krok po kroku — klasa 7

**🌐 Strona:** https://matkowpa.github.io/rownania-klasa7/

**📄 PDF do wydruku:** https://matkowpa.github.io/rownania-klasa7/zestaw-24-zadan.pdf

Plan nauki równań pierwszego stopnia dla ucznia klasy 7: 11 kroków (0–10) w układzie
film → ćwiczenia → sprawdzenie, z linkami do lekcji Pi-stacji, Matzoo, ZPE i Szalonych Liczb
oraz zestawem 24 zadań z odpowiedziami.

## Pliki

- `index.html` — cała strona (bez zależności zewnętrznych, bez CDN)
- `zestaw-24-zadan.pdf` — wersja do wydruku (plan + 24 zadania + klucz)
- `publish_telegraph.py` — opcjonalna publikacja kopii na telegra.ph

## Publikacja

- `main` — źródła
- `gh-pages` — opublikowana kopia serwowana przez GitHub Pages (source: `gh-pages` / root)

Po zmianie `index.html` lub PDF-a trzeba zaktualizować także gałąź `gh-pages`, inaczej
strona nie odświeży się:

```bash
# z gałęzi main, po zmianach w index.html / PDF
cp index.html zestaw-24-zadan.pdf /tmp/
git checkout gh-pages
cp /tmp/index.html /tmp/zestaw-24-zadan.pdf .
git commit -am "Update site"
git push origin gh-pages
git checkout main
```
