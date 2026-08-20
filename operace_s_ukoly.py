# Štefan na konci 4. lekce říkal (od času 03:00:00), že v rámci 1. projektu máme navrhnout vlastní modul a ten pak importovat, 
# tedy se o to zde pokouším.

ukoly = []
user_input = 0

# Funkce by měla zobrazit hlavní menu s nabídkou možností.
def hlavni_menu():
    print()
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    global user_input
    user_input = input("Vyberte možnost (1-4): ")

# Funkce na základě vstupu vytvoří nový úkol a uloží jej do seznamu úkolů. 
def pridat_ukol():
    print()
    nazev_ukolu = input("Zadejte název úkolu: ")
    popis_ukolu = input("Zadejte popis úkolu: ")

    if nazev_ukolu == ("") or popis_ukolu == (""):
        print()
        print("Zadán prázdný vstup u názvu úkolu či popisu úkolu. Zadejte prosím znovu.")
        return pridat_ukol()
        
    konkretni_ukol = {
        "Název úkolu": str(nazev_ukolu),
        "Popis úkolu": str(popis_ukolu)
    }

    global ukoly
    ukoly.append(konkretni_ukol)
    print(f"Úkol '" + konkretni_ukol["Název úkolu"] + "' byl přidán.")

# Tato funkce má zobrazit všechny úkoly v seznamu.
def zobrazit_ukoly():
    print()
    print("Seznam úkolů:")

    global ukoly
    for cislo_cyklu, hodnota in enumerate(ukoly):
        print(f"{cislo_cyklu + 1}" + ". " + hodnota["Název úkolu"] + " - " + hodnota["Popis úkolu"])

# Tato funkce má uživateli umožnit zadat číslo úkolu, který chce odstranit, a tento úkol odstranit.
def odstranit_ukol():
    global ukoly
    pocet_ukolu = len(ukoly)

# Podmínka, která nepustí uživatele dál, pokud je seznam úkolů prázdný. Jinak by se uživatel dostal do pasti.
    if pocet_ukolu == 0:
        print()
        print("Seznam úkolů je prázdný, tedy nelze žádný úkol smazat. Návrat do hlavního menu.")
        return  
               
    zobrazit_ukoly()
    print()
    cislo_ukolu = input("Zadejte číslo úkolu, který chcete odstranit: ")

    try:
        cislo_ukolu = int(cislo_ukolu)
    except ValueError:
        cislo_ukolu = "Chyba"

    if cislo_ukolu == "Chyba" or cislo_ukolu > pocet_ukolu or cislo_ukolu <= 0:
        print()
        print("Vybrán neexistující úkol. Zvolte prosím znovu.")
        return odstranit_ukol()

    odstraneny_ukol = ukoly.pop(cislo_ukolu - 1)
    print("Úkol '" + odstraneny_ukol["Název úkolu"] + "' byl odstraněn.")