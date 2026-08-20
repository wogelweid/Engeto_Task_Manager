# Testovací scénáře pro projekt Engeto_Task_Manager

Vaším úkolem je vytvořit testovací případy (TC) pro každou funkci v projektu Task manager. Tyto případy by měly pokrýt všechny možné cesty a okrajové případy pro každou z funkcí. Testovací případy budou sloužit jako návrh pro automatické testy nebo manuální ověření správnosti programu. Testovací případy musí být přehledně zapsány ve formátu Markdown (.md) a uloženy jako samostatný soubor (např. test_cases.md) v rámci struktury projektu.

## Co je potřeba vytvořit:

### Seznam testovacích případů:
- Pro každou funkci (hlavni_menu, pridat_ukol, zobrazit_ukoly, odstranit_ukol) vytvořte samostatnou sadu testovacích případů.
- Popište konkrétní kroky testování, očekávané výsledky a situace, které by mohly nastat (např. chybové stavy).

### Pokrytí různých typů testů:
- Pozitivní testy: Situace, kdy je funkce použita správně (např. přidání úkolu s platnými vstupy).
- Negativní testy: Situace, kdy uživatel zadá neplatné nebo neúplné údaje (např. prázdný název úkolu).
- Hraniční případy: Například přidání prvního úkolu, zobrazení prázdného seznamu, odstranění posledního úkolu.

### Popis testovacích případů:
- Každý případ by měl obsahovat:
    - Název testovacího případu.
    - Popis (detailnější vysvětlení, co je cílem testu).
    - Vstupní podmínky (např. jaký je stav seznamu úkolů před testem).
    - Kroky testu (co má uživatel udělat, nebo jaká data zadat).
    - Očekávaný výsledek (co má program udělat nebo zobrazit).
    - Skutečný výsledek (co program udělal).
    - Stav ( Pass / Fail ).
    - Poznámky (např. proč je tento případ důležitý).

---

## A. hlavni_menu()

### TCA01: Zobrazení hlavního menu
- **Popis:** Ověření, že se hlavní menu správně zobrazí.
- **Vstupní podmínky:** Program ještě není spuštěn.
- **Kroky testu:**
    1. Spustit Visual Studio Code.
    2. Vybrat soubor Main.py.
    3. Kliknout na "Run Python File".
- **Očekávaný výsledek:** Zobrazí se hlavní menu programu a to v této podobě:
    "Správce úkolů - Hlavní menu"
    "1. Přidat nový úkol"
    "2. Zobrazit všechny úkoly"
    "3. Odstranit úkol"
    "4. Konec programu"
    "Vyberte možnost (1-4): "

    přičemž na konci posledního řádku má program očekávat uživatelský vstup.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje základní funkčnost programu.

### TCA02: Ukončení programu
- **Popis:** Ověření, že se program správně ukončí.
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:**
    1. Zadat číslo 4 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše prázdný řádek + "Konec Programu." a ukončí se.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje základní funkčnost programu, tj. jeho ukončení.

### TCA03: Neplatný vstup v hlavním menu
- **Popis:** Ověření, že program správně zareaguje, když se zadá neplatný vstup (tj. cokoliv mimo 1, 2, 3, 4).
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:**
    1. Postupně zadat "0", "5", "-1", "-4", "jedna", "B", "2.3", "3.000001", "10/5", "". Jednotlivé volby potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Ve všech případech neplatného vstupu by měl program vypsat...
    prázdný řádek
    "Zadána neplatná volba. Zadejte prosím znovu."
    prázdný řádek

    A následně znovu zobrazit hlavní menu s očekávání uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje základní funkčnost programu. Neošetřený neplatný vstup by mohl způsobit kritické selhání.

---

## B. pridat_ukol()

### TCB01: Výběr platné možnosti z menu ("1. Přidat nový úkol")
- **Popis:** Ověření, že volba čísla 1 v hlavním menu správně spustí funkci pridat_ukol().
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:**
    1. Zadat číslo 1 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program spustí funkci pridat_ukol(), tj. zobrazí prázdný řádek + "Zadejte název úkolu: ", přičemž dále očekává uživatelský vstup.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje základní navigaci z hlavního menu a funkčnost jedné z klíčových funkcí programu.

### TCB02: Zadání názvu a popisu úkolu
- **Popis:** Ověření, že funkce pridat_ukol() udělá, co je od ní očekáváno.
- **Vstupní podmínky:** Program vypisuje prázdný řádek + "Zadejte název úkolu: " a čeká na uživatelský vstup.
- **Kroky testu:**
    1. Zadat "Úkol 1" a potvrdit stisknutím klávesy Enter.
    2. Zadat "Popis Úkolu 1" a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** U "Zadejte název úkolu: " program přijme uživatelský vstup a pak jej ještě přijme u "Zadejte popis úkolu: ". Poté vypíše "Úkol 'Úkol 1' byl přidán." + prázdný řádek a zobrazí hlavní menu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje funkčnost jedné z klíčových funkcí programu.

### TCB03: Zadání prázdného vstupu u funkce pridat_ukol()
- **Popis:** Ověření, že je ošetřena situace, kdy je zadán prázdný vstup při zadávání názvu či popisu úkolu. 
- **Vstupní podmínky:** Program vypisuje prázdný řádek + "Zadejte název úkolu: " a čeká na uživatelský vstup.
- **Kroky testu:**
    1. Nezadávat nic a potvrdit stisknutím klávesy Enter.
    2. Opět nezadávat nic a potvrdit stisknutím klávesy Enter.
    3. Ukončit program a provést 2x celé znovu s těmi rozdíly, že nejdříve se nezadá nic při zadávání názvu úkolu, pak se zadá "Popis Úkolu 1" a při druhé iteraci se při zadávání úkolu zadá "Úkol 1" a pak se nezadá nic u výzvy k popisu úkolu.
- **Očekávaný výsledek:** Ve všech 3 případech by se mělo po zadání popisu úkolu zobrazit prázdný řádek + "Zadán prázdný vstup u názvu úkolu či popisu úkolu. Zadejte prosím znovu." + prázdný řádek a pak "Zadejte název úkolu: " s očekáváním uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje, jak jsou ošetřeny nechtěné vstupy, které by jinak mohly způsobit kritické selhání funkcionality programu.

---

## C. zobrazit_ukoly()

### TCC01: Výběr platné možnosti z menu ("2. Zobrazit všechny úkoly"), když je seznam úkolů prázdný
- **Popis:** Ověření, že volba čísla 2 v hlavním menu správně spustí funkci zobrazit_ukoly.
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:**
    1. Zadat číslo 2 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše prázdný řádek + "Seznam úkolů: " + prázdný řádek. Načež se zobrazí hlavní menu s očekávání uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** V požadavcích na vytvoření aplikace nebylo požadováno, aby se program zachoval nějak konkrétně, když se má zobrazit seznam úkolů, který je prázdný. Nejedná se o něco, co by způsobilo selhání programu, či uvrhlo uživatele do pasti. Vypsáním "Seznam úkolů: " a ničím dalším je uživatel dostatečně informován, že seznam úkolů je prázdný.

### TCC02: Výběr platné možnosti z menu ("2. Zobrazit všechny úkoly"), když je již vytvořen úkol
- **Popis:** Ověření, že volba čísla 2 v hlavním menu správně spustí funkci zobrazit_ukoly a také, že správně zobrazí již vytvořený úkol.
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Předtím byl přes funkci pridat_ukol() přidán úkol "Úkol 1" s popisem "Popis úkolu 1".
- **Kroky testu:**
    1. Zadat číslo 2 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše: 
    prázdný řádek
    "Seznam úkolů:"
    "1. Úkol 1 - Popis úkolu 1"
    prázdný řádek

    Načež se zobrazí hlavní menu s očekávání uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje, zda funguje klíčová funkcionalita programu a to, že se zadaný úkol skutečně uložil a na požádání zobrazil.

### TCC03: Výběr platné možnosti z menu ("2. Zobrazit všechny úkoly"), když je již vytvořen úkol, ale předtím ještě byl při přidávání úkolu zadán prázdný vstup (dle testovacího scénáře TCB03)
- **Popis:** Ověření, že zadávání prázdného vstupu při vytváření úkolu nechtěně nevytvořilo záznam v seznamu úkolů.
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Předtím byl přes funkci pridat_ukol() přidán úkol "Úkol 1" s popisem "Popis úkolu 1". A předtím byl ještě proveden testovací scénář TCB03 se všemi variantami.
- **Kroky testu:**
    1. Zadat číslo 2 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše: 
    prázdný řádek
    "Seznam úkolů:"
    "1. Úkol 1 - Popis úkolu 1"
    prázdný řádek

    Načež se zobrazí hlavní menu s očekávání uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje, zda program neuloží do seznamu neplatně zadaný vstup při vytváření úkolu. Není záhodno, aby se uložil buď popis úkolu bez jména či úkol bez popisu.

### TCC04: Výběr platné možnosti z menu ("2. Zobrazit všechny úkoly"), když je již vytvořen úkol, poté přidání dalších 2 úkolů a poté opětovné zobrazení seznamu úkolů.
- **Popis:** Ověření, že volba čísla 2 v hlavním menu správně spustí funkci zobrazit_ukoly a také, že správně zobrazí již vytvořený úkol.
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Předtím byl přes funkci pridat_ukol() přidán úkol "Úkol 1" s popisem "Popis úkolu 1".
- **Kroky testu:**
    1. Zadat číslo 2 a potvrdit stisknutím klávesy Enter.
    2. Zkontrolovat, zda zobrazený seznam úkolů odpovídá očekávání.
    3. Zadat číslo 1 a vytvořit "Úkol 2" - "Popis pro úkol 2".
    4. Zadat číslo 1 a vytvořit "Úkol 3" - "Popis pro úkol 3".
    5. Zadat číslo 2 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše: 
    prázdný řádek
    "Seznam úkolů:"
    "1. Úkol 1 - Popis úkolu 1"
    "1. Úkol 2 - Popis úkolu 2"
    "1. Úkol 3 - Popis úkolu 3"
    prázdný řádek

    Načež se zobrazí hlavní menu s očekávání uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je málo důležitý, protože spíše jen pro jistotu ověřuje, že program bez chyby zvládá kombinaci už ověřených činností.

### TCC05: Výběr platné možnosti z menu ("2. Zobrazit všechny úkoly") a to poté, co byl jeden úkol ze seznamu odstraněn, přičemž v seznamu byl právě jeden úkol
- **Popis:** Ověření, že když je nějaký úkol odstraněn ze seznamu úkolu, tak se v něm již nebude zobrazovat po vyvolání funkce zobrazit_ukoly().
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Předtím byl přes funkci pridat_ukol() přidán úkol "Úkol 1" s popisem "Popis úkolu 1", který byl následně odstraněn přes funkci odstranit_ukol().
- **Kroky testu:**
    1. Zadat číslo 2 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše prázdný řádek + "Seznam úkolů: " + prázdný řádek. Načež se zobrazí hlavní menu s očekávání uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje, že zda úkol nebyl odstraněn jenom formálně, ale že jej program již skutečně nezobrazuje při vyvolání zobrazit_ukoly().

### TCC06: Výběr platné možnosti z menu ("2. Zobrazit všechny úkoly") a to poté, co byl poslední úkol ze seznamu odstraněn, přičemž v seznamu byly úkoly 3
- **Popis:** Ověření, že když je nějaký úkol odstraněn ze seznamu úkolu, tak se v něm již nebude zobrazovat po vyvolání funkce zobrazit_ukoly() a zároveň to neovlivní stav ostatních uložených úkolů.
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Předtím byl přes funkci pridat_ukol() přidány úkol "Úkol 1" s popisem "Popis úkolu 1", "Úkol 2" - "Popis úkolu 2" a "Úkol 3" - "Popis úkolu 3", přičemž "Úkol 3" byl následně odstraněn přes funkci odstranit_ukol().
- **Kroky testu:**
    1. Zadat číslo 2 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše...
    prázdný řádek
    "Seznam úkolů: "
    "1. Úkol 1 - Popis úkoli 1"
    "2. Úkol 2 - Popis úkolu 2"
    prázdný řádek

    Načež se zobrazí hlavní menu s očekávání uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje, že zda úkol nebyl odstraněn jenom formálně, ale že jej program již skutečně nezobrazuje při vyvolání zobrazit_ukoly() a zároveň zda se zbývající úkoly zobrazují správně.

### TCC07: Výběr platné možnosti z menu ("2. Zobrazit všechny úkoly") a to poté, co byl prostřední úkol ze seznamu odstraněn, přičemž v seznamu byly úkoly 3
- **Popis:** Ověření, že když je nějaký úkol odstraněn ze seznamu úkolu, tak se v něm již nebude zobrazovat po vyvolání funkce zobrazit_ukoly() a zároveň to neovlivní stav ostatních uložených úkolů, respektive, že je to správných způsobem zarovná.
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Předtím byl přes funkci pridat_ukol() přidány úkol "Úkol 1" s popisem "Popis úkolu 1", "Úkol 2" - "Popis úkolu 2" a "Úkol 3" - "Popis úkolu 3", přičemž "Úkol 2" byl následně odstraněn přes funkci odstranit_ukol().
- **Kroky testu:**
    1. Zadat číslo 2 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše...
    prázdný řádek
    "Seznam úkolů: "
    "1. Úkol 1 - Popis úkoli 1"
    "2. Úkol 3 - Popis úkolu 3"
    prázdný řádek

    Načež se zobrazí hlavní menu s očekávání uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje, zda úkol nebyl odstraněn jenom formálně, ale že jej program již skutečně nezobrazuje při vyvolání zobrazit_ukoly() a zároveň zda se zbývající úkoly zobrazují správně, tj. v tomto případě, že se Úkol 3 posune ze 3. řádku na 2.

---

## D. odstranit_ukol()

### TCD01: Výběr platné možnosti z menu ("3. Odstranit úkol"), když je seznamu úkolů 1 úkol
- **Popis:** Ověření, že volba čísla 3 v hlavním menu správně spustí funkci odstranit_ukol().
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Předtím byl přes funkci pridat_ukol() přidán úkol "Úkol 1" s popisem "Popis úkolu 1".
- **Kroky testu:**
    1. Zadat číslo 3 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše...
    prázdný řádek
    "Seznam úkolů: "
    "1. Úkol 1 - Popis úkolu 1"
    prázdný řádek
    "Zadejte číslo úkolu, který chcete odstranit: "

    přičemž na konci posledního řádku má program očekávat uživatelský vstup.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass
- **Poznámky:** Tento případ je důležitý, protože ověřuje základní funkčnost programu, tj. že se uživateli zobrazí seznam úkolů a je mu umožněto si vybrat, který má být smazán.

### TCD02: Výběr platné možnosti z menu ("3. Odstranit úkol"), když je seznamu úkolů prázdný
- **Popis:** Ověření, zda je ošetřena situace, kde je spušťena funkce odstranit_ukol(), přičemž je ale seznam úkolů prázdný.
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Seznam úkolů je prázdný.
- **Kroky testu:**
    1. Zadat číslo 3 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše...
    prázdný řádek
    "Seznam úkolů je prázdný, tedy nelze žádný úkol smazat. Návrat do hlavního menu."
    prázdný řádek

    Načež program znovu zobrazí hlavní menu s očekáváním uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje, zda bylo ošetřeno riziko uvržení uživatele do pasti, ve které by jej program nepustil dál (nekonečná smyčka), pokud by u prázdného seznamu neexistovala možnost vybrat úkol ke smazání.

### TCD03: Formální odstranění úkolu
- **Popis:** Ověření, že funkce odstranit úkol uživateli oznámí, že tak učinila, když ten zvolí platnou možnost.
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Předtím byl přes funkci pridat_ukol() přidán úkol "Úkol 1" s popisem "Popis úkolu 1".
- **Kroky testu:**
    1. Zadat číslo 3 a potvrdit stisknutím klávesy Enter.
    2. Zadat číslo 1 a potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program nejprve vypíše...
    prázdný řádek
    "Seznam úkolů:"
    "1. Úkol 1 - Popis úkolu 1"
    prázdný řádek
    "Zadejte číslo úkolu, který chcete odstranit: "

    přičemž na konci posledního řádku má program očekávat uživatelský vstup.

Po zadání čísla 1 pak program vypíše...
    "Úkol 'Úkol 1' byl odstraněn."

    Načež program znovu zobrazí hlavní menu s očekáváním uživatelského vstupu.
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je důležitý, protože ověřuje, zda program dává uživatel zpětnou vazbu ohledně odstraňování úkolu.

### TCD04: Zadání neplatného vstupu u odstranění úkolu
- **Popis:** Ověření, zda je ošetřen neplatný vstup při zadávání čísla úkolu k odstranění.
- **Vstupní podmínky:** Program zobrazuje hlavní menu. Předtím byl přes funkci pridat_ukol() přidán úkol "Úkol 1" s popisem "Popis úkolu 1".
- **Kroky testu:**
    1. Zadat číslo 3 a potvrdit stisknutím klávesy Enter.
    2. Postupně zadat "0", "-1", "2", "jedna", "B", "2.3", "3.000001", "10/5", "". Jednotlivé volby potvrdit stisknutím klávesy Enter.
- **Očekávaný výsledek:** Program vypíše...
    prázdný řádek
    "Vybrán neexistující úkol. Zvolte prosím znovu."
    prázdný řádek

    Načež program znovu zobrazí seznam úkolů a výzvu k zadání čísla úkolu k odstranění (spuštění funkce odstranit_ukol()).
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento úkol je důležitý, protože ověřuje, že zda byla ošetřena možnost neplatného vstupu od uživatele. Jinak by hrozilo, že by se program zasekl, když by nevěděl, jak reagovat na neznámou volbu, či by na neplatnou volbu přesto nějaký úkol k smazání vybral.

---

## E. Komplexní otestování

### TCE01: Kombinované otestování všech funkcionalit v jednom běhu programu.
- **Popis:** Ověření, že když se v jednom běhu aplikace praktikuje používání všech funkcí, tak že to nezpůspbuje chyby, ani když se zadávají neplatné vstupy.
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:**
    1. Zadat číslo 5 a potvrdit stisknutím klávesy Enter.
    2. Zadat číslo 1 a potvrdit stisknutím klávesy Enter.
    3. Zadat "Úkol 1" jako název úkolu a "Popis úkolu 1" jako popis úkolu.
    4. Zadat číslo 2 a zkontrolovat, zda je vše v pořádku.
    5. Zadat číslo 1 a potvrdit stisknutím klávesy Enter.
    6. Zadat "" jako název úkolu a "Popis úkolu 2" jako popis úkolu.
    7. Zadat "Úkol 2" jako název úkolu a "Popis úkolu 2" jako popis úkolu.
    8. Zadat číslo 2 a zkontrolovat, zda je vše v pořádku.
    9. Zadat číslo 3 a pak zadat číslo 0.
    10. Zadat číslo 3 a pak zadat číslo 1.
    11. Zadat číslo 2 a zkontrolovat, zda je vše v pořádku, tj. že se zobrazuje jenom Úkol 2 s popisem.
    12. Zadat "Úkol 1" jako název úkolu a "Popis úkolu 1" jako popis úkolu.
    13. Zadat číslo 2 a zkontrolovat, zda je vše v pořádku, tj. že se zobrazuje jako první Úkol 2 a jako druhý úkol 1. 
    14. Zadat číslo 3 a pak zadat číslo 2.
    15. Zadat číslo 3 a pak zadat číslo 2.
    16. Zadat číslo 3 a pak zadat číslo 1.
    17. Zadat číslo 2 a zkontrolovat, zda je vše v pořádku, tj. že je seznam úkolů prázdný.
    18. Zadat číslo 3 a stisknout klávesu enter.
    19. Zadat číslo 4.
- **Očekávaný výsledek:** Program by se měl v průběhu jednotlivých kroků chovat očekávaným způsobem (jak konkrétně již bylo vypsáno u jiných TC).
- **Skutečný výsledek:** Stalo se, jak bylo očekáváno.
- **Stav:** Pass.
- **Poznámky:** Tento případ je středně důležitý, protože ověřuje, že kombinování již prověřených funkcí nezpůsobí nějaké neočekávané chyby.