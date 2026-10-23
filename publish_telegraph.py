#!/usr/bin/env python3
"""Publikuje plan równań na telegra.ph (bez konta) i zapisuje URL."""
import json, os, urllib.request, urllib.parse

API = "https://api.telegra.ph/"
TOKEN_FILE = "/opt/data/projects/rownania-klasa7/.telegraph_token"


def call(method, **params):
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(API + method, data=data)
    with urllib.request.urlopen(req, timeout=30) as r:
        out = json.load(r)
    if not out.get("ok"):
        raise RuntimeError(out)
    return out["result"]


def a(text, href):
    return {"tag": "a", "attrs": {"href": href}, "children": [text]}


def p(*children):
    return {"tag": "p", "children": list(children)}


def li(*children):
    return {"tag": "li", "children": list(children)}


def ul(items):
    return {"tag": "ul", "children": items}


def h3(text):
    return {"tag": "h3", "children": [text]}


def h4(text):
    return {"tag": "h4", "children": [text]}


def b(text):
    return {"tag": "b", "children": [text]}


def em(text):
    return {"tag": "em", "children": [text]}


def link_line(label, url, note=""):
    # czytelny link: etykieta jako h4, tytuł jako klikalny tekst
    title = url.rsplit("/", 1)[-1]
    pretty = {
        "mat00382-liczba-spelniajaca-rownanie": "Liczba spełniająca równanie (Pi-stacja)",
        "mat00383-rozwiazywanie-rownan-wprowadzenie": "Rozwiązywanie równań — wprowadzenie (Pi-stacja)",
        "mat00384-rozwiazywanie-rownan-rozwiazanie-w-dwoch-krokach": "Rozwiązanie w dwóch krokach (Pi-stacja)",
        "mat00385-rozwiazywanie-rownan-rownania-z-nawiasami": "Równania z nawiasami (Pi-stacja)",
        "mat00386-rozwiazywanie-rownan-rownania-z-ulamkami": "Równania z ułamkami (Pi-stacja)",
        "mat00387-rownania-oznaczone-nieoznaczone-i-sprzeczne": "Równania sprzeczne i tożsamościowe (Pi-stacja)",
        "mat00371-przeksztalcenia-wzorow": "Przekształcenia wzorów (Pi-stacja)",
        "mat00012-1-a-waga-a-rownanie": "Waga i równanie — ćwiczenie interaktywne",
    }.get(title, title)
    kids = [a(pretty, url)]
    if note:
        kids.append(" — " + note)
    return [h4("▶ " + label), p(*kids)]


PIST = "https://pistacja.tv/film/"
STEPS = [
    {
        "n": 0, "t": "Sprawdź, od czego zaczynasz", "time": "10 minut · diagnoza",
        "body": [
            p("Rozwiąż 5 zadań na kartce, bez zaglądania do odpowiedzi:"),
            ul([li("x + 6 = 15"), li("3x = 21"), li("2x − 5 = 9"),
                li("4(x − 1) = 2x + 6"), li("5 − x = 2")]),
            p(b("Odpowiedzi: "), "9, 7, 7, 5, 3."),
            p("1–2 źle → zacznij od kroku 1. 3 źle → krok 2 i 3. 4 źle → krok 5. "
              "5 źle → krok 3 i więcej ćwiczeń ze znakami. Wszystko dobrze → możesz zacząć od kroku 4."),
        ],
    },
    {
        "n": 1, "t": "Co to znaczy, że liczba spełnia równanie", "time": "20 minut",
        "body": [
            link_line("Obejrzyj", PIST + "mat00382-liczba-spelniajaca-rownanie"),
            link_line("Interaktywne", "https://www.pistacja.tv/h5p/mat00012-1-a-waga-a-rownanie"),
            p(b("Zrób po lekcji:")),
            ul([li(a("ZPE — Rozwiązywanie równań", "https://zpe.gov.pl/a/rozwiazywanie-rownan/D19oMGK23"),
                   " — ćwiczenia 1–4"),
                li("Zestaw 24 zadań: zadania 1–2")]),
            p(em("Sprawdź: umiesz powiedzieć „x = 12 spełnia x + 7 = 19, bo 12 + 7 = 19”.")),
        ],
    },
    {
        "n": 2, "t": "Dodawanie i odejmowanie obu stron", "time": "20 minut",
        "body": [
            link_line("Obejrzyj", PIST + "mat00383-rozwiazywanie-rownan-wprowadzenie"),
            p(b("Zrób po lekcji:")),
            ul([li(a("Matzoo — Rozwiązywanie równań, zestaw 1",
                     "https://matzoo.pl/klasa7/rozwiazywanie-rownan-zestaw-1_57_370"),
                   " — pierwsze 10 przykładów"),
                li("Zestaw 24 zadań: zadania 1–2")]),
            p(em("Zasada: x + 5 = 12 → odejmujesz 5 od obu stron → x = 7. "
                 "Przenoszenie na drugą stronę to skrót tej operacji, ze zmianą znaku.")),
        ],
    },
    {
        "n": 3, "t": "Mnożenie i dzielenie obu stron", "time": "20 minut",
        "body": [
            link_line("Obejrzyj", PIST + "mat00384-rozwiazywanie-rownan-rozwiazanie-w-dwoch-krokach"),
            p(b("Zrób po lekcji:")),
            ul([li(a("Matzoo — zestaw 2", "https://matzoo.pl/klasa7/rozwiazywanie-rownan-zestaw-2_57_371"),
                   " — 8–10 przykładów"),
                li("Zestaw 24 zadań: zadania 3–6")]),
            p(em("Kolejność: najpierw dodaj lub odejmij, potem podziel obie strony przez współczynnik.")),
        ],
    },
    {
        "n": 4, "t": "Powtórka bez nowego materiału", "time": "20 minut",
        "body": [
            p(b("Zrób:")),
            ul([li(a("ZPE — ćwiczenia „Równania równoważne – wstęp”",
                     "https://zpe.gov.pl/a/cwiczenia/DvkyZQ1jX")),
                li("Zestaw 24 zadań: zadania 1–6 jeszcze raz, bez zaglądania do odpowiedzi"),
                li("Zapisz w zeszycie błędów każde zadanie, które nie wyszło za pierwszym razem")]),
            p(em("6 z 6 dobrze? Przechodzisz do kroku 5. Mniej niż 5? Powtórz kroki 2 i 3.")),
        ],
    },
    {
        "n": 5, "t": "Nawiasy i x po obu stronach", "time": "25 minut",
        "body": [
            link_line("Obejrzyj", PIST + "mat00385-rozwiazywanie-rownan-rownania-z-nawiasami"),
            p(b("Zrób po lekcji:")),
            ul([li("Zestaw 24 zadań: zadania 13–18"),
                li(a("Matzoo — zestaw 2", "https://matzoo.pl/klasa7/rozwiazywanie-rownan-zestaw-2_57_371"),
                   " — 5 przykładów z nawiasami")]),
            p(em("Minus przed nawiasem zmienia znaki wszystkich składników: −(x − 3) = −x + 3.")),
        ],
    },
    {
        "n": 6, "t": "Ułamki w równaniach", "time": "25 minut",
        "body": [
            link_line("Obejrzyj", PIST + "mat00386-rozwiazywanie-rownan-rownania-z-ulamkami"),
            p(b("Zrób po lekcji:")),
            ul([li("Zestaw 24 zadań: zadania 19–20"),
                li(a("ZPE — Rozwiązywanie równań", "https://zpe.gov.pl/a/rozwiazywanie-rownan/D19oMGK23"),
                   " — przykłady z ułamkami")]),
            p(em("W x/2 + x/3 = 5 mnożysz całe obie strony przez 6, a nie tylko mianowniki.")),
        ],
    },
    {
        "n": 7, "t": "Równania sprzeczne i tożsamościowe", "time": "15 minut",
        "body": [
            link_line("Obejrzyj", PIST + "mat00387-rownania-oznaczone-nieoznaczone-i-sprzeczne"),
            p(b("Zrób po lekcji:")),
            ul([li("Zestaw 24 zadań: zadania 21–22")]),
            p(em("0 = 1 → sprzeczne, brak rozwiązań. 0 = 0 → tożsamość, każde x jest rozwiązaniem.")),
        ],
    },
    {
        "n": 8, "t": "Zadania tekstowe i przekształcanie wzorów", "time": "25 minut",
        "body": [
            link_line("Obejrzyj", PIST + "mat00371-przeksztalcenia-wzorow"),
            p(b("Zrób po lekcji:")),
            ul([li(a("ZPE — zadania tekstowe za pomocą równań",
                     "https://zpe.gov.pl/a/rozwiazywanie-zadan-tekstowych-za-pomoca-rownan/D1G6Bgq3k")),
                li("Zestaw 24 zadań: zadania 23–24"),
                li(a("MatFiz24 — zadania z latami", "https://matfiz24.pl/rownania/zadania-z-latami"),
                   " — 3 przykłady")]),
            p(em("Schemat: przeczytaj → nazwij niewiadomą → ułóż równanie → rozwiąż → sprawdź, czy wynik ma sens.")),
        ],
    },
    {
        "n": 9, "t": "Sprawdzian — 8 zadań, 15 minut", "time": "20 minut",
        "body": [
            p(b("Zrób: "), a("Sprawdzian — Rozwiązywanie równań",
                             "https://szaloneliczby.pl/rozwiazywanie-rownan-sprawdzian-klasa-7/")),
            p("8 zadań, 10 punktów, 15 minut. Po sprawdzeniu zapisz błędy w zeszycie."),
            p(b("Dodatkowo: "), a("sprawdzian z 14 zadaniami",
                                 "https://szaloneliczby.pl/rownania-z-jedna-niewiadoma-sprawdzian-klasa-7/"),
              " · ", a("karty pracy do wydruku", "https://matematykagryzie.pl/baza-wiedzy/rozwiazywanie-rownan-karty-pracy")),
        ],
    },
    {
        "n": 10, "t": "Powtórka tylko tego, co nie wyszło", "time": "20 minut",
        "body": [
            p(b("Zrób:")),
            ul([li("Otwórz zeszyt błędów i rozwiąż ponownie tylko te zadania, które wcześniej nie wyszły"),
                li(a("Matzoo — zestaw 2", "https://matzoo.pl/klasa7/rozwiazywanie-rownan-zestaw-2_57_371"),
                   " — 10 przykładów na koniec"),
                li("Zestaw 24 zadań: poziom, który sprawiał najwięcej problemów")]),
            p(em("Cel: 8 z 8 w sprawdzianie i zero powtarzających się błędów. Jeśli błąd wraca trzeci raz — poproś o pomoc przy tym jednym typie zadania.")),
        ],
    },
]

TASKS = [
    "x + 7 = 19", "x − 5 = 8", "4x = 36", "x/3 = 7", "2x + 3 = 11", "5x − 4 = 21",
    "3x + 7 = 22", "5x − 8 = 12", "−2x + 9 = 1", "7 − 3x = −8", "x/4 + 3 = 5", "(2/3)x = 8",
    "2(x + 3) = 16", "3(x − 1) = 2x + 5", "4x + 3 = 2x + 11", "5(x − 2) = 3(x + 4)",
    "2(3x − 1) = 4x + 10", "3x − 2(x + 1) = 5", "x/2 + x/3 = 5", "(x + 1)/2 = (2x − 3)/5",
    "2(x + 1) = 2x + 3", "3(x − 2) = 3x − 6",
    "Ojciec ma 42 lata, syn 12. Za ile lat ojciec będzie dwa razy starszy od syna?",
    "W trójkącie drugi kąt jest 2 razy większy od pierwszego, a trzeci o 20° większy od pierwszego. Podaj miary kątów.",
]
ANSWERS = ("1. 12 · 2. 13 · 3. 9 · 4. 21 · 5. 4 · 6. 5 · 7. 5 · 8. 4 · 9. 4 · 10. 5 · 11. 8 · "
           "12. 12 · 13. 5 · 14. 8 · 15. 4 · 16. 11 · 17. 6 · 18. 7 · 19. 6 · 20. −11 · "
           "21. brak rozwiązań · 22. każde x · 23. za 18 lat · 24. 40°, 80°, 60°")

content = [
    p("Plan na 3 tygodnie: 10 kroków po około 20 minut. W każdym kroku masz film, "
      "ćwiczenia i zadania do zrobienia — po kolei, bez przeskakiwania."),
    h3("Jak korzystać"),
    ul([
        li(b("Jeden krok = jedna sesja."), " Nie rób dwóch kroków pod rząd."),
        li(b("Najpierw film, potem zadania."), " Nie odkładaj ćwiczeń na później."),
        li(b("Po każdym zadaniu sprawdź wynik podstawieniem."), " Podstaw x do pierwotnego równania."),
        li(b("Prowadź zeszyt błędów:"), " zadanie, co zrobiłeś, jak powinno być."),
    ]),
]

def flat_text(node):
    if isinstance(node, str):
        return node
    if isinstance(node, list):
        return "".join(flat_text(x) for x in node)
    if isinstance(node, dict):
        return flat_text(node.get("children") or [])
    return ""


def normalize(nodes):
    out = []
    for n in nodes:
        if isinstance(n, list):
            out.extend(normalize(n))
            continue
        text = flat_text(n.get("children") or [])
        if n.get("tag") == "p" and text.strip() in {"Zrób po lekcji:", "Zrób:", "Zrób"}:
            out.append(h4("✎ Zrób po lekcji"))
            continue
        out.append(n)
    return out

for s in STEPS:
    content.append(h3(("☐ " if s["n"] else "") + f"Krok {s['n']} · {s['t']}"))
    content.append(p(em(s["time"])))
    content.extend(normalize(s["body"]))

content.append(h3("Zestaw 24 zadań"))
content.append({"tag": "ol", "children": [li(t) for t in TASKS]})
content.append(p(b("Odpowiedzi: "), ANSWERS))
content.append(p(em("21: brak rozwiązań (0 = 1). 22: tożsamość (0 = 0). "
                    "23: 42 + x = 2(12 + x). 24: x + 2x + (x + 20°) = 180°.")))

content.append(h3("Pięć zasad, które robią różnicę"))
content.append({"tag": "ol", "children": [
    li(b("Zapisuj każdą operację pod równaniem."), " Nie licz w pamięci."),
    li(b("Przenosisz = zmieniasz znak."), " x + 5 = 12 → x = 12 − 5."),
    li(b("Dzielisz lub mnożysz całe obie strony"), " — nie tylko wybrany fragment."),
    li(b("Minus przed nawiasem zmienia wszystkie znaki"), " w środku."),
    li(b("Zawsze sprawdzaj przez podstawienie."), " To 10 sekund i wyłapuje większość błędów."),
]})

content.append(p(em("Źródła: Pi-stacja (pistacja.tv), Matzoo, Zintegrowana Platforma Edukacyjna, "
                    "Szalone Liczby, MatFiz24, Matematyka Gryzie.")))

token = None
if os.path.exists(TOKEN_FILE):
    token = open(TOKEN_FILE).read().strip()
else:
    acc = call("createAccount", short_name="rownania", author_name="Plan nauki")
    token = acc["access_token"]
    open(TOKEN_FILE, "w").write(token)

title = "Równania krok po kroku — klasa 7"
url_file = "/opt/data/projects/rownania-klasa7/.telegraph_url"
if os.path.exists(url_file):
    path = open(url_file).read().strip().rsplit("/", 1)[-1]
    page = call(
        "editPage",
        access_token=token,
        path=path,
        title=title,
        author_name="Plan nauki",
        content=json.dumps(content, ensure_ascii=False),
        return_content="false",
    )
else:
    page = call(
        "createPage",
        access_token=token,
        title=title,
        author_name="Plan nauki",
        content=json.dumps(content, ensure_ascii=False),
        return_content="false",
    )
print(page["url"])
open("/opt/data/projects/rownania-klasa7/.telegraph_url", "w").write(page["url"])
