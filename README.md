# Matematyka klasa 7 — równania i procenty

**🌐 Strona główna:** https://matkowpa.github.io/rownania-klasa7/

Na stronie głównej są dwa boksy: **Równania** i **Procenty**. Każdy prowadzi do
osobnego planu nauki w tym samym układzie: 11 kroków (0–10), film → ćwiczenia →
sprawdzenie, 24 zadania z odpowiedziami i PDF do wydruku.

- **Równania:** https://matkowpa.github.io/rownania-klasa7/rownania.html
- **Procenty:** https://matkowpa.github.io/rownania-klasa7/procenty.html

**📄 PDF — równania:** https://matkowpa.github.io/rownania-klasa7/zestaw-24-zadan.pdf

**📄 PDF — procenty:** https://matkowpa.github.io/rownania-klasa7/zestaw-24-zadan-procenty.pdf

## Pliki

- `index.html` — strona główna z dwoma kartami wyboru działu
- `rownania.html` — plan równań (bez zależności zewnętrznych, bez CDN)
- `procenty.html` — plan procentów (ten sam design i mechanizm postępu)
- `zestaw-24-zadan.pdf` — równania: plan + 24 zadania + klucz
- `zestaw-24-zadan-procenty.pdf` — procenty: plan + 24 zadania + klucz
- `publish_telegraph.py` — opcjonalna publikacja kopii równań na telegra.ph

## Publikacja

- `main` — źródła
- `gh-pages` — opublikowana kopia serwowana przez GitHub Pages (source: `gh-pages` / root)

Po zmianie HTML-a lub PDF-a trzeba zaktualizować także gałąź `gh-pages`, inaczej
strona nie odświeży się:

```bash
# z gałęzi main, po zmianach
cp index.html rownania.html procenty.html zestaw-24-zadan.pdf zestaw-24-zadan-procenty.pdf /tmp/
git checkout gh-pages
cp /tmp/index.html /tmp/rownania.html /tmp/procenty.html /tmp/zestaw-24-zadan.pdf /tmp/zestaw-24-zadan-procenty.pdf .
git commit -am "Update site"
git push origin gh-pages
git checkout main
```
