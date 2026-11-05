# Równania i procenty krok po kroku — klasa 7

**🌐 Strona:** https://matkowpa.github.io/rownania-klasa7/

**📄 PDF — równania:** https://matkowpa.github.io/rownania-klasa7/zestaw-24-zadan.pdf

**📄 PDF — procenty:** https://matkowpa.github.io/rownania-klasa7/zestaw-24-zadan-procenty.pdf

Dwa plany nauki dla ucznia klasy 7 w tym samym układzie: 11 kroków (0–10),
film → ćwiczenia → sprawdzenie, z linkami do lekcji Pi-stacji, Matzoo, ZPE
i Szalonych Liczb oraz zestawem 24 zadań z odpowiedziami.

- **Równania** — równania pierwszego stopnia (`index.html`).
- **Procenty** — procenty, podwyżki i obniżki, VAT, punkty procentowe (`procenty.html`).

## Pliki

- `index.html` — plan równań (bez zależności zewnętrznych, bez CDN)
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
cp index.html procenty.html zestaw-24-zadan.pdf zestaw-24-zadan-procenty.pdf /tmp/
git checkout gh-pages
cp /tmp/index.html /tmp/procenty.html /tmp/zestaw-24-zadan.pdf /tmp/zestaw-24-zadan-procenty.pdf .
git commit -am "Update site"
git push origin gh-pages
git checkout main
```
